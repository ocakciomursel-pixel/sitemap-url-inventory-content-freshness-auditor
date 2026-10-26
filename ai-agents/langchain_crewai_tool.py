"""
XML Sitemap URL Inventory, SEO Freshness & Content Auditor — LangChain, CrewAI & OpenAI Assistants Tool
Official Apify Actor: https://apify.com/lucacelli/sitemap-url-inventory-content-freshness-auditor ($0.50 / 1,000 URLs)
"""
import os
import requests
from typing import Dict, Any, List

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~sitemap-url-inventory-content-freshness-auditor/run-sync-get-dataset-items"

def run_sitemap_url_inventory_content_freshness_auditor(custom_input: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """
    Executes XML Sitemap URL Inventory, SEO Freshness & Content Auditor on Apify Cloud ($0.50/1k URLs).
    Automatically discover and parse XML sitemaps and nested sitemap indexes on any domain to extract full URL inventories, content freshness metrics, publishing velocity, and section breakdowns.
    """
    default_payload = {
    "domains": [
        "apify.com",
        "vercel.com"
    ],
    "maxUrlsPerDomain": 200
}
    payload = custom_input if custom_input else default_payload
    res = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    res.raise_for_status()
    return res.json()
