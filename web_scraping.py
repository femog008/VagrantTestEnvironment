from bs4 import BeautifulSoup
import requests
import pandas as pd


page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
# forecast_items = seven_day.find_all(class_="tombstone-container")
# tonight = forecast_items[0]
# period = tonight.find(class_="period-name").get_text()
# short_desc = tonight.find(class_="short-desc").get_text()
# temp = tonight.find(class_="temp").get_text()
# img = tonight.find("img")
# desc = img['title']
# print(desc)
# print(period)
# print(short_desc)
# print(temp)
print(type(seven_day))
print(type(seven_day.select(".tombstone-container .period-name")[0]))
periods = [pt.get_text() for pt in seven_day.select(".tombstone-container .period-name")]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})

# for i in range(10):
#     print(i)

# print(periods)
# print(short_descs)
# print(temps)
# print(descs)
print(type(seven_day))

print(weather)

# weather.to_csv('out.csv', ',')