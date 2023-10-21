from scrapper.main import Scrapper

def main():
    scrapper = Scrapper('https://www.kabum.com.br')
    print(scrapper.execute())

if __name__ == '__main__':
    main()