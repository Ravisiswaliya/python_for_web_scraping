from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

def proxy(PROXY_HOST,PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("network.proxy.type", 1)

    fp.set_preference("network.proxy.http", PROXY_HOST)
    fp.set_preference("network.proxy.http_port", int(PROXY_PORT))

    #fp.set_preference("network.proxy.ssl", PROXY_HOST)
    #fp.set_preference("network.proxy.ssl_port", int(PROXY_PORT))

    fp.set_preference("network.proxy.ftp", PROXY_HOST)
    fp.set_preference("network.proxy.ftp_port", int(PROXY_PORT))

    fp.set_preference("network.proxy.socks", PROXY_HOST)
    fp.set_preference("network.proxy.socks_port", int(PROXY_PORT))
    fp.update_preferences()
    return webdriver.Firefox(firefox_profile=fp)

driver = proxy("85.95.33.249", 8080)

driver.set_page_load_timeout(60)
driver.get('https://www.paddypower.com/football/fifa-world-cup-2018?tab=outrights')
sleep(20)

res = driver.execute_script('return document.documentElement.outerHTML')
soup = BeautifulSoup(res, 'lxml')


bet = soup.find_all('div', {'class':'outright-item'})

for p in bet:
    try:
        team = b.find('p',{'class':'outright-item__runner-name'})
        score = b.find('div',{'class':'grid__cell-3-12'})
        print(team,score)
    except:
        pass



