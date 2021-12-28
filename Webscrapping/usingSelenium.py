from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.maximize_window()

url="https://www.amazon.in/HP-PC-21-5-Inch-Desktop-22-df0202in/dp/B09HRXTGGJ/ref=sr_1_1?m=A14CZOWI0VEHLG&pd_rd_r=2cc448f4-08fe-46ca-9009-f36d3486cd65&pd_rd_w=BEfha&pd_rd_wg=GF7KU&pf_rd_p=f690369a-7bb4-48bb-9349-f68a447ef06d&pf_rd_r=E4NN2HGX6ZHEBD2MGG2T&qid=1640089354&refinements=p_6%3AA14CZOWI0VEHLG&smid=A14CZOWI0VEHLG&sr=8-1"
home_url="https://www.amazon.in"
driver.get(home_url)

search_box=driver.find_element(By.NAME,'field-keywords')
search_box.send_keys('Asus Laptop',Keys.ENTER)
print(driver.title)
rows=driver.find_elements(By.CLASS_NAME,'a-size-mini')

for items in rows:
    print(items.text)
# try:
#     ele=(driver.find_element(By.TAG_NAME,'h1'))
#     print('text',ele.text)
# except Exception as e:
#     print(e)
# driver.close()