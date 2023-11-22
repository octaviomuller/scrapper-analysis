import os
import time
from googleapiclient.discovery import build

gs_api_key = os.environ["GOOGLE_SEARCH_API_KEY"]
cse_id = os.environ["CUSTOM_SEARCH_ENGINE_ID"]

def get_most_visited_sites(keyword, website_count):
    service = build("customsearch", "v1", developerKey=gs_api_key)

    domains = "site:com.br OR site:com"
    query = f"{keyword} {domains}"

    all_sites = []
    max_results_per_page = 10

    while len(all_sites) < website_count:
        remaining_sites = website_count - len(all_sites)
        current_results = min(max_results_per_page, remaining_sites)

        res = service.cse().list(q=query, cx=cse_id, num=current_results, cr="countryBR", start=len(all_sites) + 1).execute()
        sites = list(map(lambda site: site['displayLink'], res['items']))
        all_sites.extend(sites)

        time.sleep(5)
    
    return all_sites