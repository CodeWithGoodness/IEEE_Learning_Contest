grocery_list = {}
try:
    while True:
        
        grocery_item = input("Item: ")
        if grocery_item not in grocery_list:
            grocery_list[grocery_item] = 1
            
        else:
            grocery_list[grocery_item] += 1
            
    

            
except EOFError:
    for list_name, count in sorted(grocery_list.items()):
            print (f"{count} {list_name.upper()}")
            
        
            
                  