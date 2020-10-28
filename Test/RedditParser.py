import requests
from bs4 import BeautifulSoup

class RedditParser:
    subreddit_url = ""

    def __init__(self, subreddit_url):
        self.subreddit_url = subreddit_url

    def parse_basic_informations(self):
        result = ""
        if (self.subreddit_url != ""): 
            headers ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
            with requests.Session() as s:
                r = s.get(self.subreddit_url, headers=headers)
                soup = BeautifulSoup(r.content, "html.parser")
                dates = [item['data-timestamp'] for item in soup.find_all('div', class_="thing", attrs={'data-timestamp' : True})]
                authors = [item['data-author'] for item in soup.find_all('div', class_="thing", attrs={'data-author' : True})]
                topics = [item.findAll(text=True) for item in soup.find_all('a', class_="title may-blank")]

                
#                data-topic
 #               data-content
  #              data-subreddit
                
                for d in dates:
                    print (d)
                for a in authors:
                    print (a)
                for t in topics:
                    print(t)

        return result