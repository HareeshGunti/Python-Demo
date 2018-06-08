def Div42ByWithHandling(divider):
    try:
        return 42 / divider
#    except ZeroDivisionError:
#        print("Error: tried divide by zero")
    except:
        print('Error')
        
def Div42By(divider):
    return 42 / divider

print(Div42ByWithHandling(2))
print(Div42ByWithHandling(21))
print(Div42ByWithHandling(0))
print(Div42ByWithHandling(7))

print(Div42By(2))
print(Div42By(21))
print(Div42By(0))
print(Div42By(7))

