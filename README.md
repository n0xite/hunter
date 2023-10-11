# hunter
Hunter is a google search automator, especially useful with google dorks while looking for different people. It's still in very early stages of development but works pretty well.

# How to use
To use hunter, input your queries (dorks) into mod variable (twitter, linkedin, instagram and youtube are default). 
Then run hunter.py and input your search target full name.
Hunter will now print out results for your search in a list.

# Config
mod - Queries to be searched
DefaultDelayMax - Max delay in randomized default delay
DefaultDecision - Default decision for automatic link preview. (Empty field for manual choice during execution)
LinkMax - Amount of links to be opened in browser (if user agrees)

# Required modules
- time
- pickle
- BeautifulSoup
- selenium 
- random 
- ChromeDriverManager
- configparser
