from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

def install_firefox_proxy(PROXY_HOST,PROXY_PORT):
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

driver = install_firefox_proxy("163.172.27.213", 3128)
driver.set_page_load_timeout(60)
driver.get('https://m.skybet.com/football/world-cup-2018/event/16742642')

sleep(4)

res = driver.execute_script('return document.documentElement.outerHTML')
soup = BeautifulSoup(res, 'lxml')

bet = soup.find_all('div', {'class':'row_11ssjiv'})

for p in bet:
    try:
        team = b.find('div',{'class':'title_1nskdmh'})
        score = b.find('span',{'class':'priceInner_14t1nf5'})
        print(team,score)
    except:
        pass
