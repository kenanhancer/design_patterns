class UserParams {
    private String name;
    private int age;
    private String address;
    private String email;
    private String phone;
    private String username;

    public UserParams(String name, int age, String address, String email, String phone, String username) {
        this.name = name;
        this.age = age;
        this.address = address;
        this.email = email;
        this.phone = phone;
        this.username = username;
    }

    public String getName() {
        return this.name;
    }

    public String setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return this.age;
    }

    public int setAge(int age) {
        this.age = age;
    }

    public String getAddress() {
        return this.address;
    }

    public String setAddress(String address) {
        this.address = address;
    }

    public String getEmail() {
        return this.email;
    }

    public String setEmail(String email) {
        this.email = email;
    }

    public String getPhone() {
        return this.phone;
    }

    public String setPhone(String phone) {
        this.phone = phone;
    }

    public String getUsername() {
        return this.username;
    }

    public String setUsername(String username) {
        this.username = username;
    }
}