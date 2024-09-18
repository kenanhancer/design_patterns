package parameter_object_and_result_object_pattern.mix_exercises.demo1;

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

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return this.age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getAddress() {
        return this.address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getEmail() {
        return this.email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhone() {
        return this.phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getUsername() {
        return this.username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
}

public class app1 {
    public static void main(String[] args) {
        UserParams user = new UserParams("John", 30, "123 Main St", "", "", "john123");

        System.out.println("Name: " + user.getName());
        System.out.println("Age: " + user.getAge());
    }
}