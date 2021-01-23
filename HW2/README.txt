Jessica Pan -- jeypan@ucsc.edu
CSE 210A Programming Languages -- Winter 2021
Homework 2 -- WHILE interpreter

**NOTE: I used pyinstaller to create my executable. Make sure you have pyinstaller install before you run the test script, otherwise the test scripts don't work. I am also using the lark-parser library in python to create the AST of the WHILE interpreter, so make sure to have the lark-parser installed before running the test scripts.
    - To download pyinstaller: pip install pyinstaller
    - To download lark-parser: pip install lark-parser

**2nd Note: I wasn't able to run my test scripts on my local computer (windows) even though my script worked and my Makefile was correct. I tried using linux on a VM, UNIX Timeshare, and Ubuntu on my Windows computer but all platforms were unable to run my test script with my python script. I eventually had to run it on a mac to get my scripts to work.

In this assignment, we are to write an interpreter for the WHILE language. I've decided to use python again as my language of choice for this assignment. I'm still new to python and thought it would be fun and easier to code in python for this assignment.

I have 6 files to submit:
  - README.txt
  - Makefile
  - while.py
  - while.lark
  - testscriptoutput.pdf
  - myown.bats
  - log.txt
  
 *Make sure while.py, while.lark and Makefile are under the cse210A-asgtest/cse210A-asgtest-hw2-while/ directory before you run the test script. The 'myown.bats' also be under the cse210A-asgtest/cse210A-asgtest-hw2-while/tests directory.

README.txt:
  In this file, I will describe and explain the different files in my submission, along 
  with any issues I had in running my script.

Makefile:
  This file allows you to create the executable for my python script by using pyinstaller.
  To create the executable, do 'make'.
  To execute the python script, do './while'
  
  To run the test scripts on WHILE, do ./test.sh. This should run the different test cases on WHILE.

while.py:
    This file contains the interpreter for the AST of the WHILE language. This file takes 
    the input from the stdin and parses it with while.lark into an AST. Then creating a 
    state for each AST, we check for the statement's operation from the tree. Checking all 
    possible statement operations, we can move onto checking the next statements or 
    evaluaing the current statement. It then prints out all variables stored inside the state.

while.lark:
    This file parses the input from stdin into an AST. It checks if the input is a regular statement or a composite statement. If it's a regular statement, it'll check for a statement before the first semicolon (;), evaluate the statement and checks the next statement if it's a regular or composite statement again. If it's a composite statement, then it'll check for an if statement or a while statement. I've also listed the resources I used to create while.lark at the top of the file.

testscriptoutput.pdf:
  This is pdf contains a screenshot of the results of running the test scripts provided.

myown.bats:
  This is a bats file that contains my 5 test cases for the extra operator I implemented into my program (includes subtraction).

log.txt:
  This file is a log of the commits I made to my github.