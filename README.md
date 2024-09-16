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

| Access Modifier       | C# (Class Members)                                       | Java (Class Members)                                    | Python & TypeScript (Class Members)                                 |
| --------------------- | -------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------- |
| public                | Accessible from any code.                                | Accessible from any code.                               | Accessible from any code.                                           |
| private               | Accessible only within the same class.                   | Accessible only within the same class.                  | Python: Naming convention (e.g., \_var)                             |
| protected             | Accessible within the same class and derived classes.    | Accessible within the same class and derived classes.   | TypeScript: Accessible within the same class and derived classes.   |
| internal              | Accessible within the same assembly.                     | N/A                                                     | N/A                                                                 |
| protected internal    | Accessible within the same assembly and derived classes. | Accessible within the same package and derived classes. | TypeScript: Accessible within the same package and derived classes. |
| Default (No Modifier) | Private                                                  | Package-private (default)                               | Public                                                              |

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

## Prerequisites

Before setting up the project, ensure you have the following prerequisites installed:

### Runtime Version Manager

We recommend using [asdf](https://asdf-vm.com/) to manage runtime versions for different languages.

#### Installing asdf

For more details for detailed installation check [asdf Getting Started](https://asdf-vm.com/guide/getting-started.html)

#### macOS

You can install `asdf` using Homebrew:

1.  Install `asdf`:
    ```sh
    brew install asdf
    ```
2.  Add `asdf` to your shell:
    ```sh
    echo -e "\n. $(brew --prefix asdf)/libexec/asdf.sh" >> ~/.bash_profile
    source ~/.bash_profile
    ```

Now you can proceed with installing the required runtimes as described in the Prerequisites section./.bashrc

### .NET

Install .NET 7 and .NET 8 using asdf:

1. Add the .NET plugin:
```sh
asdf plugin-add dotnet-core https://github.com/emersonsoares/asdf-dotnet-core.git
````

2. Install .NET 7:
   ```sh
   asdf install dotnet-core 7.0.0
   asdf global dotnet-core 7.0.0
   ```
3. Install .NET 8:
   ```sh
   asdf install dotnet-core 8.0.0
   asdf global dotnet-core 8.0.0
   ```

### Java

Install Java using asdf:

1. Add the Java plugin:
   ```sh
   asdf plugin-add java https://github.com/halcyon/asdf-java.git
   ```
2. Install Java:
   ```sh
   asdf install java adoptopenjdk-11.0.11+9
   asdf global java adoptopenjdk-11.0.11+9
   ```

### Python

Install Python using asdf:

1. Add the Python plugin:
   ```sh
   asdf plugin-add python
   ```
2. Install Python:
   ```sh
   asdf install python 3.9.5
   asdf global python 3.9.5
   ```

### Go

Install Go using asdf:

1. Add the Go plugin:
   ```sh
   asdf plugin-add golang https://github.com/kennyp/asdf-golang.git
   ```
2. Install Go:
   ```sh
   asdf install golang 1.16.3
   asdf global golang 1.16.3
   ```

## Recommended VSCode Extensions

To enhance your development experience, consider installing the following Visual Studio Code extensions:

- **C#**: [C# for Visual Studio Code (powered by OmniSharp)](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp)
- **Java**: [Java Extension Pack](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack)
- **Kotlin**: [Kotlin Language](https://marketplace.visualstudio.com/items?itemName=mathiasfrohlich.Kotlin)
- **Python**: [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- **TypeScript**: [TypeScript and JavaScript Language Features](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-next)

These extensions provide language support, debugging capabilities, and other useful features to streamline your workflow.

## License

- **Code Runner**: [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)

This extension allows you to run code snippets or files for multiple languages, including C#, Java, Kotlin, Python, and TypeScript, directly within Visual Studio Code.

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
