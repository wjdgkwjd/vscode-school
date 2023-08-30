from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen()

soup = BeautifulSoup(html, "html.parser")
news = soup.select("#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt> a")
n=0
for  new in news:
    url=new.get("href") 
    new=new.text.strip()
    if  new !="" :
        n +=1
        print( "{:02d}".format(n), new) #:02d는 2자리 수로 출력하라는 뜻
        print( "   ", url)

##main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a")

soup = BeautifulSoup(html, "html.parser")
news = soup.select("#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt> a")
n=0
for  new in news:
    url=new.get("href") 
    new=new.text.strip()
    if  new !="" :
        n +=1
        print( "{:02d}".format(n), new) #:02d는 2자리 수로 출력하라는 뜻
        print( "   ", url)

##main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a