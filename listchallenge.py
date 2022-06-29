#!/usr/bin/env python3

import random

wordbank= ["indentation", "spaces"]
tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

def index_student():
    wordbank.append(4)

    num = input("Please input a number between 0-18: ")
    int_num = int(num)
    student_name = tlgstudents[int_num]

    print(f"{student_name} always uses {wordbank[-1]} {wordbank[1]} spaces to indent.")

def random_student():
    wordbank.append(4)
    student_name = random.choice(tlgstudents)

    print(f"{student_name} always uses {wordbank[-1]} {wordbank[1]} spaces to indent.")

def name_student():
    wordbank.append(4)
    student_name = input("Please enter a students name: ")
    
    print(f"{student_name} always uses {wordbank[-1]} {wordbank[1]} spaces to indent.")

#index_student()
#random_student()
name_student()
