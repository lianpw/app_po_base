from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PageDisplay(BaseAction):

    # 显示按钮
    display_show_btn = By.XPATH, "//*[contains(@text, '显示')]"
    # 搜索按钮
    display_search_btn = By.ID, 'com.android.settings:id/search'
    # 搜索输入框
    display_search_input = By.ID, 'android:id/search_src_text'
    # 后退按钮
    display_back = By.CLASS_NAME, 'android.widget.ImageButton'

    def page_click_show(self):
        # self.find_element(self.display_show_btn).click()
        self.base_click(self.display_show_btn)

    def page_click_search_btn(self):
        # self.find_element(self.display_search_btn).click()
        self.base_click(self.display_search_btn)

    def page_input_value(self, value):
        # self.find_element(self.display_search_input).send_keys(value)
        self.base_input(self.display_search_input, value)

    def page_back(self):
        # self.find_element(self.display_back).click()
        self.base_click(self.display_back)