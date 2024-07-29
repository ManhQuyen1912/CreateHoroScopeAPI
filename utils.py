import requests
from bs4 import BeautifulSoup
import json

#hàm dùng để kéo dữ liệu từ trang horoscope theo ngày
def get_horoscope_by_day(zodiac_sign: int, day: str):
    if not "-" in day:
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}")
    else:
        day = day.replace("-","")
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div',attrs={'class': 'main-horoscope'})
    new = split_horoscope_data(data.p.text)
    return new

def get_horoscope_by_week(zodiac_sign: int,day:str):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-weekly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div',attrs={'class':'main-horoscope'})
    new = split_horoscope_data(data.p.text)
    return new

def get_horoscope_by_month(zodiac_sign: int,day:str):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    new = split_horoscope_data(data.p.text)
    return new

#hàm tách ngày vs văn bản ra
def split_horoscope_data(horoscope_string):
    # Split the string at the first hyphen
    date, horoscope_data = horoscope_string.split(' - ', 1)
    # Create the JSON structure
    data = {
        "date": date,
        "horoscope_data": horoscope_data
    }
    return data
