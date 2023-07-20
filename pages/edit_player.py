from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class EditPlayer(BasePage):

    edit_player_menu_player_name_xpath = "//ul[2]/div[1]/div[2]/span"
    edit_player_upper_title_span_text_xpath = "//div[2]/*/div[1]/*/span"
    edit_player_player_added_popup_container = "//*[@id='__next']/div[2]/div"

    def edit_player_url_for_check(self):
        driver = self.driver
        current_url = driver.current_url
        current_url_slice = current_url.split("/")[5]
        print(current_url_slice)
        return current_url_slice

    def wait_for_alert_turnaround(self, locator_type=By.XPATH):
        """Waiting until alert from current XPath disappears"""
        wait = WebDriverWait(self.driver, timeout=60)
        element_present = wait.until_not(EC.visibility_of_element_located((locator_type, EditPlayer.edit_player_player_added_popup_container)))
