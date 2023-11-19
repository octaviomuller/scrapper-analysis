from scrapper.main import Scrapper
from dataset import Dataset

def main():
    data = Scrapper('https://www.kabum.com.br/', True).execute()
    Dataset('dataset.csv', data).save()

if __name__ == '__main__':
    main()
