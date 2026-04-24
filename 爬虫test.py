from bs4 import BeautifulSoup
import requests

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0"}
url="https://movie.douban.com/top250"
x=requests.get(url,headers=headers)
soup=BeautifulSoup(x.text,"lxml")
movie_average=soup.find_all('span',class_='rating_num')
for i in movie_average:
    movie_average=movie_average.get_text()
    print(movie_average)