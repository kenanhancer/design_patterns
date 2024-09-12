import math


fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Generating a list of numbers
squares = [x**2 for x in range(6)]
cubes = [x**3 for x in range(1, 6)]
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * (9 / 5)) + 32 for temp in celsius]

# Filtering
evens = [x for x in range(6) if x % 2 == 0]
odds = [x for x in range(1, 21) if x % 2 != 0]

words = ["book", "elephant", "sun", "encyclopedia", "apple"]
long_words = [word for word in words if len(word) > 5]

# Flattening a matrix
matrix_3d = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24]],
]
flat_list_3d = [number for row in matrix_3d for sublist in row for number in sublist]

# Categorizing age groups
ages = [2, 10, 15, 20, 25, 30, 35, 40, 45, 50]
categories = [
    "child" if age < 13 else "teen" if 13 <= age < 18 else "adult" for age in ages
]

# Tuples with number and its square
tuples = [(x, x**2) for x in range(5)]
# Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

# Permutations of Numbers and Letters
numbers = [1, 2, 3]
letters = ["a", "b", "c"]
permutations = [(number, letter) for number in numbers for letter in letters]

# Pairing Cities with Countries
cities = ["New York", "Los Angeles", "Chicago"]
countries = ["USA", "Canada", "Mexico"]
city_country_pairs = [(city, country) for city in cities for country in countries]

# Extracting Even Indexed Elements
numbers_v2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_indexed_elements = [num for index, num in enumerate(numbers_v2) if index % 2 == 0]

even_indexed_elements_v2 = [
    numbers_v2[index] for index in range(len(numbers_v2)) if index % 2 == 0
]

# Reversing each word
words_v2 = ["apple", "banana", "cherry", "date", "elderberry"]
reversed_words = [word[::-1] for word in words_v2]

# Counting Characters in words
SENTENCE = "The quick brown fox jumps over the lazy dog"
word_lengths = [len(word) for word in SENTENCE.split()]

# Filtering Palindromes
words_palindrome = ["radar", "apple", "level", "banana", "rotor"]
palindromes = [word for word in words_palindrome if word == word[::-1]]

# Generate list of prime numbers
primes = [num for num in range(2, 101) if all(num % i != 0 for i in range(2, num))]

# Filtering positive numbers
numbers_v3 = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positive_numbers = [num for num in numbers_v3 if num > 0]

# Filtering negative numbers
numbers_v4 = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
negative_numbers = [num for num in numbers_v4 if num < 0]

# Square of positive numbers
numbers_v5 = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
squares_positive = [num**2 for num in numbers_v5 if num > 2]

# Squares of negative numbers
numbers_v6 = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
squares_negative = [num**2 for num in numbers_v6 if num < 0]

# Squares of even numbers
numbers_v7 = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
squares_even = [num**2 for num in numbers_v7 if num % 2 == 0]

# Squares of odd numbers
numbers_v8 = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
squares_odd = [num**2 for num in numbers_v8 if num % 2 != 0]

# Filtering non empty strings
strings_v1 = ["", "apple", "banana", "", "cherry", "date", "", "elderberry"]
non_empty_strings = [str for str in strings_v1 if str]

non_empty_strings_v2 = [str for str in strings_v1 if str != ""]

non_empty_strings_v3 = [str for str in strings_v1 if len(str) > 0]

# Repeating each element three times
elements_v1 = [1, 2, 3, 4, 5]
repeated_elements = [num * 3 for num in elements_v1]

# Mapping each item to uppercase
words_v3 = ["apple", "banana", "cherry", "date", "elderberry"]
uppercase_words = [word.upper() for word in words_v3]

# Multiples of 3
multiples_of_3 = [num for num in range(1, 31) if num % 3 == 0]

# Multiples of 3 and 5
multiples_of_3_and_5 = [num for num in range(1, 31) if num % 3 == 0 and num % 5 == 0]

# Generating a list of tuples
tuples_v2 = [(x, y) for x in range(3) for y in range(3)]

# Generating a list of tuples with different values
tuples_v3 = [(x, y) for x in range(3) for y in range(3) if x != y]

# Generating a list of factorials
factorials = [math.factorial(num) for num in range(6)]

# Extracting the first letter of each word
words_v4 = ["apple", "banana", "cherry", "date", "elderberry"]
first_letters = [word[0] for word in words_v4]

# Extracting the last letter of each word
words_v5 = ["apple", "banana", "cherry", "date", "elderberry"]
last_letters = [word[-1] for word in words_v5]

# Extracting the first and last letter of each word
words_v6 = ["apple", "banana", "cherry", "date", "elderberry"]
first_last_letters = [word[0] + word[-1] for word in words_v6]

# Extracting the first and last letter of each word in uppercase
words_v7 = ["apple", "banana", "cherry", "date", "elderberry"]
first_last_letters_upper = [word[0].upper() + word[-1].upper() for word in words_v7]

# Extracting digits from a string
SENTENCE_V2 = "The 3 numbers are 1, 2, and 3"
digits = [char for char in SENTENCE_V2 if char.isdigit()]

# Extracting digits from a string
SENTENCE_V3 = "Phone: 123-456-7890"
digits_v3 = [char for char in SENTENCE_V3 if char.isdigit()]

# Extracting words with more than 5 characters
SENTENCE_V4 = "The quick brown fox jumps over the lazy dog"
words_v8 = [word for word in SENTENCE_V4.split() if len(word) > 5]

# Converting prices to different currency
prices = [10, 20, 30, 40, 50]
prices_usd = [price * 1.1 for price in prices]
prices_eur = [price * 1.25 for price in prices]
prices_gbp = [price * 1.4 for price in prices]
prices_tuple = [(price, price * 1.1, price * 1.25, price * 1.4) for price in prices]

# Flatten a list of tuples
tuples_v4 = [(1, 2), (3, 4), (5, 6)]
flat_list = [item for tuple in tuples_v4 for item in tuple]

# Checking Prime status
numbers_v9 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
is_prime = lambda num: all(num % i != 0 for i in range(2, num)) and num > 1
prime_status = ["prime" if is_prime(num) else "not prime" for num in range(1, 11)]

# Squares of numbers divisible by 3
numbers_v10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_divisible_by_3 = [number**2 for number in numbers_v10 if number % 3 == 0]

# Pairing numbers and letters
numbers_v11 = [1, 2, 3]
letters_v2 = ["a", "b", "c"]
pair = [(number, letter) for number in numbers_v11 for letter in letters_v2]

# Creating acronyms
words_v9 = ["Portable", "Network", "Graphics"]
ACRONYM = "".join(word[0] for word in words_v9)

# Converting a list of string to uppercase
words_v10 = ["apple", "banana", "cherry", "date", "elderberry"]
uppercase_words_v2 = [word.upper() for word in words_v10]

# Converting a list of string to lowercase
words_v11 = ["APPLE", "BANANA", "CHERRY", "DATE", "ELDERBERRY"]
lowercase_words = [word.lower() for word in words_v11]

# Converting a list of string to title case
words_v12 = ["apple", "banana", "cherry", "date", "elderberry"]
title_case_words = [word.title() for word in words_v12]
# Output: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# Converting a list of string to sentence case
words_v13 = ["apple", "banana", "cherry", "date", "elderberry"]
sentence_case_words = [word.capitalize() for word in words_v13]
# Output: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# Converting a list of string to snake case

# Converting a list of string to integers
numbers_v12 = ["1", "2", "3", "4", "5"]
integers = [int(num) for num in numbers_v12]

# Multiplies of numbers with condition
multiplies = [num * 2 if num % 2 == 0 else num * 3 for num in range(1, 11)]
multiplies_v2 = [num for num in range(1, 51) if num % 5 == 0 and num > 20]

# Uppercase Words only if longer than 4 characters
words_v14 = ["apple", "banana", "cherry", "date", "elderberry"]
uppercase_words_v3 = [word.upper() if len(word) > 4 else word for word in words_v14]

# Filtering vowels from a sentence
SENTENCE_V5 = "The quick brown fox jumps over the lazy dog"
vowels = [char for char in SENTENCE_V5 if char in "aeiouAEIOU"]

# Finding the maximum value in a list
numbers_v13 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_value = max(numbers_v13)

# Finding the minimum value in a list
numbers_v14 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_value = min(numbers_v14)

# Finding the sum of all elements in a list
numbers_v15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_elements = sum(numbers_v15)

# Finding the average of all elements in a list
numbers_v16 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
average = sum(numbers_v16) / len(numbers_v16)

# Finding the median of all elements in a list
numbers_v17 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorted_numbers = sorted(numbers_v17)

# Finding the mode of all elements in a list
numbers_v18 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mode = max(set(numbers_v18), key=numbers_v18.count)

# Finding the range of all elements in a list
numbers_v19 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
range_elements = max(numbers_v19) - min(numbers_v19)

# Finding the standard deviation of all elements in a list
numbers_v20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean = sum(numbers_v20) / len(numbers_v20)
variance = sum((x - mean) ** 2 for x in numbers_v20) / len(numbers_v20)

# Finding common elements in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = [element for element in list1 if element in list2]

# Finding the difference between two lists
list1_v3 = [1, 2, 3, 4, 5]
list2_v3 = [4, 5, 6, 7, 8]
difference = [element for element in list1_v3 if element not in list2_v3]

# Finding unique elements in two lists
list1_v2 = [1, 2, 3, 4, 5]
list2_v2 = [4, 5, 6, 7, 8]
unique_elements = [element for element in list1_v2 if element not in list2_v2] + [
    element for element in list2_v2 if element not in list1_v2
]

# Finding the union of two lists
list1_v4 = [1, 2, 3, 4, 5]
list2_v4 = [4, 5, 6, 7, 8]
union = list(set(list1_v4) | set(list2_v4))

# Finding the intersection of two lists
list1_v5 = [1, 2, 3, 4, 5]
list2_v5 = [4, 5, 6, 7, 8]
intersection = list(set(list1_v5) & set(list2_v5))

# Finding the symmetric difference of two lists
list1_v6 = [1, 2, 3, 4, 5]
list2_v6 = [4, 5, 6, 7, 8]
symmetric_difference = list(set(list1_v6) ^ set(list2_v6))

# Finding the cartesian product of two lists
list1_v7 = [1, 2]
list2_v7 = ["a", "b"]
cartesian_product = [(x, y) for x in list1_v7 for y in list2_v7]
# Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# Finding the dot product of two lists
list1_v8 = [1, 2, 3]
list2_v8 = [4, 5, 6]
dot_product = sum(x * y for x, y in zip(list1_v8, list2_v8))
# Output: 32

# Finding the cross product of two lists
list1_v9 = [1, 2, 3]
list2_v9 = [4, 5, 6]
cross_product = [(x, y) for x in list1_v9 for y in list2_v9]
# Output: [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

# Finding the sum of two lists
list1_v10 = [1, 2, 3]
list2_v10 = [4, 5, 6]
sum_lists = [x + y for x, y in zip(list1_v10, list2_v10)]
# Output: [5, 7, 9]

# Finding the difference of two lists
list1_v11 = [1, 2, 3]
list2_v11 = [4, 5, 6]
difference_lists = [x - y for x, y in zip(list1_v11, list2_v11)]
# Output: [-3, -3, -3]

# Finding the product of two lists
list1_v12 = [1, 2, 3]
list2_v12 = [4, 5, 6]
product_lists = [x * y for x, y in zip(list1_v12, list2_v12)]
# Output: [4, 10, 18]

# Finding the quotient of two lists
list1_v13 = [1, 2, 3]
list2_v13 = [4, 5, 6]
quotient_lists = [x / y for x, y in zip(list1_v13, list2_v13)]
# Output: [0.25, 0.4, 0.5]

# Finding the remainder of two lists
list1_v14 = [1, 2, 3]
list2_v14 = [4, 5, 6]
remainder_lists = [x % y for x, y in zip(list1_v14, list2_v14)]
# Output: [1, 2, 3]

# Finding the power of two lists
list1_v15 = [1, 2, 3]
list2_v15 = [4, 5, 6]
power_lists = [x**y for x, y in zip(list1_v15, list2_v15)]
# Output: [1, 32, 729]

# Finding the square root of a list
numbers_v21 = [1, 4, 9, 16, 25]
square_root = [math.sqrt(num) for num in numbers_v21]

# Finding the cube root of a list
numbers_v22 = [1, 8, 27, 64, 125]
cube_root = [num ** (1 / 3) for num in numbers_v22]

# Finding the nth root of a list
numbers_v23 = [1, 4, 9, 16, 25]
nth_root = [num ** (1 / 2) for num in numbers_v23]

# Finding the absolute value of a list
numbers_v24 = [1, -2, 3, -4, 5]
absolute_value = [abs(num) for num in numbers_v24]

# Finding the factorial of a list
numbers_v25 = [1, 2, 3, 4, 5]
factorial = [math.factorial(num) for num in numbers_v25]

# Finding the natural logarithm of a list
numbers_v26 = [1, 2, 3, 4, 5]
natural_logarithm = [math.log(num) for num in numbers_v26]

# Finding the base 10 logarithm of a list
numbers_v27 = [1, 2, 3, 4, 5]
base_10_logarithm = [math.log10(num) for num in numbers_v27]

# Finding the base 2 logarithm of a list
numbers_v28 = [1, 2, 3, 4, 5]
base_2_logarithm = [math.log2(num) for num in numbers_v28]

# Finding the exponential of a list
numbers_v29 = [1, 2, 3, 4, 5]
exponential = [math.exp(num) for num in numbers_v29]

# Finding the power of a list
numbers_v30 = [1, 2, 3, 4, 5]
power = [math.pow(num, 2) for num in numbers_v30]

# Finding the sine of a list
numbers_v31 = [0, math.pi / 4, math.pi / 2, 3 * math.pi / 4, math.pi]
sine = [math.sin(num) for num in numbers_v31]

# Finding the cosine of a list
numbers_v32 = [0, math.pi / 4, math.pi / 2, 3 * math.pi / 4, math.pi]
cosine = [math.cos(num) for num in numbers_v32]

# Finding the tangent of a list
numbers_v33 = [0, math.pi / 4, math.pi / 2, 3 * math.pi / 4, math.pi]
tangent = [math.tan(num) for num in numbers_v33]

# Finding the hyperbolic sine of a list
numbers_v34 = [0, 1, 2, 3, 4]
hyperbolic_sine = [math.sinh(num) for num in numbers_v34]

# Finding the hyperbolic cosine of a list
numbers_v35 = [0, 1, 2, 3, 4]
hyperbolic_cosine = [math.cosh(num) for num in numbers_v35]

# Finding the hyperbolic tangent of a list
numbers_v36 = [0, 1, 2, 3, 4]
hyperbolic_tangent = [math.tanh(num) for num in numbers_v36]

# Finding the inverse sine of a list
numbers_v37 = [0, 0.5, 1]
inverse_sine = [math.asin(num) for num in numbers_v37]

# Finding the inverse cosine of a list
numbers_v38 = [0, 0.5, 1]
inverse_cosine = [math.acos(num) for num in numbers_v38]

# Finding the inverse tangent of a list
numbers_v39 = [0, 1, math.inf]
inverse_tangent = [math.atan(num) for num in numbers_v39]

# Finding the inverse hyperbolic sine of a list
numbers_v40 = [0, 1, 2, 3, 4]
inverse_hyperbolic_sine = [math.asinh(num) for num in numbers_v40]

# Finding the inverse hyperbolic cosine of a list
numbers_v41 = [0, 1, 2, 3, 4]
inverse_hyperbolic_cosine = [math.acosh(num) for num in numbers_v41]

# Finding the inverse hyperbolic tangent of a list
numbers_v42 = [0, 0.5, 1]
inverse_hyperbolic_tangent = [math.atanh(num) for num in numbers_v42]

# Finding the greatest common divisor of a list
numbers_v43 = [10, 20, 30, 40, 50]
greatest_common_divisor = math.gcd(*numbers_v43)

# Finding the least common multiple of a list
numbers_v44 = [10, 20, 30, 40, 50]
least_common_multiple = math.lcm(*numbers_v44)

# Reversing each word in a list
words_v15 = ["apple", "banana", "cherry", "date", "elderberry"]
reversed_words_v2 = [word[::-1] for word in words_v15]

# Generating coordinates pairs
coordinates = [(x, y) for x in range(3) for y in range(3)]
# output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Generating coordinates pairs with different values
coordinates_v2 = [(x, y) for x in range(3) for y in range(3) if x != y]
# output: [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
