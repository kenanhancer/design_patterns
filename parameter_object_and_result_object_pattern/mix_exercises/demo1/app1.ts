class UserParams {
  name: string;
  age: number;
  address: string;
  email: string;
  phone: string;
  username: string;

  constructor(
    name: string,
    age: number,
    address: string,
    email: string,
    phone: string,
    username: string
  ) {
    this.name = name;
    this.age = age;
    this.address = address;
    this.email = email;
    this.phone = phone;
    this.username = username;
  }
}

class UserParams2 {
  constructor(
    public name: string,
    public age: number,
    public address: string,
    public email: string,
    public phone: string,
    public username: string
  ) {}
}
