from selenium import webdriver
from selenium.webdriver.common.by import By
from tabulate import tabulate
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3848522265&keywords=2024%20software%20intern&origin=SWITCH_SEARCH_VERTICAL')
driver.implicitly_wait(5)

names = driver.find_elements(by=By.CLASS_NAME, value='base-search-card__title')
locations = driver.find_elements(by=By.CLASS_NAME, value='job-search-card__location')
companies = driver.find_elements(by=By.CLASS_NAME, value='base-search-card__subtitle')

data = []
for i in range(10):
    name = names[i].text
    location = locations[i].text
    company = companies[i].text
    data.append([str(i+1), name, location, company])

driver.quit()

headerNames = ['', 'Job Title', 'Location', 'Company']
table = tabulate(data, headers=headerNames, tablefmt="grid")
print(table)