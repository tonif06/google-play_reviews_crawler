'''


!pip install google-play-scraper
!pip install pandas
!pip install numpy
!pip install openpyxl

'''

from google_play_scraper import Sort, reviews_all, reviews, app
from datetime import datetime
import pandas as pd
import numpy as np
import datetime


### EXTRAGE REVIEWS

lista_android = pd.read_csv("C:/Users/antfiera/Documents/GitHub/google-play_reviews_crawler/in.csv")
all_data = pd.DataFrame()


for _app in lista_android["app_name"]:
 result1 = reviews_all(
 _app,
 sleep_milliseconds=5, # defaults to 0
 lang='ro', # defaults to 'ro'
 country='ro', # defaults to 'ro'
 sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT , you can use Sort.NEWEST to get newst reviews
 )
 
 scrapeddata = pd.DataFrame(np.array(result1),columns=['review'])
 
 
 scrapeddata["appl"]=_app
 scrapeddata["cules la"]=datetime.datetime.now()
 scrapeddata = scrapeddata.join(pd.DataFrame(scrapeddata.pop('review').tolist()))
 all_data = all_data.append(scrapeddata)

all_data=all_data.drop(columns=['userImage'])
all_data.to_excel("C:/Users/antfiera/Documents/GitHub/google-play_reviews_crawler/android_app_reviews.xlsx", index = False) 




### EXTRAGE STATISTICILE PER APLICATIE
app_infos = []

for ap in lista_android["app_name"]:
 info = app(
 ap, 
 lang='ro', 
 country='ro'
 )
 del info['comments']
 app_infos.append(info)
 print(app_infos)


info_aps=pd.DataFrame.from_dict(app_infos)

#info_aps['updated']=(((info_aps['updated'].astype(int))/60)/60)/24+25569.00
'''
info_aps=info_aps.drop(columns=['descriptionHTML','summary', 'summaryHTML', 'saleTime', 'originalPrice','saleText', 'offersIAP','androidVersionText','developer','developerId','developerEmail','developerWebsite', 'privacyPolicy','developerInternalID','icon','headerImage','screenshots','video','videoImage', 'contentRatingDescription', 'adSupported', 'containsAds', 'version', 'recentChanges','recentChangesHTML','editorsChoice',
'inAppProductPrice', 'moreByDeveloper','description'])
'''
info_aps['cules la']= datetime.datetime.now()



info_aps.to_excel("C:/Users/antfiera/Documents/GitHub/google-play_reviews_crawler/android_app_stats.xlsx", index = False) 
print(info_aps)
