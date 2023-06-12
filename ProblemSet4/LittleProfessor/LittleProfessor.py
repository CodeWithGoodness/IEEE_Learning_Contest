import random
is_correct_level = True
while True:
    try:    
        def main():
                level_input = get_level()
                generate_integer(level_input)
            
        def get_level():
            global is_correct_level
            while is_correct_level:
                user_level = int(input("Level: "))
                if user_level in range(1, 4):
                    is_correct_level = False
                    return user_level

                else:
                    continue

        def generate_integer(level):
            i = 0
            score = 0
            while i < 10:
                if int(level) == 1:                   
                    integer1= random.randint(1, 9)
                    integer2 = random.randint(1, 9)                  
                elif int(level) == 2:
                    integer1 = random.randint(10, 99)
                    integer2 = random.randint(10, 99)
                else:
                    integer1 = random.randint(100, 999)
                    integer2 = random.randint(100, 999)

                j = 0
                while j < 3:
                    answer = integer1 + integer2
                    print (integer1," +", integer2, " = ", end=" ")
                    user_ans = int(input())
                    if answer !=user_ans:
                        print("EEE")
                        j+=1
                        if j ==3:
                            print (f"{integer1} + {integer2} = {answer}")
                        else:
                            continue
                    else:
                        score += 1
                        break
                   
                i += 1
            
            print (int(score))
        if __name__ == "__main__":
            main()

    except ValueError:
        pass
    else:
        break




