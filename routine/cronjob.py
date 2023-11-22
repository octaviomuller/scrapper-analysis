import schedule
from functools import partial

from routine.websites import get_most_visited_sites
from scrapper.main import Scrapper
from dataset import Dataset

def job(keyword, website_count):
    sites = get_most_visited_sites(keyword, website_count)
    succes_request_url = []
    error_request_url = []

    for site in sites:
        try:
            data = Scrapper(site, True).execute()
            Dataset('dataset.csv', data).save()
            succes_request_url.append(site)
        except Exception as error:
            error_request_url.append({ 'url': site, 'error': error })

    print(f'Total de sites analisados com sucesso: { len(succes_request_url) } / { len(sites) }')
    print('Sites analisados com sucesso: ', succes_request_url)
    print('Sites não analisados: ', error_request_url)

def scheduler(days, keyword, website_count):
    partial_job = partial(job, keyword, website_count=website_count)
    
    schedule.every(days).days.do(partial_job)

    while True:
        schedule.run_pending()
