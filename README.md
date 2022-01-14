# Smart-Calculator-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/74

## Work on project. Stage 6/7: Variables
### Objectives

So, your program should support variables. Use ```dict``` to store them.

Go by the following rules for variables:

- We suppose that the name of a variable (identifier) can contain only Latin letters.
- A variable can have a name consisting of more than one letter.
- The case is also important; for example, n is not the same as **N**.
- The value can be an integer number or a value of another variable.
- It should be possible to set a new value to an existing variable.
- To print the value of a variable you should just type its name.

The example below shows how variables can be declared and displayed.

```shell
> n = 3
> m=4
> a  =   5
> b = a
> v=   7
> n =9
> count = 10
> a = 1
> a = 2
> a = 3
> a
3
```

Incorrect spelling or declaration of variables should also throw an exception with the corresponding message to the user:
- First, the variable is checked for correctness. If the user inputs an invalid variable name,
then the output should be ```"Invalid identifier"```.

```shell
> a2a
Invalid identifier
> n22
Invalid identifier
```

- If a variable is valid but not declared yet, the program should print ```"Unknown variable"```.

```shell
> a = 8
> b = c
Unknown variable
> e
Unknown variable
```

- If an identifier or value of a variable is invalid during variable declaration,
the program must print a message like the one below.

```shell
> a1 = 8
Invalid identifier
> n1 = a2a
Invalid identifier
> n = a2a
Invalid assignment
> a = 7 = 8
Invalid assignment
```

Please note that the program should print ```"Invalid identifier"``` if the left part of the assignment is incorrect.
If the part after the ```"="``` is wrong then use the "Invalid assignment". First we should check the left side.

Handle as many incorrect inputs as possible. The program must never throw an exception of any kind.

It is important to note, all variables must store their values between calculations of different expressions.

Do not forget about previously implemented commands: ```/help``` and ```/exit```.

#### Examples
The greater-than symbol followed by a space (>) represents the user input.

```shell
> a  =  3
> b= 4
> c =5
> a + b - c
2
> b - c + 4 - a
0
> a = 800
> a + b + c
809
> BIG = 9000
> BIG
9000
> big
Unknown variable
> /exit
Bye!
```
