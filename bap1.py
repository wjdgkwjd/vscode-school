from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://jeju-s.jje.hs.kr/jeju-s")
soup = BeautifulSoup(html, "html.parser")
##container > div.main_content > div.meal_menu > ul > li 
# > 표시는 있든없든 상관없음

bap = soup.select(".meal_menu ul li")
print("="*50)
print( bap)
print("-"*50)

menu = ""

for m in bap:
   print( m.text.strip() ) #strip은 공백 없앰
   menu = m.text

menu = menu.split(" ") #공백 단위로 나눈 것을 ,로 나눔
print(menu)
print("="*50)

i=0
for m in menu:
    i = i+1
    if m != "":
        print(i, m)