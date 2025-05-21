a = 31  
t = type(a) # class <int> 

print(t)

b = 3.1  
t = type(b) # class <float>

print(t)

c = "31" 
t = type(c) # class <str>

print(t)

# now,
a = "31.2"
b = float(a) # a but type should be float
t = type(b)
print(t)