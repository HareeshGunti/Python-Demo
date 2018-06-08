from selenium import webdriver
#browser = webdriver.Firefox()
#browser = webdriver.Chrome()

browser = webdriver.Firefox(executable_path="firefox.exe")

browser.get("http://dcvision-confluence.amerisourcebergen.com/display/MHE/MHE+Technical+Support+Home")

#elem = browser.find_element_by_css_selector(".entry-content>ol:nth-child(15) > li:nth-child(1) > a:nth-child(1)")
#elem.text
#elem.click()
