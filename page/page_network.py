from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PageNetwork(BaseAction):

    # 更多按钮
    network_more_btn = By.XPATH, "//*[contains(@text, '更多')]"
    # 移动网络按钮
    network_move_btn = By.XPATH, "//*[contains(@text, '移动网络')]"
    # 首选网络类型按钮
    network_firstcheck_btn = By.XPATH, "//*[contains(@text, '首选网络类型')]"
    # 2g
    network_2g = By.XPATH, "//*[contains(@text, '2G')]"
    # 3g
    network_3g = By.XPATH, "//*[contains(@text, '3G')]"

    def page_click_more(self):
        # self.find_element(self.network_more_btn).click()
        self.base_click(self.network_more_btn)

    def page_click_move_network(self):
        # self.find_element(self.network_move_btn).click()
        self.base_click(self.network_move_btn)

    def page_click_first_network(self):
        # self.find_element(self.network_firstcheck_btn).click()
        self.base_click(self.network_firstcheck_btn)

    def page_click_2g(self):
        # self.find_element(self.network_2g).click()
        self.base_click(self.network_2g)

    def page_click_3g(self):
        # self.find_element(self.network_3g).click()
        self.base_click(self.network_3g)
