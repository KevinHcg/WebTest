# -*- coding = UTF-8 -*-
# Autohr   : 黄朝岗
# @公众号   : iTest岗
# File     : add_memo_page.py
# Describe : 页面定位元素及操作

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class AddMemo:
    def __init__(self,driver):
        self.driver=driver
    def add_memo(self,name,option,des):
        '''添加备忘录元素定位和操作'''
        # 点击添加
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="app"]/div/section/section/main/form/div/div[2]/div/button[3]/span')))
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/section/main/form/div/div[2]/div/button[3]/span').click()
        # 输入标题
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="app"]/div/section/section/main/div[1]/div/div[2]/form/div[1]/div/div[1]/input')))
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/section/main/div[1]/div/div[2]/form/div[1]/div/div[1]/input').send_keys(name)
        # 点击分类
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@id="app"]/div/section/section/main/div[1]/div/div[2]/form/div[2]/div/div/div/input')))
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/section/section/main/div[1]/div/div[2]/form/div[2]/div/div/div/input').click()
        # 选择类类型
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/'+option)))
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/'+option).click()
        # 输入内容
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@id="app"]/div/section/section/main/div[1]/div/div[2]/form/div[3]/div/div/textarea')))
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/section/section/main/div[1]/div/div[2]/form/div[3]/div/div/textarea').send_keys(des)
        # 点击确定
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="app"]/div/section/section/main/div[1]/div/div[3]/div/button[2]/span')))
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/section/main/div[1]/div/div[3]/div/button[2]/span').click()
        time.sleep(1)

    def check_name(self):
        '''校验标题'''
        return self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/section/main/div[1]/div/div[2]/form/div[1]/div/div[2]').text
    def check_des(self):
        '''校验备注'''
        time.sleep(0.5)
        return self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/section/main/div[1]/div/div[2]/form/div[3]/div/div[2]').text


    def check_t(self):
        time.sleep(1)
        return self.driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div/section/section/main/div[2]/div[3]/table/tbody/tr[1]/td[3]/div').text
    def del_memo(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@id="app"]/div[2]/section/section/main/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/div/button[2]')))
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[2]/section/section/main/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/div/button[2]').click()
        time.sleep(1)


if __name__ == '__main__':
    AddMemo.add_memo('a','b','c','')