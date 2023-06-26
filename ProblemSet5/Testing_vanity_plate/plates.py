def main():
    plate = input("Plate: ")
    print(is_valid(plate) )


def is_valid(s):
    if (len(s) < 3 and len(s) > 6):
        return False
    if not(s[0:2].isalpha()):
        return False
    if not(s.isalnum()):
        return False
    endOfW = ''
    startOfD = ''
    for i in s:
        if i.isalpha():
            continue
        else:
            startOfD = i
            endOfW = s.index(i)
            break
    if endOfW == '':
        return True
    if not(s[endOfW:].isdigit()):
        return False
    if startOfD == '0' :
        return False
    return True
    



if __name__ == "__main__":
    main()