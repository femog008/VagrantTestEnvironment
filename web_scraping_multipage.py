from bs4 import BeautifulSoup
import requests
import pandas as pd

# Variables
names = []
locations = []
reviews = []
query_string = "?start="

# Get page object
page = requests.get("https://www.yelp.com/biz/bar-karaoke-lounge-toronto")
soup = BeautifulSoup(page.content, 'html.parser')

# Get pagination count
pagination = soup.select("div.border-color--default__373c0__3-ifU div.pagination-link-container__373c0__1mmdE a")
length = len(pagination)

# Loop through pagination
for i in range(length + 1):
    if i == 0:
        page = requests.get("https://www.yelp.com/biz/bar-karaoke-lounge-toronto")
    else:
        page = requests.get("https://www.yelp.com/biz/bar-karaoke-lounge-toronto" + query_string + str(i*20))
        
    soup = BeautifulSoup(page.content, 'html.parser')
   
    review_section = soup.select(".list__373c0__3GI_T .review__373c0__13kpL")
    reviews_unordered_list = BeautifulSoup(("".join(str(x) for x in review_section)), 'html.parser')

    current_page_names = [pt.get_text() for pt in reviews_unordered_list.select(".review__373c0__13kpL .user-passport-info span a")]
    current_page_locations = [pt.get_text() for pt in reviews_unordered_list.select(".review__373c0__13kpL .user-passport-info div span")]
    current_page_reviews = [pt.get_text() for pt in reviews_unordered_list.select(".review__373c0__13kpL .margin-b2__373c0__abANL p span")]
    

    names += current_page_names
    locations += current_page_locations
    reviews += current_page_reviews

    print(len(reviews_unordered_list.select(".review__373c0__13kpL")))
    print(len(names))
    print("##############")

# Convert to table format
all_reviews = pd.DataFrame({
    "name": names,
    "locations": locations,
    "reviews":reviews
})

# Save to csv
all_reviews.to_csv('/vagrant_data/reviews.csv', ',')
