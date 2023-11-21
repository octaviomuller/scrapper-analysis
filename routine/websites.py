import os
from googleapiclient.discovery import build

gs_api_key = os.environ["GOOGLE_SEARCH_API_KEY"]
cse_id = os.environ["CUSTOM_SEARCH_ENGINE_ID"]

def get_most_visited_sites(keyword):
    service = build("customsearch", "v1", developerKey=gs_api_key)

    domains = "site:com.br OR site:com"
    query = f"{keyword} {domains}"
    
    res = service.cse().list(q=query, cx=cse_id, num=3, cr="countryBR").execute()

    sites = map(lambda site: site['displayLink'], res['items'])
    
    return list(sites)