try:
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from time import sleep
    import pickle
    from subprocess import run
    import configparser
    import webbrowser
    from random import randint
except:
    run("pip install -r requirements.txt")





clean_name = ""
queries = []


def Start():
    name = input("Full name: ")
    return name

def cfgInit(cfgPath):
    config = configparser.ConfigParser()
    config.read(cfgPath)
    queryArray = config.get('QUERIES', 'links')
    queryArray_clean = queryArray.split(",")
    delayMax = config.get('SETTINGS', 'DefaultDelayMax')
    defaultDecision = config.get('SETTINGS', 'DefaultDecision')
    return queryArray_clean, delayMax, defaultDecision


def queryResolver(name):
    clean_name = " ".join(name.split())
    cArray = cfgInit('config.ini')[0]
    for c in cArray:
        mQuery = '"' + clean_name + '" ' + c.strip(" ")
        queries.append(mQuery)
    return queries

delayMax = int(cfgInit('config.ini')[1])
defaultDecision = str(cfgInit('config.ini')[2])
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
    chrome_options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 



    #driver.find_element_by_xpath('//*[@id="L2AGLb"]/div').click()

    driver.get("http://www.google.com/search?q=test")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    sleep(randint(1, delayMax))
    for cookie in cookies:
        driver.add_cookie(cookie)
    sleep(1)
    return driver


def viewLink(links):
    if links:
        if len(links) > 5:
            if defaultDecision == "None":
                d = input("There are more than 5 links to be displayed, do you want to open them in a webbrowser? ")
            elif defaultDecision == "Yes" or defaultDecision == "No":
                d = defaultDecision
        
            if d == "Yes" or d == "Y" or d == "y":
                for l in links:
                    webbrowser.open(l)
            elif d == "No" or d == "N" or d == "n":
                print("Displaying links to the console: ")

              
                

def Search(queries, driver):

    for q in queries:
    # Query to obtain links
        print('SEARCHING FOR: ' + q)
        print('----------------------------------------------------------')
        query = str(q)
        links = [] # Initiate empty list to capture final results
        # Specify number of pages on google search, each page contains 10 #links

        sleep(0.4)

        url = "http://www.google.com/search?q=" + query + "&start=0"
        print('URL: ' + url)
        print('----------------------------------------------------------')
        
    
        sleep(0.6)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # soup = BeautifulSoup(r.text, 'html.parser')
            
        search = soup.find_all('div', class_="yuRUbf")
        for h in search:
            links.append(h.a.get('href'))
        viewLink(links)
        print(links)
        print('----------------------------------------------------------')
        sleep(randint(1, delayMax))
    driver.close()
    driver.quit()

def Main():
    queryResolver(Start())
    Search(queries, WebInit())
    d = input("Do you want to look for someone else?: ")
    if d == "Yes" or "Y" or "y":
        Main()
    elif d == "No" or "N" or "n":
        exit

Main()