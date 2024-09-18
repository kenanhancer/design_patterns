List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
List<string> fruits = new List<string> { "apple", "banana", "cherry" };


// numbers.ForEach(Console.WriteLine);
// fruits.ForEach(Console.WriteLine);

Console.WriteLine("[" + string.Join(", ", numbers) + "]");
Console.WriteLine($"[{string.Join(", ", numbers)}]");
