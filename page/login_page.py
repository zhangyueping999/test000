import page
from base.base_aciton import BaseAciton

#登录
class LoginPage( BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)
    def login_in(self,name,pwd):
        self.send_element_content(page.login_username_id,name)
        self.send_element_content(page.login_pwd_id,pwd)
        self.click_element(page.login_login_in_btn)
    def close_login_page(self):
        self.click_element(page.login_login_out_btn)