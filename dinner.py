from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import re
# from imageUrlToSave import  save_image

today = str(datetime.date.today())
print("today",today)
meal_name="lunch"

url=f"http://jeju-s.jje.hs.kr/jeju-s/food/{today.replace('-','/')}/{meal_name}"
html = urlopen( url)
soup = BeautifulSoup(html, "html.parser")

bap_date = soup.select(".txt_date")[0].text
bap_title = soup.select(".food_pop>h2")[0].text
bap = soup.select(".ulType_food > li:nth-child(2) > dl > dd")[0].text
image=soup.select(".food_img> img")[0].get("src")
image_url="http://jeju-s.jje.hs.kr" + image
print(bap)

print("#"*100)