#Write a python function to create and return a new dictionary from the given dictionary(item:price).
#Given the following input, create a new dictionary with elements having price more than 200.
#prices = {'ACME': 45.23,'AAPL': 612.78, 'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}

def create_new_dictionary(prices):
    #start writing your code here
    new_dict={}
    for key, val in prices.items():
        if val>20:
             new_dict[key]=val
    return new_dict
    

    
    return new_dict

prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))
