from fastapi import HTTPException, Depends, status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.schemas.user import User, UserBase

# Initialize the InferringRouter with metadata
router = InferringRouter(
    prefix="/users",
    tags=["users"],
    responses={400: {"description": "Bad Request"}, 404: {"description": "Not Found"}},
)

# In-Memory Data Storage with Initial Data
initial_users: list[User] = [
    User(id=1, username="john_doe", email="john@example.com"),
    User(id=2, username="jane_smith", email="jane@example.com"),
    User(id=3, username="joe_bloggs", email="joe@example.com"),
]


class UserManager:
    def __init__(self, users: list[User]):
        self.users: list[User] = users
        self.user_id_counter = len(users) + 1  # Starts from the next available ID

    def get_all_users(self):
        return self.users

    def create_user(self, user_data: UserBase):
        new_user = User(id=self.user_id_counter, **user_data.model_dump())
        self.users.append(new_user)
        self.user_id_counter += 1
        return new_user

    def get_user(self, user_id: int):
        return next((user for user in self.users if user.id == user_id), None)

    def update_user(self, user_id: int, user_update: UserBase):
        for idx, user in enumerate(self.users):
            if user.id == user_id:
                updated_user = User(id=user_id, **user_update.model_dump())
                self.users[idx] = updated_user
                return updated_user
        return None

    def delete_user(self, user_id: int):
        original_length = len(self.users)
        self.users = [user for user in self.users if user.id != user_id]
        return len(self.users) < original_length


user_manager = UserManager(initial_users)


@cbv(router)
class UserView:

    user_manager: UserManager = Depends(lambda: user_manager)

    @router.get(
        "/",
        response_model=list[User],
        status_code=status.HTTP_200_OK,
        summary="Retrieve All Users",
        description="Fetch a list of all users in the system.",
        responses={200: {"description": "List of users retrieved successfully"}},
    )
    def get_users(self):
        return self.user_manager.get_all_users()  # pylint: disable=no-member

    @router.post(
        "/",
        response_model=User,
        status_code=status.HTTP_201_CREATED,
        summary="Create a New User",
        description="Add a new user to the collection.",
        responses={
            201: {"description": "User created successfully."},
            400: {"description": "Invalid input data."},
        },
    )
    def create_user(self, new_user: UserBase):
        return self.user_manager.create_user(new_user)  # pylint: disable=no-member

    @router.get(
        "/{user_id}",
        response_model=User,
        status_code=status.HTTP_200_OK,
        summary="Retrieve a User",
        description="Fetch a user by ID.",
        responses={
            200: {"description": "User retrieved successfully."},
            404: {"description": "User not found."},
        },
    )
    def get_user(self, user_id: int):
        user = self.user_manager.get_user(user_id)  # pylint: disable=no-member
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        return user

    @router.put(
        "/{user_id}",
        response_model=User,
        status_code=status.HTTP_200_OK,
        summary="Update a User",
        description="Update user details by ID.",
        responses={
            200: {"description": "User updated successfully."},
            404: {"description": "User not found."},
        },
    )
    def update_user(self, user_id: int, user_update: UserBase):
        updated_user = self.user_manager.update_user(  # pylint: disable=no-member
            user_id, user_update
        )  # pylint: disable=no-member
        if not updated_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        return updated_user

    @router.delete(
        "/{user_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a User",
        description="Remove a user from the collection.",
        responses={
            204: {"description": "User deleted successfully."},
            404: {"description": "User not found."},
        },
    )
    def delete_user(self, user_id: int):
        if not self.user_manager.delete_user(user_id):  # pylint: disable=no-member
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
