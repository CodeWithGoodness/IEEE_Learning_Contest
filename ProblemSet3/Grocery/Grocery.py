grocery_list = {}
try:
    while True:
        
        grocery_item = input("Item: ]")
        if grocery_item not in grocery_list:
            grocery_list[grocery_item] = 1
            
        else:
            grocery_list[grocery_item] += 1
            
    

            
except EOFError:
    for num, list in sorted(grocery_list.items()):
            print (f"{num} {list.upper()}")
            
        
            
                  