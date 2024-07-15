// Define the UserParams class to encapsulate parameters
class UserParams {
    name: string;
    age: number;
    address: string;
    email: string;
    phone: string;

    constructor(name: string, age: number, address: string, email: string, phone: string) {
        this.name = name;
        this.age = age;
        this.address = address;
        this.email = email;
        this.phone = phone;
    }
}

// Method to create a new user with UserParams object as a parameter
function createUser(userParams: UserParams): void {
    console.log(
        `Creating user with name: ${userParams.name}, age: ${userParams.age}, address: ${userParams.address}, email: ${userParams.email}, phone: ${userParams.phone}`
    );
}

// Method to update a user with UserParams object as a parameter
function updateUser(userId: number, userParams: UserParams): void {
    console.log(
        `Updating user with ID: ${userId} with name: ${userParams.name}, age: ${userParams.age}, address: ${userParams.address}, email: ${userParams.email}, phone: ${userParams.phone}`
    );
}

// Method to display user information
function displayUser(userParams: UserParams): void {
    console.log(
        `User Info - Name: ${userParams.name}, Age: ${userParams.age}, Address: ${userParams.address}, Email: ${userParams.email}, Phone: ${userParams.phone}`
    );
}

// Main execution
(() => {
    // Creating a UserParams object and passing it to the methods
    const userParams = new UserParams(
        "John",
        30,
        "123 Main St",
        "john@example.com",
        "555-1234"
    );

    createUser(userParams);
    updateUser(1, userParams);
    displayUser(userParams);
})();
