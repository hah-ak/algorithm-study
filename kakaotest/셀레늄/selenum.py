from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "http://www.danranmembers.or.kr/edunew2/newedu_detail.asp?idx=3&gotopage=1&edu_idx=2102241&order_num=EDU202009162028480064000&epart=%B1%E2%C1%B8&title=&keyword=&category=1"
driver = webdriver.Chrome(executable_path= r"C:\Users\AI\Desktop\chromedriver")
driver.get(url)