// 1. Fruits List
List<string> fruits = new List<string> { "apple", "banana", "cherry", "date", "elderberry" };

// 2. Squares of numbers from 0 to 5
var squares = Enumerable.Range(1, 6).Select(x => x * x).ToList();

// 3. Cubes of numbers from 1 to 5
var cubes = Enumerable.Range(1, 5).Select(x => x * x * x).ToList();

// 3.1. Cubes of numbers from 1 to 5 using Math.Pow
var cubes2 = Enumerable.Range(1, 5).Select(x => Math.Pow(x, 3)).ToList();

// 4. Sum of numbers from 1 to 10
var sum = Enumerable.Range(1, 10).Sum();

// 5. Average of numbers from 1 to 10
var average = Enumerable.Range(1, 10).Average();

// 6. Maximum of numbers from 1 to 10
var max = Enumerable.Range(1, 10).Max();

// 7. Minimum of numbers from 1 to 10
var min = Enumerable.Range(1, 10).Min();

// 8. Count of numbers from 1 to 10
var count = Enumerable.Range(1, 10).Count();

// 9. Count of even numbers from 1 to 10
var countEven = Enumerable.Range(1, 10).Count(x => x % 2 == 0);

// 10. Count of odd numbers from 1 to 10
var countOdd = Enumerable.Range(1, 10).Count(x => x % 2 != 0);

// 11. Count of numbers from 1 to 10 that are greater than 5
var countGreaterThan5 = Enumerable.Range(1, 10).Count(x => x > 5);

// 12. Count of number from 1 to 10 that are less than 5
var countLessThan5 = Enumerable.Range(1, 10).Count(x => x < 5);

// 13. Count of numbers from 1 to 10 that are greater than 5 and less than 8
var countBetween5And8 = Enumerable.Range(1, 10).Count(x => x > 5 && x < 8);

// 14. Count of numbers from 1 to 10 that are not equal to 5
var countNotEqual5 = Enumerable.Range(1, 10).Count(x => x != 5);

// 15. Celcius temperatures
List<int> celciusTemperatures = new List<int> { 0, 10, 20, 30, 40, 50 };

// 16. Fahrenheit temperatures
var fahrenheit = celciusTemperatures.Select(temp => temp * (9 / 5) + 32).ToList();

// 17. Even numbers from 1 to 20
var evenNumbers = Enumerable.Range(1, 20).Where(x => x % 2 == 0).ToList();

// 18. Odd numbers from 1 to 20
var oddNumbers = Enumerable.Range(1, 20).Where(x => x % 2 != 0).ToList();

// 19. Even numbers from 1 to 20 that are greater than 10
var evenNumbersGreaterThan10 = Enumerable.Range(1, 20).Where(x => x % 2 == 0 && x > 10).ToList();

// 20. Odd numbers from 1 to 20 that are less than 10
var oddNumbersLessThan10 = Enumerable.Range(1, 20).Where(x => x % 2 != 0 && x < 10).ToList();

// 21. Words list
List<string> words = new List<string> { "book", "elephant", "sun", "encyclopedia", "apple" };
