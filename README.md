# Lead Harvesting Tools

This repo contains a notebook and helper script for scraping public records, enriching them with an LLM and sending the results to Google Sheets and Podio. A placeholder function for REIRail skip tracing is also included.

## Setup
1. **Clone the repo** and create a Python virtual environment.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a `.env` file** in the project root and provide these variables:
   ```ini
   OPENAI_API_KEY=sk-...
   GOOGLE_CREDS_JSON_PATH=/path/to/service_account.json
   SPREADSHEET_NAME=LeadHarvestingNotebook
   PODIO_TOKEN=xxxx
   PODIO_APP_ID=123456
   REIRAIL_API_KEY=optional
   ```
   The Google credentials file comes from a service account with Sheets access.
4. **Generate the notebook**:
   ```bash
   python generate_notebook.py
   ```
   This creates `LeadHarvestingNotebook.ipynb` which contains the full pipeline code.

## Running
Open the notebook with Jupyter and call `run_pipeline(URL)` in a code cell where `URL` is a page that lists code violations (or other distress records). Each scraped row is scored by the LLM, written to your Google Sheet, and pushed to Podio. If you provided the REIRail key, skip tracing results will print in the output.

Adjust selectors inside `scrape_code_violations` if your target site uses a different table structure.
