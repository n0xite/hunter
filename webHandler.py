from linkView import viewLink
import time
import pickle
from bs4 import BeautifulSoup
from selenium import webdriver
from random import randint
from webdriver_manager.chrome import ChromeDriverManager
from cfgHandler import cfgInit


headless = False
viewport = [414, 896]


cfgObj = cfgInit('config.ini')

delayMax = int(cfgObj[1])

def WebInit():
        #query_ln = '"' + clean_name + '" '+ 'site:"linkedin.com"'
    #query_tw = '"' + clean_name + '" ' +   'site:"twitter.com"'
    #query_yt = '"' + clean_name + '" ' + 'site:"youtube.com"'

    #proxy = "socks5://192.168.1.199:9050"
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument('log-level=3')
    #chrome_options.add_argument('--proxy-server='+proxy)
    # Adding argument to disable the AutomationControlled flag 
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") 
    
    # Exclude the collection of enable-automation switches 
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    chrome_options.add_argument("start-maximized")
    # Turn-off userAutomationExtension 
    chrome_options.add_experimental_option("useAutomationExtension", False) 
    chrome_options.headless = headless
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
    driver.set_window_size(viewport[0], viewport[1])



    #driver.find_element_by_xpath('//*[@id="L2AGLb"]/div').click()

    driver.get("http://www.google.com/search?q=test")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    time.sleep(randint(1, delayMax))
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(1)
    return driver



                

def Search(queries, driver):

    for q in queries:
    # Query to obtain links
        print('SEARCHING FOR: ' + q)
        print('----------------------------------------------------------')
        time_start = time.time()
        query = str(q)
        links = [] # Initiate empty list to capture final results
        # Specify number of pages on google search, each page contains 10 #links

        time.sleep(0.4)

        url = "http://www.google.com/search?q=" + query + "&start=0"
        print('URL: ' + url)
        print('----------------------------------------------------------')
        
    
        time.sleep(0.6)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # soup = BeautifulSoup(r.text, 'html.parser')
            
        search = soup.find_all('div', class_="yuRUbf")
        for h in search:
            links.append(h.a.get('href'))
        viewLink(links)
        #print(links)
        for l in links:
            print(l + '\n')
        time_end = time.time()
        print('Time elapsed: ' + str(time_end - time_start))
        print('----------------------------------------------------------')
        time.sleep(randint(1, delayMax))
    driver.close()
    driver.quit()
