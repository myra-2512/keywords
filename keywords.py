a=str(input("Enter a string: "))
for i in a:
    if (i=='a'):
        print("a is found")
        break
else:
    print("a is not found")


#Activity 2

for x in range(10):
    if x%20==0:
        print("twist")
    elif x%15==0:
        pass
    elif x%5==0:
        print("fizz")
    elif x%3==0:
        print("buzz")
    else:
        print(x)


#Activity 3

var = 10

while var>0:
    var=var-1
    if var==5:
        continue
    print("Current variable value: ", var)
print("Good bye!")





















































































































































        