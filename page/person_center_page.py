from base.base_aciton import BaseAciton
import page
#个人中心

class PersonCenterPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    #点击这个人中心设置按钮
    def click_person_center_setting(self):
        self.click_element(page.person_cernter_setting_btn)
    def is_login_sucess(self):
        try:
            self.find_element(page.person_center_all_order)
            return True
        except:
            return False
