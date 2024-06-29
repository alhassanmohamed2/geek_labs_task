from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  
from collections import Counter
import re

pattern = r'\$[^\d\s][a-zA-Z0-9_]*'





twitter_urls = [
    "https://twitter.com/Mr_Derivatives",
    "https://twitter.com/warrior_0719",
    "https://twitter.com/ChartingProdigy",
    "https://twitter.com/allstarcharts",
    "https://twitter.com/yuriymatso",
    "https://twitter.com/TriggerTrades",
    "https://twitter.com/AdamMancini4",
    "https://twitter.com/CordovaTrades",
    "https://twitter.com/Barchart"
]

service=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)




Tweets_set=set()



stock_patt = []
dub_list = []

for url in twitter_urls:

    driver.get(url)
    Tweets = driver.find_elements(By.XPATH,".//div[@data-testid='tweetText']")
    while True:
        for Tweet in Tweets:
            Tweets_set.add(Tweet.text)
            matches = re.findall(pattern, Tweet.text)
            for match in matches:
                stock_patt.append(match)


        driver.execute_script("""window.scrollBy(0, 3000);""")
        sleep(3)
        Tweets = driver.find_elements(By.XPATH,".//div[@data-testid='tweetText']")
        print(f"Tweets is : {len(Tweets_set)}")

        if len(Tweets_set) not in dub_list:
            dub_list.append(len(Tweets_set))
        else:
            break
    dub_list = []
    Tweets = []
    Tweets_set = set()

cont = Counter(stock_patt)
print(cont)
with open('readme.txt', 'w') as f:
    f.write(f'{cont}')

