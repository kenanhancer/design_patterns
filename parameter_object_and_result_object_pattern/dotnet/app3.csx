public class UserParams
{
    public string Name { get; set; }
    public int Age { get; set; }
    public string Address { get; set; }
    public string Email { get; set; }
    public string Phone { get; set; }
    public string UserName { get; set; }

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

UserParams user1 = new UserParams(name: "John Doe", age: 30, address: "123 Main St", email: "", phone: "555-1234", userName: "johndoe")
{
    Name = "John Doe",
    Age = 30,
    Address = "123 Main St",
    Email = "",
    Phone = "555-1234",
    UserName = "johndoe"
};