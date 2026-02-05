# Activity Python 5: Task 1
# File: ACT_Python_HeaderTemplate_UCusername.py
# Date: 04 Feb 2026
# By: Avaneesh Kad
# Section: 001
#
# ELECTRONIC SIGNATURE
# Avaneesh Kad
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for
# all your python files the rest of the semester.
# If you used any resources to complete this assignment (including but # not
#limited to AI, homework help sites, other students, tutors)
# please give credit here: None
# Resources used. note: if you used an AI please site which AI program you used.


# Import libraries because its a good practice
import math

#Pseudocode:-
#start with defining the function name
#input a1, b1, c1, a2, b2, and c2 , so 6 input arguments
#now to determine whether its an input function or not, use 'if' and (a1*b2)-(a2*b1) != 0
#if its not unique out the statement 'The function is not unique'
#and set the values of x and y as -9999
#BUT
#Iff the unique is true, find the values of x and y 
# x = c1b2-c2b1  /  a1b2-a2b1
# y = c2a1-c1a2  /  b2a1-b1a2
#in the last return (x, y)

def Algebra(a1, b1, c1, a2, b2, c2):
    if ((a1 * b2) - (a2 * b1)) == 0:
        print("The function does any unique solutions")
        x = -9999
        y = -9999
    else:
        x = ((c1 * b2) - (c2 * b1)) / ((a1 * b2) - (a2 * b1))
        y = ((c2 * a1) - (c1 * a2)) / ((a1 * b2) - (a2 * b1))

    return x, y


#To run the function 
#go to cd /ENED/HW_04Feb 
#go to the python terminal
#type 'import Algebra'
#thenn input the info we have
# A = Algebra.Algebra(1, 2, 1, 4, 5, 1)
#print(A)
