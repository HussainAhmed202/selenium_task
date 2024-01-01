import unittest
import myScript
from user import getUser

class TestLogin(unittest.TestCase):

    def setUp(self):
         """ This function sets up the test suite by creating a new instance of the 
            WebDriver and navigating to the base URL.  """
         
         self.valid_user = getUser()

         print("Inside set up")
         self.driver = myScript.create_driver()
         self.driver.get("http://127.0.0.1:5000")

    def test_valid_login(self):
        print("Testing valid login attempt...")

        myScript.enter_credentials(self.driver, self.valid_user.username ,self.valid_user.password)
        myScript.attempt_login(self.driver)
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:5000/home" ) 
        
    def test_invalid_user(self):
        print("Testing invalid user login attempt")

        invalid_username = "abc$%"
        invalid_password = "123"

        myScript.enter_credentials(self.driver, invalid_username, invalid_password)
        myScript.attempt_login(self.driver)
        self.assertEqual(self.driver.current_url,"http://127.0.0.1:5000/" )


    def test_invalid_password(self):
        print("Testing invalid password  condition")

        invalid_password = "hello"

        myScript.enter_credentials(self.driver, self.valid_user.username, invalid_password)
        myScript.attempt_login(self.driver)
        self.assertEqual(self.driver.current_url,"http://127.0.0.1:5000/" )
        

    def test_invalid_username(self):
        print("Testing invalid username condition")

        invalid_username = "wronguser"
        
        myScript.enter_credentials(self.driver, invalid_username, self.valid_user.password)
        myScript.attempt_login(self.driver)
        self.assertEqual(self.driver.current_url,"http://127.0.0.1:5000/" )
         



    def tearDown(self):
        print("Inside tear down")
        self.driver.quit()



 
if __name__ == "__main__":
    unittest.main()

