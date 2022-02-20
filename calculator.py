from ast import Pass
from cmd import PROMPT
from lib2to3.pgen2.token import NUMBER
from multiprocessing.sharedctypes import Value

def get_input():
    value = input(PROMPT)
    
def get_operator(PROMPT):
    PROMPT = 'Enter an Operator: '
    op = get_input(PROMPT)
    if op == ["+", "-", "*", "/"]:
        print("Operator")
        while op != ["+", "-", "*", "/"]:
            print("Invalid Operator")

def get_number(PROMPT):
    PROMPT = 'Enter number: '
    num = get_input()
    
def perform_operation(num2):
    op1 = get_operator()
    num1 = get_number()
    if op1 == "+":
        return num1 + num2
    elif op1 == "-":
        return num1 - num2
    elif op1 == "/":
        while num2 == 0:
            print("number not divisible by zero")
        return num1 / num2
    elif op1 == "*":
        return num1 * num2
    
     
def start_calculator():
    print("press 'q' to exit")
    num1 = get_number()
    return NUMBER


