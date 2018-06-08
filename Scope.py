i = 42 # global variable

def someFunction():
    global i
    print("global i : " + str(i))
#    i = 41 # due to assignment becomes local
    i = 41
    print("local i : " + str(i))

someFunction()
print("global i : " + str(i))
    
    
