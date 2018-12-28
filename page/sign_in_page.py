import page
from base.base_aciton import BaseAciton
#注册

class SignInPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)
    def click_exit_accout(self):
        self.click_element(page.sign_in_exit_account_id)
