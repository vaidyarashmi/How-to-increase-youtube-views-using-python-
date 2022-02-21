from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
number_of_drivers=int(input("Enter the number of drivers::"))
url=input("enter url::")
time_to_refersh=int(input("Enter the refersh rate::"))
drivers=[]
for i in range(number_of_drivers):
    drivers.append(webdriver.Chrome(ChromeDriverManager().install()))
    drivers[i].get(url)

while True:
    time.sleep(time_to_refersh)
    for i in range(number_of_drivers):
        drivers[i].refresh()

drivers.quit()