from dataclasses import dataclass


class UserParams:
    def __init__(self, name, age, address, email, phone, user_name):
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.phone = phone
        self.user_name = user_name


class UserParams2:
    def __init__(
        self,
        name: str,
        age: int,
        address: str,
        email: str,
        phone: str,
        user_name: str = None,
    ):
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.phone = phone
        self.user_name = user_name
        
@dataclass
class UserParams3:
    name: str
    age: int
    address: str
    emai: str
    phone: str
    user_name: str = None)
    


class UserParams4:


user1 = UserParams("John", 30, "123 Main St", "", "555-1234", "john_doe")
user2 = UserParams2("John", 30, "123 Main St", "", "555-1234", "john_doe")
user3 = UserParams3("John", 30, "123 Main St", "", "555-1234", "john_doe")
