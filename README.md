[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ktyD1gKg)

# Project made by: Laura Ortiz Usme & Miguel Ángel Salgar Olarte

## Versions of OS, Programming Language and Tools Used
* ***Operative System:*** **Windows 11 Home Version 23H2**
* ***Programming Language Used:*** **Python 3.11**
* ***Tools Used in the Implementation:*** **No external libraries were used, code was inspired by [Geeks For Geeks](https://www.geeksforgeeks.org/cocke-younger-kasami-cyk-algorithm/)**

## Instructions to run the program
Using a python IDE you can open the main.py file and click on the run button, or alternatively, by using the CMD you can type py main.py to start running the program.
The program won't give an immediate response but it will wait patiently for user input, the input instructions are as follows:
1. An integer for the total number of grammars to be analyzed
2. Two integers (separated by a space), the first integer is the number of rules the grammar has, the second one is the number of strings to process
3. The rules of the grammar, this step is repeated as many times as the **first** integer in step 2 dictates.
4. A chain to be analyzed, this step is repeated as many times as the **second** integer in step 2 dictates. The program will automatically reply yes or no to each chain entered
5. If the integer in the first step is above 1, repeat step 2 onwards until the program finishes. The program will finish once it has exhausted the number of grammars stipulated in step 1
