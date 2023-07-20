from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from pages.base_page import BasePage

from utils.settings import DEFAULT_LOCATOR_TYPE



class PlayersDashboardPage(BasePage):
    menu_player_button_xpath = "//ul[1]/div[@role='button'][2]"
    players_file_download_button_xpath = "//div[1]//div[2]/button"

    def players_page_menu_click_on_players_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=PlayersDashboardPage.menu_player_button_xpath)
        return self.click_on_the_element(self.menu_player_button_xpath)

    def players_dashboard_download_click_on_download_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=PlayersDashboardPage.players_file_download_button_xpath)
        return self.click_on_the_element(self.players_file_download_button_xpath)

    def path_to_players_file_download(self):
        players_file = PlayersDashboardPage(self.driver)
        LoginPage.user_log_in(self)
        players_file.players_page_menu_click_on_players_button()
        # players_file.players_dashboard_download_click_on_download_button()
