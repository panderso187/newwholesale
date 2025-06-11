# Property Enrichment Example

This small FastAPI app demonstrates how to enrich a Propwire CSV with data from the Estated API. A minimal Tailwind page lets you upload a CSV and download the enriched result.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file with your Estated API key:
   ```bash
   ESTATED_TOKEN=your_key_here
   ```
3. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

Navigate to `http://localhost:8000` to upload a file. The service returns a CSV with an extra `avm` column containing the estimated property value. API keys are loaded from environment variables for security.
