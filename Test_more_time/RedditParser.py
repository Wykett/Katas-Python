import requests
import datetime
from bs4 import BeautifulSoup

class RedditParser:
    subreddit_url = ""

    def __init__(self, subreddit_url):
        self.subreddit_url = subreddit_url

    #def format_date_from_timestamp(self, d):
        
     #   return time_format

    def parse_basic_informations(self):
        result = []
        if (self.subreddit_url != ""): 
            headers ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
            with requests.Session() as s:
                r = s.get(self.subreddit_url, headers=headers)
                soup = BeautifulSoup(r.content, "html.parser")
                dates = [item['data-timestamp'] for item in soup.find_all('div', class_="thing", attrs={'data-timestamp' : True})]
                authors = [item['data-author'] for item in soup.find_all('div', class_="thing", attrs={'data-author' : True})]
                topics = soup.select('a.title.may-blank')
                contents = []
                subreddits = [item['data-subreddit'] for item in soup.find_all('div', class_="thing", attrs={'data-subreddit' : True})]
                                
 #               data-content ?
                
                print (len(dates))
                print (len(authors))
                print (len(topics))
                print (len(subreddits))

                dict = {}
                for i in range(0,len(dates)):
                    d = dates[i]
                    if len(d) == 13:
                        d = int(str(d)[0:-3])
                    time = datetime.datetime.utcfromtimestamp(d)
                    time_format = time.strftime('%Y-%m-%d %H:%M:%S')
                    dict["Date"] = time_format
                    dict["Author"] = authors[i]
                    dict["Topics"] = topics[i].text
                    dict["Content"] = ""
                    dict["Subreddit"] = subreddits[i]
                    result.append(dict)
                
        return result