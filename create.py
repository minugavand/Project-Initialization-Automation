import sys
from github import Github
from dotenv import load_dotenv


path = os.getenv("FILEPATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def create():
    folderName = str(sys.argv[1])
    

if __name__ == "__main__":
    create()
