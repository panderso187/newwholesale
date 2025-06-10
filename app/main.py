from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import httpx
import os
import io

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

ESTATED_TOKEN = os.getenv("ESTATED_TOKEN")

if not ESTATED_TOKEN:
    raise RuntimeError("ESTATED_TOKEN missing in environment")

async def fetch_estated(session: httpx.AsyncClient, address: str, city: str, state: str, zip_code: str):
    url = (
        "https://api.estated.com/v4/property?"
        f"address={address},{city},{state}&postal_code={zip_code}&token={ESTATED_TOKEN}"
    )
    resp = await session.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/enrich")
async def enrich(csv_file: UploadFile = File(...)):
    try:
        contents = await csv_file.read()
        df = pd.read_csv(io.BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid CSV: {e}")

    async with httpx.AsyncClient() as session:
        results = []
        for _, row in df.iterrows():
            try:
                data = await fetch_estated(session, row['address'], row['city'], row['state'], str(row['zip']))
                avm = data.get('data', {}).get('valuation', {}).get('value')
                results.append({**row, 'avm': avm})
            except Exception:
                results.append({**row, 'avm': None})

    output = io.StringIO()
    pd.DataFrame(results).to_csv(output, index=False)
    output.seek(0)
    return StreamingResponse(iter([output.getvalue()]), media_type='text/csv')
