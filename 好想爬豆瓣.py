from bs4 import BeautifulSoup
import requests
import time

count=0
with open("豆瓣top250.txt","w",encoding="utf-8") as f:
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0"}

    f.write(f"{"排名".ljust(6)}{ "影名".ljust(25)}{ "评分".rjust(6)}\n")
    f.write(f"{'*' * 40}\n")
    print(f"{"排名".ljust(6)}{ "影名".ljust(25)}{ "评分".rjust(6)}\n")
    print(f"{'*' * 40}\n")
    for offset in range(0,250,25):
        url=f"https://movie.douban.com/top250?start={offset}"
        x=requests.get(url,headers=headers)
        time.sleep(1.8)
        soup=BeautifulSoup(x.text,"lxml")
        movie_blocks=soup.find_all('span',class_='title')
        movie_average=soup.find_all('span',class_='rating_num')
        chinese_name=[]
        scorce=[]
        for i in movie_blocks:
            movie_name=i.get_text()
            movie_name=movie_name.strip()
            if movie_name.startswith("/"):
                continue
            chinese_name.append(movie_name)
        for i in movie_average:
            value=i.get_text()
            scorce.append(value)
        for a,b in zip(chinese_name,scorce):
            count+=1
            f.write(f"{str(count).ljust(6)}{a.ljust(25)}{b.rjust(6)}\n")
            print(f"{str(count).ljust(6)}{a.ljust(25)}{b.rjust(6)}\n")