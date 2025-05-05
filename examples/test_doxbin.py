from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class MyTestClass(BaseCase):
    def test_doxbin(self):
        self.open("https://doxbin.com/")
        self.sleep(2)
        self.uc_gui_click_captcha()
        self.sleep(2)
        self.assert_text("Doxbin")
