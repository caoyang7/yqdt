from selenium import webdriver

# 设置你自己的chormedriver存放路径
driver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.baidu.com")

print(driver.page_source)
