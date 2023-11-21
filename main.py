from dotenv import load_dotenv
from dataset.dataset import Dataset

from routine.cronjob import job
from scrapper.main import Scrapper

load_dotenv()

def main():
    # data = Scrapper('www.zattini.com.br', True).execute()
    # Dataset('dataset.csv', data).save()
    job('loja online', 10)
    

if __name__ == '__main__':
    main()
