from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class UserParams:
    name: str
    age: int
    address: str
    email: str
    phone: str
    user_name: str | None = None


@dataclass
class User:
    user_id: str
    name: str
    age: int
    address: str
    email: str
    phone: str
    user_name: str | None = None

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


class UserService:
    def create_user(self, user_id: str, user_params: UserParams):
        new_user = User.create_from_params(user_id, user_params)
        print(
            f"Creating user with ID: {new_user.user_id}, "
            "name: {new_user.name}, age: {new_user.age}, "
            "address: {new_user.address}, email: {new_user.email}, phone: {new_user.phone}"
        )
        return new_user

    def update_user(self, user: User, user_params: UserParams):
        user.update_with_params(user_params)
        print(
            f"Updating user with name: {user.name}, "
            "age: {user.age}, address: {user.address}, "
            "email: {user.email}, phone: {user.phone}"
        )
        return user


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


@dataclass
class CreateUserCommand(Command):
    user_service: UserService
    user_id: str
    user_params: UserParams

    def execute(self):
        return self.user_service.create_user(self.user_id, self.user_params)


@dataclass
class UpdateUserCommand(Command):
    user_service: UserService
    user: User
    user_params: UserParams

    def execute(self):
        return self.user_service.update_user(self.user, self.user_params)


class UserCommandExecutor:
    history = []

    def execute_command(self, command: Command):
        result = command.execute()
        self.history.append(command)
        return result


def main():
    user_command_executor = UserCommandExecutor()
    user_service = UserService()

    # Creating a new user
    user_params = UserParams(
        name="John",
        age=30,
        address="123 Main St",
        email="john@example.com",
        phone="555-1234",
        user_name="john_doe",
    )
    create_user_command = CreateUserCommand(
        user_service=user_service, user_id="1", user_params=user_params
    )
    new_user = user_command_executor.execute_command(create_user_command)

    # Updating the User entity with new parameters
    updated_params = UserParams(
        name="John Doe",
        age=31,
        address="456 Elm St",
        email="john.doe@example.com",
        phone="555-5678",
        user_name="john_doe_updated",
    )
    update_user_command = UpdateUserCommand(
        user_service=user_service, user=new_user, user_params=updated_params
    )
    updated_user = user_command_executor.execute_command(update_user_command)

    # Outputs for verification
    print(f"Created User: {new_user}")
    print(f"Updated User: {updated_user}")
    print(f"Command History: {user_command_executor.history}")


if __name__ == "__main__":
    main()
