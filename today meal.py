from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
#import dsLib

today = str(datetime.date.today())
#today="2023-08-30"
t=today.split("-")
# t=['2023','08','30']


# https://jeju-s.jje.hs.kr/jeju-s/food/2023/08/17/breakfast

meal_name=["breakfast","lunch","diner"]

for  period_Name in meal_name:
     
      print(period_Name)
      print("="*60)

      url=f"http://jeju-s.jje.hs.kr/jeju-s/food/{t[0]}/{t[1]}/{t[2]}/{period_Name}"

      html = urlopen(url)
      soup = BeautifulSoup(html, "html.parser")

      bap_title = soup.select(".food_pop>h2")[0].text
      bap_title = bap_title.replace("\t"," ").replace("\n","").replace("\r","")
      print(bap_title)
      bap = soup.select(".ulType_food > li:nth-child(2) > dl > dd")[0].text
     
      print(bap)
      print("="*60)