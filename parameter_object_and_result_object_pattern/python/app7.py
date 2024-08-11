from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CreateUserParams:
    user_id: str
    name: str
    age: int
    address: str
    email: str
    phone: str
    user_name: str | None = None


@dataclass
class UpdateUserParams:
    name: str | None = None
    age: int | None = None
    address: str | None = None
    email: str | None = None
    phone: str | None = None
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

    def update_with_params(self, update_params: UpdateUserParams):
        if update_params.name:
            self.name = update_params.name
        if update_params.age:
            self.age = update_params.age
        if update_params.address:
            self.address = update_params.address
        if update_params.email:
            self.email = update_params.email
        if update_params.phone:
            self.phone = update_params.phone
        if update_params.user_name:
            self.user_name = update_params.user_name

    @staticmethod
    def create_from_params(create_params: CreateUserParams):
        return User(
            user_id=create_params.user_id,
            name=create_params.name,
            age=create_params.age,
            address=create_params.address,
            email=create_params.email,
            phone=create_params.phone,
            user_name=create_params.user_name,
        )


class UserService:
    def create_user(self, create_params: CreateUserParams):
        new_user = User.create_from_params(create_params)
        print(
            f"Creating user with ID: {new_user.user_id}, "
            "name: {new_user.name}, age: {new_user.age}, "
            "address: {new_user.address}, email: {new_user.email}, phone: {new_user.phone}"
        )
        return new_user

    def update_user(self, user: User, update_params: UpdateUserParams):
        user.update_with_params(update_params)
        print(
            f"Updating user with name: {user.name}, "
            "age: {user.age}, address: {user.address}, "
            "email: {user.email}, phone: {user.phone}"
        )
        return user


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


@dataclass
class CreateUserCommand(Command):
    user_service: UserService
    create_params: CreateUserParams

    def execute(self):
        return self.user_service.create_user(self.create_params)


@dataclass
class UpdateUserCommand(Command):
    user_service: UserService
    user: User
    update_params: UpdateUserParams

    def execute(self):
        return self.user_service.update_user(self.user, self.update_params)


class UserCommandExecutor:
    def __init__(self):
        self.history = []

    def execute_command(self, command: Command):
        result = command.execute()
        self.history.append(command)
        return result


def main():
    user_command_executor = UserCommandExecutor()
    user_service = UserService()

    # Creating a new user
    create_params = CreateUserParams(
        user_id="1",
        name="John",
        age=30,
        address="123 Main St",
        email="john@example.com",
        phone="555-1234",
        user_name="john_doe",
    )
    create_user_command = CreateUserCommand(
        user_service=user_service, create_params=create_params
    )
    new_user = user_command_executor.execute_command(create_user_command)

    # Updating the User entity with new parameters
    update_params = UpdateUserParams(
        name="John Doe",
        age=31,
        address="456 Elm St",
        email="john.doe@example.com",
        phone="555-5678",
        user_name="john_doe_updated",
    )
    update_user_command = UpdateUserCommand(
        user_service=user_service, user=new_user, update_params=update_params
    )
    updated_user = user_command_executor.execute_command(update_user_command)

    # Outputs for verification
    print(f"Created User: {new_user}")
    print(f"Updated User: {updated_user}")
    print(f"Command History: {user_command_executor.history}")


if __name__ == "__main__":
    main()
