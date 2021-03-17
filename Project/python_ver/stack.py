#!/usr/bin/env python

'''
    Jessica Pan -- jeypan@ucsc.edu
    CSE 210A Programming Languages -- Winter 2021
    Project -- Basic Calculator
'''


class Stack:

    def __init__(self):
        self.stack = []

    def peek(self):
        if self.stack:
            return self.stack[-1]  # last element of stack
        else:
            return None  # stack's empty

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def isEmpty(self):
        return self.stack == []
