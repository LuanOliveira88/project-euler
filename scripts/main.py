import sys 
import os 

import requests
from bs4 import BeautifulSoup


def fetch_title(id):
    url = f"https://projecteuler.net/problem={id}"
    response = requests.get(url=url)
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.h2.get_text(strip=True)
        return title

def fetch_content(id):
    url = f"https://projecteuler.net/minimal={id}"
    response = requests.get(url=url)
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.prettify()
        return content.replace("<p>", "").replace("</p>", "<br>")

def main():
    if len(sys.argv) == 2:
        id = sys.argv[1]
        title = fetch_title(id)
        path_ = f".\\problems\\problem_{id}"    
        if os.path.exists(path=path_):
            print('Não foi possível criar esse diretório, pois já existe')
        else:
            os.mkdir(path=path_)
            with open(file=os.path.join(path_, "main.py"), mode="w") as file:
                file.write("# Shine On  You Crazy Diamond")
            with open(file=os.path.join(path_, "main_test.py"), mode="w") as file:
                file.write("# Test Here")

            with open(file=os.path.join(path_, "README.md"), mode="w") as file:
                file.write(f"# {title}\n\n")
                file.write(f"## Problem {id}\n\n")
                file.writelines(fetch_content(id))

if __name__ == '__main__':
    main()
                