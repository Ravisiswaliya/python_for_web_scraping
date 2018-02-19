#importing library
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import threading

#creating a function

def site1():
    #threading.Timer(5.0,site1).start() #run script in every 5 sec    #this line will run this program in every 5 seconds
    url = "http://sports.williamhill.com/bet/en-gb/betting/e/12085242/World%20Cup%202018%20-%20Outright.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    }

    r = requests.get(url=url, headers=headers)  #request to get url
    #getting text only data
    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup)                         #just for checking

    #selecting class to extract data
    select = soup.findAll(name='div', attrs={'class': 'eventselection'})   #selecting team name
    select2 = soup.findAll(name='div', attrs={'class': 'eventprice'})      #selecting price

    #creating list
    l2 = []
    l1 = []

    for t, t2 in zip(select, select2):    #iterating over data
        t = t.text                        #getting text only
        t = " ".join(t.split())
        t2 = t2.text
        t2 = " ".join(t2.split())
        l2.append(t)                      #adding data to list
        l1.append(t2)

    #script for mobile.bet365.com
    driver = webdriver.Firefox()          #selecting firefox driver
    driver.get('https://mobile.bet365.com/?apptype=&appversion=&cb=1518802538#type=Coupon;key=1-172-1-26326924-2-0-0-0-2-0-0-4063-0-0-1-0-0-0-0-0-75-0-0;ip=0;lng=1;anim=1')
    sleep(10)                             #using time.sleep function

    res = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(res, 'lxml')     #reading data using beautifulsoup

    bet = soup.find_all('div', {'class': 'priceColumn'})   #finding class that holding team name and price

    l3 = []                               #creating a list
    for b in bet:
        try:
            team_and_score = b.find('span', {'class': 'opp'}).text  #finding tag and getting text content
            l3.append(team_and_score)     #storing data into list
            l3.sort()                     #sorting list
        except:
            pass
    # saving data into a dictionary
    uu = {'team': l2,
          'sports.williamhill.com':l1,
          'mobile.bet365.com': l3,
            }
    #creating dataframe from extracted data
    df = pd.DataFrame(uu, columns=['team', 'sports.williamhill.com', 'mobile.bet365.com'])
    df = df.set_index('team')             #setting team as index
    #df.to_csv('output.csv')              #(Optional) if you want save output in csv file
    print(df)                             #reading dataframe


#calling function
site1()

