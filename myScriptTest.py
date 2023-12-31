import unittest
import myScript

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.URL = "http://127.0.0.1:5000"

        print("Inside set up")
        self.driver = myScript.create_driver()
        self.driver.get(self.URL)

    def test_valid_login(self):
        print("Inside test valid login")

        valid_username = "hussain"
        valid_password = "password"

        myScript.enter_credentials(self.driver, valid_username, valid_password)
        myScript.attempt_login(self.driver)
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:5000/home" ) 
        
    def test_invalid_user(self):
        print("Inside test invalid user")

        invalid_username = "abc"
        invalid_password = "123"

        myScript.enter_credentials(self.driver, invalid_username, invalid_password)
        myScript.attempt_login(self.driver)
        self.assertEqual(self.driver.current_url,"http://127.0.0.1:5000/" ) 
        
    
    def test_missing_user(self):
        print("Inside test missing user")

        missing_username = ""
        invalid_password = "123"

        myScript.enter_credentials(self.driver, missing_username, invalid_password)
        myScript.attempt_login(self.driver)
        self.assertEqual(self.driver.current_url,"http://127.0.0.1:5000/" ) 
        
    
    def test_missing_password(self):
        print("Inside test missing user")

        missing_username = "hi"
        missing_password = ""

        myScript.enter_credentials(self.driver, missing_username, missing_password)
        myScript.attempt_login(self.driver)
        self.assertEqual(self.driver.current_url,"http://127.0.0.1:5000/" ) 
        
       

    def tearDown(self):
        print("Inside tear down")
        self.driver.quit()


unittest.main()

