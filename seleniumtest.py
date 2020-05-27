#搜索虎牙直播
#第一步：导入selenium
from selenium import webdriver
import time
# 第二步：打开谷歌浏览器
driver = webdriver.Chrome(executable_path="chromedriver.exe")
# 第三步：打开百度
driver.get("https://www.baidu.com/")
# 第四步：输入搜索关键字
element1 = driver.find_element_by_id("kw")
element1.send_keys("虎牙")
# 第五步： 点击搜索按钮
element2 = driver.find_element_by_id("su")
element2.click()
time.sleep(3)
title = driver.title
# print(title)
if title =="虎牙_百度搜索":
    print("测试成功！")
else:
    print("测试失败！")
#20秒后关闭
time.sleep(3)
# 最后一步: 结束测试
driver.quit()