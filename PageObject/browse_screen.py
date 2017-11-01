from PageObject.page import Page

class Browse(Page):
    def __init__(self, app):
        super().__init__(app)

    def wait_page_to_load(self):
        self.wait_element_to_load('xpath', self.app.locators['header_browse_title'])

    def title(self):
        self.find_element('xpath', self.app.locators['header_browse_title'])

    def get_title_text(self):
        self.get_element_text(self.title())