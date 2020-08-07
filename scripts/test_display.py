import os, sys
sys.path.append(os.getcwd())
from time import sleep
from base.base_driver import init_driver
from page.page_display import PageDisplay


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display = PageDisplay(self.driver)

    def test_search(self):
        # 点击显示
        self.display.page_click_show()
        sleep(3)
        # 点击放大镜
        self.display.page_click_search_btn()
        sleep(3)
        # 输入文件
        self.display.page_input_value('hello')
        sleep(3)
        # 点击返回
        self.display.page_back()

    def teardown(self):
        self.driver.quit()