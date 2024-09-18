package mix_exercises.demo1;

public class app1 {
    public static void main(String[] args) {
        System.out.println("Hello, World!");

        String firstName = "Kenan";
        String lastName = "Hancer";
        int age = 40;

        String fullName = STR."\{firstName} \{lastName}";

        String result = STR."My name is \{fullName} and I am \{age} years old.";

        System.out.println(result);
    }
}
