class UserParams
{
    public string Name;
    public int Age;
    public string Address;
    public string Email;
    public string Phone;
    public string UserName;

    public UserParams(string name, int age, string address, string email, string phone, string userName)
    {
        Name = name;
        Age = age;
        Address = address;
        Email = email;
        Phone = phone;
        UserName = userName;
    }
}

class User
{
    public string UserId;
    public string Name;
    public int Age;
    public string Address;
    public string Email;
    public string Phone;
    public string UserName;

    public User(string userId, string name, int age, string address, string email, string phone, string userName)
    {
        UserId = userId;
        Name = name;
        Age = age;
        Address = address;
        Email = email;
        Phone = phone;
        UserName = userName;
    }

    public void UpdateWithParams(UserParams userParams)
    {
        Name = userParams.Name;
        Age = userParams.Age;
        Address = userParams.Address;
        Email = userParams.Email;
        Phone = userParams.Phone;
        UserName = userParams.UserName;
    }

    public static User CreateFromParams(string userId, UserParams userParams)
    {
        return new User(userId, userParams.Name, userParams.Age, userParams.Address, userParams.Email, userParams.Phone, userParams.UserName);
    }
}

User CreateUser(string userId, UserParams userParams)
{
    User newUser = User.CreateFromParams(userId, userParams);
    Console.WriteLine(
        $@"Creating user with ID: {newUser.UserId}, 
        name: {newUser.Name}, age: {newUser.Age}, 
        address: {newUser.Address}, email: {newUser.Email}, 
        phone: {newUser.Phone}, username: {newUser.UserName}"
    );
    return newUser;
}

User UpdateUser(User user, UserParams userParams)
{
    user.UpdateWithParams(userParams);
    Console.WriteLine(
        $@"Updating user with ID: {user.UserId}, 
        name: {user.Name}, age: {user.Age}, 
        address: {user.Address}, email: {user.Email}, 
        phone: {user.Phone}, username: {user.UserName}"
    );
    return user;
}

void Main()
{
    UserParams userParams = new UserParams(name: "John Doe", age: 30, address: "123 Main St", email: "john@example.com", phone: "555-1234", userName: "johndoe");

    User newUser = CreateUser(userId: "1", userParams: userParams);

    UserParams updatedParams = new UserParams(name: "Jane Doe", age: 31, address: "456 Elm St", email: "john.doe@example.com", phone: "555-5678", userName: "john_doe_updated");

    User updatedUser = UpdateUser(user: newUser, userParams: updatedParams);

    Console.WriteLine($"Created User: {newUser}");

    Console.WriteLine($"Update User: {updatedUser}");
}

Main();