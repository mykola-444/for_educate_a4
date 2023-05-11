from Tools.scripts.findlinksto import visit
from selenium.webdriver import Chrome
#from core.tool import ss, s
from selenium.webdriver.common.keys import Keys

driver = Chrome()
driver.get("http://todomvc.com/examples/knockoutjs/")

#driver.maximize_window()
# enter Data

driver.find_element_by_class_name("new-todo").send_keys("HelloWorld" + Keys.ENTER)
#driver.find_element_by_xpath("//input[@name='jform[email1]']").send_keys("asd@gf.com")
#print(driver.find_element_by_class_name("todo-list>li").find_elements_by_name("HelloWorld"))
driver.find_element_by_class_name("todo-list>li").find_elements_by_name("HelloWorld").double_click()