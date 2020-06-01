from selenium import webdriver
import unittest


class NewVisitortest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User checks out the homepage
        self.browser.get('http://localhost:8000')

        # Notices the page title and header
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # User is invited to enter a to-do item

        # She types "Buy peacock feathers" into a box

        # She clicks enter, page updates and the page lists the items

        # There is still a box inviting her to add another item

        # She enters "Use peacock feathers to make a fly"

        # Page updates again

        # The site generates a unique URL for her

        # She visits the URL, the to-do list is still there

        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
