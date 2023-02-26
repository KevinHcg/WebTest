# -*- coding = UTF-8 -*-
# Autohr   : 黄朝岗
# @公众号   : iTest岗
# File     : login_page.py
# Describe : 页面定位元素及操作
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class LoginPage:

    def __init__(self,driver):
        self.driver=driver

    def login(self,name,pwd):
        '''登录元素定位和业务操作'''
        # 输入账号
        # 隐式等待，页面加载完成才执行下一步
        # driver.implicitly_wait(10)
        # 显式等待
        WebDriverWait(self.driver, 10, 0.6).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, '//*[@id="loginBox"]/form/div[1]/div/div/div[2]/div/input')))
        self.driver.find_element(By.XPATH,'//*[@id="loginBox"]/form/div[1]/div/div/div[2]/div/input').send_keys(name)
        # 输入密码
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="loginBox"]/form/div[2]/div/div/div[2]/div/input')))
        self.driver.find_element(By.XPATH,'//*[@id="loginBox"]/form/div[2]/div/div/div[2]/div/input').send_keys(pwd)
        # 点击登录
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="loginBox"]/form/div[3]/div/button')))
        self.driver.find_element(By.XPATH,
                                 '//*[@id="loginBox"]/form/div[3]/div/button').click()
        # 强制等待
        time.sleep(1)
    def chick_name_pwd(self):
        '''账号密码异常的弹窗'''
        time.sleep(0.5)
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/p').text

    def login_cg(self):
        '''登录成功返回标题'''
        time.sleep(0.5)
        return self.driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/section/section/header/div/div[1]/div/span/b').text


if __name__ == '__main__':
    # 创建浏览器对象,Chrome驱动程序的新实例
    driver = webdriver.Chrome()
    driver.get('http://43.143.75.118:30993/')
    LoginPage(driver).login('test','test')