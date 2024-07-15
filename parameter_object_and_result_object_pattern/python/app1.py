# Define the UserParams class to encapsulate parameters
class UserParams:
    def __init__(self, name: str, age: int, address: str, email: str, phone: str):
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.phone = phone


# Method to create a new user with UserParams object as a parameter
def create_user(user_params: UserParams):
    print(
        f"Creating user with name: {user_params.name}, age: {user_params.age}, address: {user_params.address}, email: {user_params.email}, phone: {user_params.phone}"
    )


# Method to update a user with UserParams object as a parameter
def update_user(user_id: int, user_params: UserParams):
    print(
        f"Updating user with ID: {user_id} with name: {user_params.name}, age: {user_params.age}, address: {user_params.address}, email: {user_params.email}, phone: {user_params.phone}"
    )


# Method to display user information
def display_user(user_params: UserParams):
    print(
        f"User Info - Name: {user_params.name}, Age: {user_params.age}, Address: {user_params.address}, Email: {user_params.email}, Phone: {user_params.phone}"
    )


if __name__ == "__main__":
    # Creating a UserParams object and passing it to the methods
    user_params = UserParams(
        name="John",
        age=30,
        address="123 Main St",
        email="john@example.com",
        phone="555-1234",
    )

    create_user(user_params)
    update_user(user_id=1, user_params=user_params)
    display_user(user_params)
