// Define the UserParams class to encapsulate the parameters for the CreateUser method
class UserParams
{
    public string Name;
    public int Age;
    public string Address;
    public string Email;
    public string Phone;

    UserParams(string name, int age, string address, string email, string phone)
    {
        Name = name;
        Age = age;
        Address = address;
        Email = email;
        Phone = phone;
    }
}


void CreateUser(UserParams userParams)
{
    Console.WriteLine(
        $@"Creating user with name: {userParams.Name}, 
        age: {userParams.Age}, address: {userParams.Address}, 
        email: {userParams.Email}, phone: {userParams.Phone}"
    );
}


void UpdateUser(UserParams userParams)
{
    Console.WriteLine(
        $@"Updating user with name: {userParams.Name}, 
        age: {userParams.Age}, address: {userParams.Address}, 
        email: {userParams.Email}, phone: {userParams.Phone}"
    );
}

void DisplayUser(UserParams userParams)
{
    Console.WriteLine(
        $@"Displaying user with name: {userParams.Name}, 
        age: {userParams.Age}, address: {userParams.Address}, 
        email: {userParams.Email}, phone: {userParams.Phone}"
    );
}

void Main()
{
    var userParams = new UserParams(name: "John Doe", age: 30, address: "123 Main St", email: "john@example.com", phone: "555-1234");

    CreateUser(userParams);
    UpdateUser(userParams);
    DisplayUser(userParams);
}

Main();