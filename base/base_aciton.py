import time
from selenium.webdriver.common.by import By


class BaseAciton:
    #当类初始化的时候这个方法就执行
    def __init__(self,driver):
        self.driver = driver

    #把一些常见的操作定义出来 (点击 输入内容)
    def click_element(self, loc):
        #到底点击哪个元素 是不是的先找到这个元素才能点击
        self.find_element(loc).click()
#向输入框输入内容
    def send_element_content(self,loc,content):
        self.find_element(loc).clear()

        self.find_element(loc).send_keys(content)
    def find_element(self, loc):
        #在找元素之前 等待
        self.driver.implicitly_wait(10)
        return self.driver.find_element(loc[0], loc[1])

#设置滑动
    def swip_screen(self,tag):
        time.sleep(1)
        screen_size = self.driver.get_window_size()
        width = screen_size.get("width")
        height = screen_size.get("height")
        if tag == 1:#向上滑
            self.driver.swipe(width * 0.5,height * 0.8,width * 0.5, height * 0.3,1000 )
        if tag == 2:#向下滑
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 1000)
        if tag == 3:#向左滑
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 1000)
        if tag == 4:
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, 1000)

    def get_toast_message(self, message):
        toast_xpath = "//*[contains(@text,'{}')]".format(message)
        toast_message = self.find_element((By.XPATH, toast_xpath)).text
        return toast_message

    def get_screen(self):
        # 截图名称
        png_name = "./screen/{}.png".format(int(time.time()))
        self.driver.get_screenshot_as_file(png_name)

        # with open("abc.png", "rb") as f:
        # allure.attach("截图名字", f.read(), allure.attach_type.PNG)

