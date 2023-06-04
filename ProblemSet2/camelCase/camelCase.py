def main():
    #prompt the user for input
    in_camel_case = input("CamelCase:")
    print("snake_case:", end= " ")
    to_snake_case(in_camel_case)

def to_snake_case(word):
    for i in range(len(word)):
        if word[i].isupper():
            print("_",(word[i]).lower(),end="", sep="")
        else:
            print(word[i], end="")
    
    
main()



    








