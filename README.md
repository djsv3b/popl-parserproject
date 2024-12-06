# PoPL Parser Project Deliverable 1
Aden Landy, Andrea Fratila, Danny Saab
FS24

## Set Up
Use the included antlr4 jar and follow the instructions [here](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md) to install and setup antlr. Make sure you also have at least Java version 11 installed.

##Instructions
First, run the command to generate the tokens for the grammar:
> antlr4 -Dlanguage=Python3 popl_project.g4 

Next, open the popl_project.py file and replace the input_code with the code to be parsed.
Finally, run the program to parse the code.