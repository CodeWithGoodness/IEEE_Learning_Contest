operation = input("Do some calculation : ").split()
num_1 = float(operation[0])
operator = operation[1]
num_2= float(operation[2])

match operator:
    case "+":
        print (num_1 + num_2)
    case "-":
        print (num_1 - num_2)
    case "*":
        print (num_1 * num_2)
    case "/":
        print (num_1 / num_2)
    case _:
        print ("recheck operator")
    

