import schedule

from routine.websites import get_most_visited_sites
from scrapper.main import Scrapper
from dataset import Dataset

def job():
    sites = get_most_visited_sites('loja online')
    error_request_url = []
    succes_request_url = []

    sites.insert(0, "https://www.kabum.com.br/")

    try:
        for site in sites:
            data = Scrapper(site, True).execute()
            Dataset('dataset.csv', data).save()
            succes_request_url.append(site)
    except:
        error_request_url.append(site)

    print(succes_request_url, error_request_url)


def scheduler(days):
    schedule.every(days).days.do(job)

    while True:
        schedule.run_pending()
