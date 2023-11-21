from dotenv import load_dotenv

from routine.cronjob import job
from scrapper.main import Scrapper

load_dotenv()

def main():
    # Scrapper('https://www.lojaintegrada.com.br/', False).execute()
    job()
    

if __name__ == '__main__':
    main()
