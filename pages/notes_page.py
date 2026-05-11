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

    view_btn = (By.XPATH, "(//a[@data-testid='note-view'])[1]")

    delete_btn = (By.XPATH, "(//button[@data-testid='note-delete'])[1]")

    edit_btn = (By.XPATH, "(//button[@data-testid='note-edit'])[1]")

    update_save_btn = (By.XPATH, "//button[contains(text(),'Save')]")

    complete_checkbox_direct = (
        By.XPATH,
        "(//input[@data-testid='toggle-note-switch'])[1]",
    )

    checkbox_within_card = (By.XPATH, "//input[@data-testid='note-completed']")

    title_required_error = (By.XPATH, "//div[contains(text(),'Title is required')]")

    success_message = (By.CLASS_NAME, "Toastify__toast-body")

    def __init__(self, driver):
        super().__init__(driver)

    def click_edit(self):
        self.click(self.edit_btn)

    def update_note(self, title, description):
        self.send_keys(self.title_input, title)

        self.send_keys(self.desc_input, description)

        self.click(self.update_save_btn)

    def delete_note(self):
        self.click(self.delete_btn)

    def complete_note_within_card(self):
        self.click(self.checkbox_within_card)

    def update_note_with_checkbox(self):
        self.click(self.update_save_btn)

    def click_view(self):
        self.click(self.view_btn)

    def get_success_message(self):
        return self.get_text(self.success_message)

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
