import page
from base.base_aciton import BaseAciton

#首页
class HomePage( BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)
    def click_my_button(self):
        self.click_element(page.home_my_button)
