Jessica Pan -- jeypan@ucsc.edu
CSE 210A Programming Languages -- Winter 2021
Homework 1 -- ARITH

**NOTE: I used pyinstaller to create my executable. Make sure you have pyinstaller install before you run the test script, otherwise the test scripts don't work.

**2nd Note: I wasn't able to run my test scripts on my local computer (windows) even though my script worked and my Makefile was correct. I tried using linux on a VM, UNIX Timeshare, and Ubuntu on my Windows computer but all platforms were unable to run my test script with my python script. I eventually had to run it on a mac to get my scripts to work.

In this assignment, we are to write an interpreter for the ARITH language. I've decided to use python as my language of choice for this assignment. I'm relatively new to python and thought it would be fun and easier to code in python for this assignment.

I have 6 files to submit:
  - README.txt
  - Makefile
  - arith.py
  - testscriptsoutput.pdf
  - myown.bats
  - log.txt
  
 *Make sure arith.py and Makefile are under the cse210A-asgtest/cse210A-asgtest-hw1-arith/ directory before you run the test script. The 'myown.bats' also be under the cse210A-asgtest/cse210A-asgtest-hw1-arith/tests directory.

README.txt:
  In this file, I will describe and explain the different files in my submission, along with any issues I had in running my script.

Makefile:
  This file allows you to create the executable for my python script by using pyinstaller.
  To create the executable, do 'make'.
  To execute the python script, do './arith'
  
  To run the test scripts on ARITH, do ./test.sh. This should run the different test cases on ARITH.

arith.py:
  This is file contains the code to the interpreter ARITH. In arith.py, the two main functions that do the interpreting of ARITH are 'parse' and 'eval'. The function 'parse' first declares the precedences of each operator by assigning it a number according to its priority.
      0 = lowest priority
      5 = highest priority
  We then tokenize the input from the stdin and convert the input into postfix notation. (e.g. 3 + 6 * 9  => 3 6 9 * + ) I'm using a list to sort and hold the prefix notation and a stack to store the operators in their proper order. The 'eval' function evaluates the postfix notation from 'parse'. As the eval function reads the postfix notation, it pushes the numbers it sees onto a stack. When it reaches an operator in the postfix notation, it pops the stack twice. Thus retrieving the two numbers to do the operation that 'eval' had just reached. To perform the operation on the 2 numbers, a function 'calc' is called to do the math. The value 'calc' produces is then pushed back onto the stack for the next time 'eval' reaches an operator. This process repeats, until the entire postfix notation is read, and eventually we can pop the last number in the stack for the result of our input.

testscriptsoutput.pdf:
  This is pdf contains a screenshot of the results of running the test scripts provided.

myown.bats:
  This is a bats file that contains my 5 test cases for the extra operator I implemented into my program (includes subtraction).

log.txt:
  This file is a log of the commits I made to my github.

