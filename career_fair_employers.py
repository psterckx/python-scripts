# Peter Sterckx, created on 9/14/2019
# Genreates a text file containing all employers that will be at the Clemson Career Fair along with the days they will be there
# Requires chromedriver.exe and specific path to the driver (string chrome_path)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

file = open("employers.txt","a")

chrome_path = r"C:\Users\Peter\Documents\Projects\Active\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = "https://clemson-csm.symplicity.com/events/e218e984457c75cedce368720787687e/employers"
driver.get(url)

for page in range(1,100):

    try:
        employers = WebDriverWait(driver, 10).until(ec.text_to_be_present_in_element((By.XPATH, """//*[@id="companies"]/paging-controls[2]/span/span"""),str(page)))
    except:
        driver.quit()
        file.close()
        print("End of results")
        quit()

    day_list = ['']*3
    days = driver.find_elements_by_xpath("""//*[@id="companies"]/div/ul/li/div[1]/table/tbody/tr[1]/td""")
    employers = driver.find_elements_by_xpath("""//*[@id="companies"]/div/ul/li/div[1]/h2/span""")
    for i,employer in enumerate(employers):
        if "1" in days[i].text:
            day_list[0] = "1"
        else:
            day_list[0] = ""
        if "2" in days[i].text:
            day_list[1] = "2"
        else:
            day_list[1] = ""
        if "3" in days[i].text:
            day_list[2] = "3"
        else:
            day_list[2] = ""

        line = ""
        for day in day_list:
            if day != "":
                line += day + " "

        file.write(employer.text + " - " + line + "\n")

    element = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, """//*[@id="companies"]/paging-controls[2]/span/button[2]""")))
    element.click()

driver.quit()
file.close()
print("End of results")
