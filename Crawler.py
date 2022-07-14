from selenium import webdriver
import json
import pymysql
import time
import os.path

#report count
file_count = 18              

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(0.5)
driver.maximize_window()

driver.get("http://127.0.0.1:8000/")
time.sleep(3)
s = driver.find_element_by_xpath("//input[@type='file']")
s.send_keys("your_file_path")

time.sleep(3)
driver.find_element_by_xpath('//*[@id="filetree"]/ul/li/div/label/span').click()
driver.find_element_by_xpath('//*[@id="start-analysis"]').click()

path = '/home/ubuntu/.cuckoo/storage/analyses/' + str(file_count) + '/reports/report.json'

print('Waiting for reporting...')
while True :
  if os.path.isfile(path):
    print("report found")
    break
#SQL module
with open('/home/ubuntu/.cuckoo/storage/analyses/latest/reports/report.json') as f:
  data = json.load(f)
  #SQL QUERY
  connection = pymysql.connect(host='your_ip', user='your_id', password='your_pw', db='your_db', charset='utf8')
  cursor = connection.cursor()
  sql = "INSERT INTO cuckoo VALUES ('" + data + "')"
  cursor.execute(sql)
  connection.commit()
  print(data)
  print('\n\n\nSuccess to insert JSON report in Database')
