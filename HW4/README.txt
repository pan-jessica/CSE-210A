Jessica Pan -- jeypan@ucsc.edu
CSE 210A Programming Languages -- Winter 2021
Homework 4 -- WHILE-SS interpreter

**NOTE: I used pyinstaller to create my executable. Make sure you have pyinstaller install before you run the test script, otherwise the test scripts don't work. I am also using the lark-parser library in python to create the AST of the WHILE interpreter, so make sure to have the lark-parser installed before running the test scripts.
    - To download pyinstaller: pip install pyinstaller
    - To download lark-parser: pip install lark-parser

**2nd Note: I wasn't able to run my test scripts on my local computer (windows) even though my script worked and my Makefile was correct. I tried using linux on a VM, UNIX Timeshare, and Ubuntu on my Windows computer but all platforms were unable to run my test script with my python script. I eventually had to run it on a mac to get my scripts to work.

In this assignment, we are to write an interpreter for the WHILE language and produce the small steps of each command. I've decided to use python again as my language of choice for this assignment. I'm still new to python and thought it would be fun and easier to code in python for this assignment.

I have 8 files to submit:
  - README.txt
  - Makefile
  - while-ss.py
  - ssprint.py
  - while.lark
  - testscriptoutput.pdf
  - myown.bats
  - log.txt
  
 *Make sure while-ss.py, ssprint.py, while.lark and Makefile are under the cse210A-asgtest/cse210A-asgtest-hw4-whiless/ directory before you run the test script. The 'myown.bats' also be under the cse210A-asgtest/cse210A-asgtest-hw4-whiless/tests directory.

To create the executable: make
To run executable: ./while-ss
To run test scripts: ./test.sh
