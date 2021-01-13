Jessica Pan -- jeypan@ucsc.edu
CSE 210A Programming Languages -- Winter 2021
Homework 1 -- ARITH


In this assignment, we are to write an interpreter for the ARITH language. I've decided to python as my language of choice for this assignment. I'm relatively new to python and thought it would be fun to code in python for this assignment.

I have 5 files to submit:
  - README.txt
  - Makefile
  - arith.py
  - stack.py

README.txt:
  In this file, I will describe and explain the different files in my submission.

Makefile:
  This file allows you to run my python code for ARITH.
  To run arith.py, you can type 'make' to run my file.

arith.py:
  This is file contains the code to the interpreter ARITH. In arith.py, the two main functions that do the interpreting of ARITH are 'parse' and 'eval'. The function 'parse' first declares the precedences of each operator by assigning it a number according to its priority.
      0 = lowest priority
      5 = highest priority
  We then tokenize the input from the stdin and convert the input into postfix notation. (e.g. 3 + 6 * 9  => 3 6 9 * + ) I'm using a list to sort the prefix notation and a stack to store the operators