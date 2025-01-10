#sam tidmarsh
#simple calculator

#init
#func
#this function adds num1+num2 and prints results
def mult(num1, num2):#tells computer how to multiply and show answer
    result = num1 * num2
    print("The result is: "+str(result))
def div(num1, num2):#tells computer how to divide and show answer
    result = num1/num2
    print("The result is: "+str(result))
def sub(num1, num2):#tells computer how to subtract and show answer
    result = num1 - num2
    print("The result is: "+str(result))
def add(num1, num2):#tells computer how to add and show answer
    result = num1 + num2
    print("The result is: "+str(result))
def simpleCalc():
    print("Welcome Preschoolers to Simple Calculator")
    while True:
        print("Please choose an operation: ")#makes them pick which kind of calculator they want
        print("""1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Quit""")
        operation = int(input("(1-5) :"))#has them pick which operation by number
        if operation == 1:#for addition print
            add1=int(input("Enter the first number: "))
            add2=int(input("Enter the second number: "))
            add(add1,add2)
        if operation == 2:#subtraction and print
            sub1 = int(input("Enter the first number: "))
            sub2=int(input("Enter the second number: "))
            sub(sub1,sub2)
        if operation == 3:#multiply and print
            mult1 = int(input("Enter the first number: "))
            mult2=int(input("Enter the second number: "))
            mult(mult1,mult2)
        if operation == 4:#divide and print
            div1 = int(input("Enter the first number: "))
            div2=int(input("Enter the second number: "))
            div(div1,div2)
        if operation == 5:#if they're done
            print("Okay! Have a nice day!")
            break
#main
simpleCalc()
