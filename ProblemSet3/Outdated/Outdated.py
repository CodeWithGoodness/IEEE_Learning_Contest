try:
    date_dict = {
        "January": "1",
        "February": "2",
        "March": "3",
        "April" : "4",
        "May" : "5",
        "June" : "6",
        "July" : "7",
        "August" : "8",
        "September" : "9",
        "October" : "10",
        "November" : "11",
        "December" : "12"
        }
    date = input("Date: ")
    seperators = [' ', '/', ',']

    for i in date:
        if i == '/':
            m, d, y = date.split(seperators[1])
        
        elif i == ' ':
            m, d, y = date.split(seperators[0]) 
            d = d.replace(",", "") 

    
    for x in date_dict:
        if m == x or m == date_dict[x]: 
            formatted_m= "{:0>2}".format(date_dict[x])
            formatted_d = "{:0>2}".format(d)
            formatted_y = "{:0>4}".format(y)
            
            print(formatted_y + "/" + formatted_m + "/" + formatted_d)
        
except ValueError:
    pass