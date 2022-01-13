# Smart-Calculator-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/74

## Work on project. Stage 5/7: Error_
### Objectives

- The program should print ```Invalid expression``` in cases when the given expression has an invalid format. 
If a user enters an invalid command, the program must print ```Unknown command```. 
All messages must be printed without quotes. The program must never throw an exception.
- To handle incorrect input, you should remember that the user input that starts with ```/``` is a command,
in other situations, it is an expression.
- Do not forget to write methods to decompose your program.
- Like before, ```/help``` command should print information about your program. When the command ```/exit``` is entered,
the program must print ```Bye!```, and then stop.



#### Examples
The greater-than symbol followed by a space (>) represents the user input.

```shell
> 8 + 7 - 4
11
> abc
Invalid expression
> 123+
Invalid expression
> +15
15
> 18 22
Invalid expression

> -22
-22
> 22-
Invalid expression
> /go
Unknown command
> /exit
Bye!
```
