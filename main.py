from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from csv import writer

url = "http://164.100.196.30/Content/html/abpas6.4.2/Homepage.html#/citizensearch"
path = "C:\Program Files (x86)\chromedriver.exe"
import time
from selenium.webdriver.support.ui import Select


l1 = [
"IND/IND/IND/0152/3372/2022",
"IND/IND/IND/0152/3371/2022",
"IND/IND/IND/0152/3370/2022",
"IND/IND/IND/0152/3369/2022",
"IND/IND/IND/0152/3368/2022",
"IND/IND/IND/0152/3367/2022",
"IND/IND/IND/0152/3366/2022",
"IND/IND/IND/0152/3365/2022",
]

driver = webdriver.Chrome(path)
driver.get(url)
driver.maximize_window()
time.sleep(5)

select = Select(driver.find_element(By.TAG_NAME,"select"))
# print ([o.text for o in select.options]) # these are string-s
select.select_by_visible_text("File Number")

with open("user_data.csv", "w+", newline="", encoding="utf8") as f:
      thewriter = writer(f)
      header = ['File_Name', 'Mobile_no', 'Email', 'Assessment_No']
      thewriter.writerow(header)
      for file in l1:
            data = []
            data.append(file)
            try:
                  driver.find_element(By.TAG_NAME, 'input').send_keys(file)
                  driver.find_element(By.ID, 'CitizenSerchDetailsId').click()
                  time.sleep(7)
                  b = driver.find_element(By.CSS_SELECTOR, 'span[class="ng-binding ng-scope"][ng-click="grid.appScope.showCase(row.entity.PlanRequestId)"]').click()
                  time.sleep(7)
            
                  try:
                        mob_no = driver.find_element(By.XPATH, "//table[@class= 'table table-condensed']/tbody/tr[4]/td[4]").text
                        print("Mob.no", "-", mob_no)
                        
                  except Exception as message:
                        print(message)
                        mob_no = None
                  data.append(mob_no)
                  
                  try:
                        email = driver.find_element(By.XPATH, "//table[@class= 'table table-condensed']/tbody/tr[5]/td[4]").text
                        print("Email", "-",email)
                  except Exception as message:
                        print(message)
                        email = None
                  data.append(email)
                  try:
                        assessment_no = driver.find_element(By.XPATH, "//table[@class= 'table table-condensed']/tbody/tr[10]/td[2]").text
                        print("Assessment_no", "-",assessment_no)
                        
                  except Exception as message:
                        print(message)
                        assessment_no = None
                  data.append(assessment_no)
                  driver.find_element(By.CSS_SELECTOR, 'button[class="md-warn md-raised close md-button md-ink-ripple"]').click()
                  time.sleep(2)
                  driver.find_element(By.TAG_NAME, 'input').clear()
                  time.sleep(2)
            except Exception as message:
                  print(message)
            print(data)
            thewriter.writerow(data)
