"""
XML Sitemap URL Inventory, SEO Freshness & Content Auditor — Python Quickstart
Official Apify Store Actor: https://apify.com/lucacelli/sitemap-url-inventory-content-freshness-auditor ($0.50 / 1,000 URLs)
"""
import os
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~sitemap-url-inventory-content-freshness-auditor/run-sync-get-dataset-items"

payload = {
    "domains": [
        "apify.com",
        "vercel.com"
    ],
    "maxUrlsPerDomain": 200
}

if __name__ == "__main__":
    print(f"Running XML Sitemap URL Inventory, SEO Freshness & Content Auditor on Apify Cloud ({ENDPOINT})...")
    response = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    response.raise_for_status()
    data = response.json()
    print(f"Extracted {len(data)} records! Sample:")
    print(data[:3])
