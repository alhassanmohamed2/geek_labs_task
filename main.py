from bs4 import BeautifulSoup
import re


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




url = 'https://twitter.com/ChartingProdigy'

service=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)



browser.get(url)

html_content = browser.page_source




soup = BeautifulSoup( html_content,'html.parser')



wait = WebDriverWait(browser, 10)  
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="tweetText"]')))

js_code = ""
with open('main.js','r') as js_code:
    js_code = js_code.read()

text_content = browser.execute_script(js_code)


print(text_content)





browser.quit()




# links = soup.find_all('a')

# specific_class_elements = soup.find_all(class_='specific-class')

# element_with_id = soup.find(id='id__gqzdksgviyp')
# # for i in element_with_id:
# #     print(i.text)
# print(len(element_with_id))


# pattern = r'\$[^\d\s][a-zA-Z0-9_]*'



# url = 'https://twitter.com/Mr_Derivatives'



# print(element_with_id.text)

# print(element_with_id['href'])


# matches = re.findall(pattern, text)

# for match in matches:
#     print(match)