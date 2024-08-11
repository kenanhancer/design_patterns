# Define the UserParams class to encapsulate parameters
class UserParams:
    def __init__(
        self,
        name: str,
        age: int,
        address: str,
        email: str,
        phone: str,
        user_name: str | None = None,
    ):
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.phone = phone
        self.user_name = user_name


# Define the User entity class
class User:
    def __init__(
        self,
        user_id: str,
        name: str,
        age: int,
        address: str,
        email: str,
        phone: str,
        user_name: str | None = None,
    ):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.phone = phone
        self.user_name = user_name

    def update_with_params(self, user_params: UserParams):
        self.name = user_params.name
        self.age = user_params.age
        self.address = user_params.address
        self.email = user_params.email
        self.phone = user_params.phone
        self.user_name = user_params.user_name

    @staticmethod
    def create_from_params(user_id: str, user_params: UserParams):
        return User(
            user_id=user_id,
            name=user_params.name,
            age=user_params.age,
            address=user_params.address,
            email=user_params.email,
            phone=user_params.phone,
            user_name=user_params.user_name,
        )


# Method to create a new user with UserParams object as a parameter
def create_user(user_id: str, user_params: UserParams):
    new_user = User.create_from_params(user_id, user_params)
    print(
        f"Creating user with ID: {new_user.user_id}, "
        "name: {new_user.name}, age: {new_user.age}, "
        "address: {new_user.address}, email: {new_user.email}, phone: {new_user.phone}"
    )
    return new_user


# Method to update a user with UserParams object as a parameter
def update_user(user: User, user_params: UserParams):
    user.update_with_params(user_params)
    print(
        f"Updating user with name: {user.name}, "
        "age: {user.age}, address: {user.address}, "
        "email: {user.email}, phone: {user.phone}"
    )
    return user


def main():
    # Creating a UserParams object and passing it to the methods
    user_params = UserParams(
        name="John",
        age=30,
        address="123 Main St",
        email="john@example.com",
        phone="555-1234",
        user_name="john_doe",
    )

    # Creating a User entity from UserParams
    new_user = create_user(user_id=1, user_params=user_params)

    # Updating the User entity with new parameters
    updated_params = UserParams(
        name="John Doe",
        age=31,
        address="456 Elm St",
        email="john.doe@example.com",
        phone="555-5678",
        user_name="john_doe_updated",
    )
    updated_user = update_user(user=new_user, user_params=updated_params)

    # Outputs for verification
    print(f"Created User: {new_user}")
    print(f"Updated User: {updated_user}")


if __name__ == "__main__":
    main()
