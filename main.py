from dotenv import load_dotenv

from routine.cronjob import job

load_dotenv()

def main():
    job('lojas online de departamentos diversos', 100)
    

if __name__ == '__main__':
    main()
