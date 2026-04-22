from pages.dropdown_page import DropdownPage

class TestDropdown:

    def test_select_option1(self, driver):
        page = DropdownPage(driver)
        page.open()
        page.select_option("Option 1")
        assert page.get_selected_option() == "Option 1"

    def test_select_option2(self, driver):
        page = DropdownPage(driver)
        page.open()
        page.select_option("Option 2")
        assert page.get_selected_option() == "Option 2"