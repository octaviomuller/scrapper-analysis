import schedule

from routine.websites import get_most_visited_sites
from scrapper.main import Scrapper
from dataset import Dataset

def job():
    sites = get_most_visited_sites('loja online')
    succes_request_url = []
    error_request_url = []

    for site in sites:
        try:
            data = Scrapper(site, True).execute()
            Dataset('dataset.csv', data).save()
            succes_request_url.append(site)
        except Exception as error:
            error_request_url.append({ 'url': site, 'error': error })

    print('Sites analisados com sucesso: ', succes_request_url)
    print('Sites não analisados: ', error_request_url)

def scheduler(days):
    schedule.every(days).days.do(job)

    while True:
        schedule.run_pending()
