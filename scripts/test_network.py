import os, sys
sys.path.append(os.getcwd())
from time import sleep
from base.base_driver import init_driver
from page.page_network import PageNetwork


class TestNetword:

    def setup(self):
        self.driver = init_driver()
        self.network = PageNetwork(self.driver)

    def test_network_2g(self):
        self.network.page_click_more()
        sleep(2)
        self.network.page_click_move_network()
        sleep(2)
        self.network.page_click_first_network()
        sleep(2)
        self.network.page_click_2g()

    def test_network_3g(self):
        self.network.page_click_more()
        sleep(2)
        self.network.page_click_move_network()
        sleep(2)
        self.network.page_click_first_network()
        sleep(2)
        self.network.page_click_3g()

    def teardown(self):
        self.driver.quit()