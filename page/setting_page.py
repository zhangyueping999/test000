import page
from base.base_aciton import BaseAciton

#负责设置页面相关逻辑
class SettingPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)
    #退出当前账号
    def logout_account(self):
        self.swip_screen(1)
        self.click_element(page.setting_center_login_out_btn)
        self.click_element(page.setting_center_login_dialog_confirm_btn)


