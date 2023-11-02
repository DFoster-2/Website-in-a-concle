import requests
import threading
from bs4 import BeautifulSoup

def forward_traffic(url):
    while True:
        response = requests.get(url)
        #print(response.content)
        soup = BeautifulSoup(response.content)
        print(soup.get_text())
def main():
    url = "https://shellshock.io"

    threading.Thread(target=forward_traffic, args=(url,)).start()
if __name__ == "__main__":
    main()