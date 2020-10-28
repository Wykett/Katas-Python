from Counting import Counting
from MultipleSum import MultipleSum
from RedditParser import RedditParser

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

#PART 1 test

#------------------------------------------------------------------------------------------------------------------------

#Counting exercise
#Data to test counting
urls = ["http://www.google.com/a.txt",
	"http://www.google.com.tw/a.txt",
	"http://www.google.com/download/c.jpg",
	"http://www.google.co.jp/a.txt",
	"http://www.google.com/b.txt",
	"https://facebook.com/movie/b.txt",
	"http://yahoo.com/123/000/c.jpg",
	"http://gliacloud.com/haha.png"]
#How to test counting for url
counting = Counting(urls)
counting_result = counting.count()
print (counting_result)

#------------------------------------------------------------------------------------------------------------------------

#Multiples count exercise
#Datas to test multiple sum
list_of_multiples_to_search = [3,5]
range_start = 1
range_end = 10
#How to test multiple sum
multiple_sum = MultipleSum(list_of_multiples_to_search, range_start, range_end)
multiple_sum_result = multiple_sum.multiple_sum()
print (multiple_sum_result)

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

#PART 2 test

#------------------------------------------------------------------------------------------------------------------------
#Reddit parser
#Datas to test reddit parser
subreddit_url = "https://www.reddit.com/r/todayilearned/"
#How to test reddit parser
reddit_parser = RedditParser(subreddit_url)
reddit_parser_result = reddit_parser.parse_basic_informations()
#print (reddit_parser_result)