from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class NotesPage(BasePage):
    
    # LOCATORS
    add_btn = (By.XPATH, "//button[@data-testid='add-new-note']")

    category_dropdown = (By.ID, "category")

    title_input = (By.ID, "title")

    desc_input = (By.ID, "description")

    create_btn = (By.XPATH, "//button[contains(text(),'Create')]")

    note_titles = (By.XPATH, "//div[@data-testid='note-card-title']")

    title_required_error = (By.XPATH, "//div[contains(text(),'Title is required')]")

    def __init__(self, driver):
        super().__init__(driver)

    # Create Note
    def create_note(self, title, description, category):
        # Open Add Note modal
        self.click(self.add_btn)

        # Fill note details
        self.send_keys(self.title_input, title)
        self.send_keys(self.desc_input, description)

        # Select category
        dropdown = Select(self.driver.find_element(*self.category_dropdown))

        dropdown.select_by_visible_text(category)

        # Click Create button
        self.click(self.create_btn)

        # Wait until note appears in UI
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//div[@data-testid='note-card-title' and contains(text(), '{title}')]",
                )
            )
        )

    # Verify Note Exists
    def is_note_present(self, title):
        self.wait.until(EC.presence_of_all_elements_located(self.note_titles))

        titles = []

        elements = self.driver.find_elements(*self.note_titles)

        for element in elements:
            try:
                text = element.text.strip()

                if text:
                    titles.append(text)

            except:
                continue

        return title in titles


    # Negative Test: Verify Title Required Error
    def is_title_required_error_displayed(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.title_required_error)
            ).is_displayed()

        except:
            return False



    # Get All Note Titles
    def get_all_titles(self):
        self.wait.until(EC.presence_of_all_elements_located(self.note_titles))
        titles = []
        elements = self.driver.find_elements(*self.note_titles)

        for element in elements:
            try:
                text = element.text.strip()
                if text:
                    titles.append(text)
            except:
                continue
        return titles
