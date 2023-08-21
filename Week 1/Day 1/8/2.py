# # Create variables of different data types and print them

a="Darshan"
A="Rana"

my_var="This is Variable"
# # also called snake case

x=10
y=5
print (a)
print (A)
print(my_var)

print (x)
print(y)
print (x+y)

# # not valid variables
# # 2myvar = "John"
# # my-var = "John"
# # my var = "John"

hiHELLO=" hiHELLO-THIS IS ONE TYPE OF VARIABLE"
print(hiHELLO)

# # assign multiple var at one time
p,q,r=1,2,3
print (p,r)

fruits=["apple","banana","graps"]
x,y,z=fruits
print (x)

# global variables
x="awesome"
def myfunc():
    print("Python is",x)
    
myfunc()    

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# supported data types in python
int
float
str
list
bool
x = 5
print(type(x)) 
