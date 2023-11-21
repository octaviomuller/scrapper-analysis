from dotenv import load_dotenv

from routine.cronjob import job

load_dotenv()

def main():
    job('loja online', 10)
    

if __name__ == '__main__':
    main()
