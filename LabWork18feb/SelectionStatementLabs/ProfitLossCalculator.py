#program to calculate profit an dloss based on cost price and selling price
#input of cost price 
cost_price = float(input("Enter the cost price (in rs): "))
#to validate cost price
if(cost_price <= 0):
    print("Invalid cost price")
    exit() #exiting the program if cost price is invalid
else:    
    #input of selling price
    selling_price = float(input("Enter the selling price (in rs): "))
    #to validate selling price
    if(selling_price <= 0):
        print("Invalid selling price")
        exit() #exiting the program if selling price is invalid
    else:
        #calculating profit or loss
        if(selling_price > cost_price):
            profit = selling_price - cost_price
            print("Profit:rs", profit)
        elif(selling_price < cost_price):
            loss = cost_price - selling_price
            print("Loss:rs", loss)
        else:
            print("No profit no loss")