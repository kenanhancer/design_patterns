# Design Patterns Project

Welcome to the Design Patterns Project! This repository contains examples and implementations of various design patterns using multiple programming languages including C#, Java, Kotlin, Python, and TypeScript.

## Table of Contents

- [Introduction](#introduction)
- [Languages Used](#languages-used)
- [Access Modifiers](#access-modifiers)
- [Design Patterns Implemented](#design-patterns-implemented)
- [Setup Instructions](#setup-instructions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Design patterns are typical solutions to common problems in software design. Each pattern is like a blueprint that you can customize to solve a particular design problem in your code. This project aims to provide clear, well-documented examples of these patterns in various programming languages to aid in learning and applying them in real-world scenarios.

## Languages Used

The following languages are used in this project:

- C#
- Java
- Kotlin
- Python
- TypeScript

Each language has its own directory containing the implementations of the design patterns.

## Access Modifiers


| Access Modifier | C# (Class Members) | Java (Class Members) | Python & TypeScript (Class Members) |
|-----------------|--------------------|----------------------|---------------------------------------|
| public          | Accessible from any code. | Accessible from any code. | Accessible from any code. |
| private         | Accessible only within the same class. | Accessible only within the same class. | Python: Naming convention (e.g., _var) |
| protected       | Accessible within the same class and derived classes. | Accessible within the same class and derived classes. | TypeScript: Accessible within the same class and derived classes. |
| internal        | Accessible within the same assembly. | N/A | N/A |
| protected internal | Accessible within the same assembly and derived classes. | Accessible within the same package and derived classes. | TypeScript: Accessible within the same package and derived classes. |
| Default (No Modifier) | Private | Package-private (default) | Public |

## Design Patterns Implemented

Below is a list of design patterns implemented in this repository:

1. **Creational Patterns**
   - Singleton
   - Factory Method
   - Abstract Factory
   - Builder
   - Prototype

2. **Structural Patterns**
   - Adapter
   - Bridge
   - Composite
   - Decorator
   - Facade
   - Flyweight
   - Proxy

3. **Behavioral Patterns**
   - Chain of Responsibility
   - Command
   - Iterator
   - Mediator
   - Memento
   - Observer
   - State
   - Strategy
   - Template Method
   - Visitor

Each pattern is implemented in the `src` directory of the respective language.

## Setup Instructions

To run the examples, follow the instructions for each language:

### C#

1. Ensure you have [.NET](https://dotnet.microsoft.com/download) installed.
2. Navigate to the C# project directory.
3. Build and run the project using `dotnet build` and `dotnet run`.

### Java

1. Ensure you have [Java JDK](https://www.oracle.com/java/technologies/javase-downloads.html) installed.
2. Navigate to the Java project directory.
3. Compile and run the project using `javac` and `java` commands.

### Kotlin

1. Ensure you have [Kotlin](https://kotlinlang.org/docs/command-line.html) installed.
2. Navigate to the Kotlin project directory.
3. Compile and run the project using `kotlinc` and `kotlin` commands.

### Python

1. Ensure you have [Python](https://www.python.org/downloads/) installed.
2. Navigate to the Python project directory.
3. Run the scripts using `python <script_name>.py`.

### TypeScript

1. Ensure you have [Node.js](https://nodejs.org/en/) and [TypeScript](https://www.typescriptlang.org/download) installed.
2. Navigate to the TypeScript project directory.
3. Compile the TypeScript files using `tsc`.
4. Run the compiled JavaScript files using `node`.

## Contributing

Contributions are welcome! If you have a new design pattern to add or improvements to existing implementations, feel free to fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
