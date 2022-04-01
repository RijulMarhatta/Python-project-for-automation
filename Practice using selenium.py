For automation in selenium
From Seleniumbase import Basecase
Class Home Test(Basecase):


def test_home_page(self):
    # open home page
    self.open_page()

    # assert page title
    self.assert_title("Practice E-Commerce Site – Automation Bro")

    # assert logo
    self.assert_element(HomePage.logo_icon)

    # click on the get started button and assert the url
    self.click(HomePage.get_started_btn)
    get_started_url = self.get_current_url()
    self.assert_equal(
        get_started_url, "https://practice.automationbro.com/#get-started")
    self.assert_true("get-started" in get_started_url)

    # get the text of the header and assert the value
    self.assert_text("Think different. Make different.", HomePage.heading_text)

    # Exercise: scroll to bottom and assert the copyright text
    self.scroll_to_bottom()
    self.assert_text("Copyright © 2020 Automation Bro",
                     HomePage.copyright_text)