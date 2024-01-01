class User:
    def __init__(self):
        self.username = None
        self.password = None

    def add_username(self, username):   
        print("Testing inalid username condition")
        self.username = username

    def add_password(self, password):
        self.password = password

    def __str__(self) -> str:
        return f"{self.username} {self.password}"



def getUser() -> User:
    u1 = User()
    u1.add_username("hussain")
    u1.add_password("password")
    return u1

 
if __name__ == "__main__":
    getUser()