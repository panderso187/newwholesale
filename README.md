# Wholesale AI Blueprint

This repository contains a starter workflow for automating lead intake with Firecrawl, GPT‑4 and Airtable.

## Files

- `blueprints/firecrawl_airtable_blueprint.json` – n8n workflow that scrapes a property URL, summarizes the details, scores seller motivation and drafts a cash offer before appending to Airtable.
- `prompts/summary_prompt.txt` – GPT prompt used for property summaries and motivation scoring.
- `prompts/offer_prompt.txt` – GPT prompt used to create the offer letter.
- `airtable_schema.csv` – example Airtable table schema for the workflow output.

## Usage

1. Import `blueprints/firecrawl_airtable_blueprint.json` into your n8n instance.
2. Set up a Google Sheet with a column named `property_url` to trigger the flow.
3. Configure your Firecrawl and OpenAI credentials in n8n.
4. Create an Airtable base using the fields in `airtable_schema.csv` and update the node with your base ID.

Once configured, adding a new URL to your sheet will scrape the listing, produce a short summary, rate seller motivation and create an initial offer draft.
