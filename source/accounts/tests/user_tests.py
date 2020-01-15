from django.test import TestCase
from selenium.webdriver import Chrome


class LoginTest(TestCase):
    def setUp(self):
        self.driver = Chrome()

    def tearDown(self):
        self.driver.close()

    def test_log_in_as_admin(self):
        self.driver.get('http://127.0.0.1:8000/accounts/login/')
        # self.driver.find_element_by_class_name('login').click()
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_css_selector('button[type="submit"]').click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/'


class LogoutTest(TestCase):
    def setUp(self):
        self.driver = Chrome()

    def tearDown(self):
        self.driver.close()

    def test_logout_as_admin(self):
        self.driver.get('http://localhost:8000')
        self.driver.find_element_by_class_name('login').click()
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_css_selector('button').click()
        self.driver.find_element_by_class_name('logout').click()
        assert self.driver.current_url == 'http://localhost:8000/'

