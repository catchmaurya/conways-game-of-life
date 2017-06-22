#-------------------------------------------------------------------------------
# Name:        Validator
# Purpose:     Interview - ThoughtWorks
#
# Author:      Maurya
#
# Created:     01/10/2012
# Copyright:   No copyright
# Licence:     <No Licence>
#-------------------------------------------------------------------------------
"""
    This validator has the utils to validate:
    * integers
    * seeds
"""
def is_integer(value):
    return type(value) == type(1)
def is_seed(value):
    return value in ('-','*')

if __name__ == '__main__':
    # run the code as below
    print is_integer(23)
    print is_integer(2.3)
    print is_seed('*')
    print is_seed('0')
