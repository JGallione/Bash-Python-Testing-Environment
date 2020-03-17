import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


s_earch = input("Google Search:") 
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver2 = webdriver.Chrome('/Newest_build_folder/TestingEnv/lib/python3.7/site-packages/selenium')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
#driver2.get('http://www.Stackoverflow.com/')

time.sleep(1) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys(s_earch)
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()