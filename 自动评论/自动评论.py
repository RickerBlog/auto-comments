# 给小码王全社区用户发同一条评论
# 需要安装selenium库
# 必须以电脑所有的分辨率运行程序
# 引入必要库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
#变量设置
# 下面的应该都看得懂
userID = 0
phone = input("输入小码王登录手机号:")
password = input("输入小码王登录密码:")
comment = input("评论内容:")
# 检测目录
current_directory = os.path.dirname(os.path.abspath("__file__"))
# 设置webDriver
# 需要更改webDriver，可以修改在该目录下的webDriver.cfg，将文件内容替换成准备好的webDriver文件名（确保webDriver在该文件目录下的drivers文件夹）
webDriver = open(current_directory + "\\webDriver.cfg").read()
# 启动chomediver
driver = webdriver.Chrome(current_directory + "\\drivers\\" + webDriver)

# 定义函数
# 单击元素
def clickElement(Xpath):
    while len(driver.find_elements(By.XPATH,Xpath)) < 1:
        print(len(driver.find_elements(By.XPATH,Xpath)))
        print(driver.find_elements(By.XPATH,Xpath))
        time.sleep(1)
    driver.find_element(By.XPATH,Xpath).click()
# 向元素发送文字/键盘
def send_keys_to_Element(Xpath, keys):
    while len(driver.find_elements(By.XPATH,Xpath)) < 1:
        pass
    driver.find_element(By.XPATH,Xpath).send_keys(keys)

# 自动操作网页
# 打开登录界面
driver.get("https://world.xiaomawang.com/w/index")
clickElement("/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div/a[1]")
send_keys_to_Element("/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/div/form/div[1]/div[1]/div/div/span/input", phone)
send_keys_to_Element("/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/div/form/div[1]/div[2]/div/div/span/span/input", password)
clickElement("/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/div/form/div[2]/label/span[1]")
clickElement("/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/div/form/button")
time.sleep(5)
# 自动给全社区用户的主页发评论
while True:
    userID = userID + 1
    driver.get("https://world.xiaomawang.com/w/person/project/all/" + str(userID))
    send_keys_to_Element("/html/body/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/textarea", comment)
    clickElement("/html/body/div/div[2]/div[4]/div[2]/div[2]/div[2]/div[2]/button")
