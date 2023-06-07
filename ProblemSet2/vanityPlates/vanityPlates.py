# def main ():
#     plate = input("Plate: ")
#     if is_valid(plate):
#        print("Valid")
#     else:
#         print("Invalid")

# def is_valid(plate_number):
    
#     for i in plate_number:
#         if length(plate_number) == True:
#                 print(2)
#         if alpha(plate_number) == True:
#             print(1)
            
#                 if is_alphanumeric(plate_number) ==True:
#                     print(3)
#                     if plate_number[-1].isdigit() and plate_number[-1]!= "0":
#                         print(i,plate_number[-1])
#                         return True

    
        
          
# def alpha (p):
#     if p[0:2].isalpha():
#         return True
# def length(s):
#     if len(s) >=2 and len(s) <= 6:
#         return True
# def is_alphanumeric(n):
#     if all (i.isalnum() for i in n):
#         return True



# main()

def main(vn):
   
    if (len(vn) < 3 and len(vn) > 6):
        return False
    if not(vn[0:2].isalpha()):
        return False
    if not(vn.isalnum()):
        return False
    endOfW = ''
    startOfD = ''
    for i in vn:
        if i.isalpha():
            continue
        else:
            startOfD = i
            endOfW = vn.index(i)
            break
    if endOfW == '':
        return True
    if not(vn[endOfW:].isdigit()):
        return False
    if startOfD == '0' :
        return False
    return True

print(main(input("Plate: ")))

