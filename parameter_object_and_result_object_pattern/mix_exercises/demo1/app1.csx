class UserParams
{
    private string _name;
    private int _age;
    private string _address;
    private string _email;
    private string _phone;
    private string _userName;

    public string Name
    {
        get => _name;
        set = _name = value;
    }

    public int Age
    {
        get => _age;
        set => _age = value;
    }

    public string Address
    {
        get => _address;
        set => _address = value;
    }

    public string Email
    {
        get => _email;
        set => _email = value;
    }

    public string Phone
    {
        get => _phone;
        set => _phone = value;
    }

    public string UserName
    {
        get => _userName;
        set => _userName = value;
    }

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

class UserParams2
{
    public string Name { get; set; }
    public int Age { get; set; }
    public string Address { get; set; }
    public string Email { get; set; }
    public string Phone { get; set; }
    public string UserName { get; set; }

    public UserParams2(string name, int age, string address, string email, string phone, string userName)
    {
        Name = name;
        Age = age;
        Address = address;
        Email = email;
        Phone = phone;
        UserName = userName;
    }
}

UserParams user1 = new UserParams("John", 30, "123 Main St", "", "", "john123");

UserParams2 user2 = new UserParams2("John", 30, "123 Main St", "", "", "john123");