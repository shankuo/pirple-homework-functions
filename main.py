"""
Title: Homework #2 Functions
Purpose: Using def / return statement to define a function. Based on the earlier 
homework #1 variable source code, adding functons to code that return 
the song attributes value

Syntax:

def functionName(parameter,..):
    code block 
    return

Best practices of function naming convention is using camelCase  
"""
# a song attribute and global scope variable
Artist="Dave Coz"
Genre="Jazz"
Album="Lucky Man"
Title="You Make Me Smile"
DurationSeconds= 250.8
Year=1993
BillBoard200 = False

# Purpose: Return artist song attribute value
def artist():
    ''' Takes no parameter, return a String value '''
    return Artist

# Purpose: Return genre song attribute value
def genre():
    ''' Takes no parameter, return a String value '''
    return Genre

# Purpose: album song attribute return
# Return : String
def album():
    ''' Takes no parameter, return a String value '''
    return Album

# Purpose: Return year song attribute value
def year():
    ''' Takes no parameter, return a Integer value '''
    return Year    

# Purpose: Return billboard song attribute value
# Return : Boolean
def billBoard200():
    ''' Takes no parameter, return a Boolean value '''
    return BillBoard200

# Main 
# Calling the functions by it functioName with print
print (artist())
print (genre())
print (album())
print (billBoard200())
