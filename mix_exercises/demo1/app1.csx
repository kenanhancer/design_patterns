List<string> names = new List<string> { "John", "Jane", "Jack", "Jill" };

names.Add("Jesse");

var query = from name in names
            where name.StartsWith("J")
            select name;

Console.WriteLine("Names starting with 'J':");
Console.WriteLine(string.Join(", ", query));

WriteLine("Hello from app1.csx");