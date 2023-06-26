from plates import is_valid


def test_length():
    assert is_valid("git98") == True
    assert is_valid("67glory45") == False
    assert is_valid("CS50") == True
    assert is_valid("CSO5") == True
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

    


# and len(s) > 6
#     assert (s[0:2].isalpha()):
        
#     assert (s.isalnum()):
       
#     endOfW = ''
#     startOfD = ''
#     for i in s:
#         if i.isalpha():
#             continue
#         else:
#             startOfD = i
#             endOfW = s.index(i)
#             break
#     if endOfW == '':
#         return True
#     if not(s[endOfW:].isdigit()):
#         return False
#     if startOfD == '0' :
#         return False