def main():
    #prompt the user for input
    in_camel_case = input("CamelCase:")
    print("snake_case:", end= " ")
    to_snake_case(in_camel_case)

def to_snake_case(word):
    for i in range(len(word)):
        if word[i].isupper():
            print("_",(word[i]).lower(), end="")
        else:
            print(word[i], end="")
    i + 1
    
main()

    #if split_words.isUpper

    








