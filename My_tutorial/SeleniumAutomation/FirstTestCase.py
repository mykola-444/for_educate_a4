from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

#from selenium import webdriver
#browser = webdriver.Chrome
#browser = webdriver.Chrome('C:\\Progs\\Python37\\Scripts\\chromedriver')
#browser.get('http://www.selenium.dev')
#browser.find_element_by_link_text('Downloads').click()

driver = Chrome()
driver.get("https://www.thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588")

driver.maximize_window()
# enter Data
driver.find_element_by_name("jform[name]").send_keys("HelloWorld")
driver.find_element_by_xpath("//input[@name='jform[email1]']").send_keys("asd@gf.com")
driver.find_element_by_name("jform[name]").clear()
driver.find_element_by_name("jform[name]").send_keys("NOOOOOOHelloWorld" + Keys.ENTER)

# Radio dutton
# driver.find_element_by_xpath("//input[@value='home']").click()

# Checkbox
# driver.find_element_by_name("terms").click()

# work on button
# driver.find_element_by_xpath("//input[@type='submit']").click()

# click on link
# driver.find_element_by_link_text("Quick Demo").click()

# driver.close()
