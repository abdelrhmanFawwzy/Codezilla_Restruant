# it is programe to order food
# dicts with the available items
pizzas = { "Margherita": 100,  "Pepperoni": 120, 
            "Meat Lovers": 150,  "Chicken": 130} 
burgers = {"Beef": 100, "Chicken": 80,
           "Bacon": 120 } 
drinks = {"Coke": 30,  "Sprite": 25, 
          "Fanta": 25, "Pepsi": 30 } 
soups = { "Chicken Soup": 50,  "Beef Soup": 60, 
          "Mushroom Soup": 40 } 
desserts = {"Ice Cream": 50,   "Chocolate Cake": 60, 
            "Cheese Cake": 70 }
# welcome message_1 listing the available items
message_1 = '''Welcome to Codezilla Restaurant
1. Pizaas
2. Burgers
3. Drinks
4. soups
5. Desserts'''
# message_2 for dealing with orders
message_2 = '''1. Add another item
2. View the order
3. clear the order
4. Exit'''
# intilizing dict for orders
orders = {}
# Loop until user press Enter
while True:
    print(message_1)
    # ask user for desierd item
    desierd_item = input("Please, Enter the number of item\
 you want (Enter to Exit): ")
    print("-"*60)
    # if choose 1
    if desierd_item == "1":
        # loop throgh pizaas dict
        # use enumerat for (num)
        for num, pizaa in enumerate(pizzas, 1):
            # print num. pizaa kind: price EGP
            print(f"{num}. {pizaa}: {pizzas[pizaa]} EGP")
        # ask user for item num, and 0 to return to main message
        item = int(input("Please, Enter the number of item\
 you want (0 to return to the previos menu): "))
        # if user choose 0
        if item == 0:
            continue
        else:
            # ask user for quantity
            quantity = input("Please, Enter the quantity: ")
             # get the item
            pizzas_lst = list(pizzas.keys())
            pizzas_price = list(pizzas.values())
            get_item = pizzas_lst[item-1]
            get_price = pizzas_price[item-1]
            # add order info to dict 
            orders.update({get_item:{"price":get_price, "quantity":quantity}})
            # show user  message_2
            print(message_2)
            choice = input("Please Enter you choice: ")
            # if choice 1
            if choice == "1":
                # return to the main loop
                continue
            # if choice 2
            if choice == "2":
                print("Your order is: ")
                print("-"*40)
                # loop through order dict 
                for order in orders:
                    # print 
                    print(f"Item: {order}") 
                    print(f"Price: {orders[order]["price"]}")
                    print(f"Quantity: {orders[order]["quantity"]}")
                
            # if choice 3
                # delete elment in order dict
            # if choice 4
                # Exit the program
    break      
        
            
        
        
    
    
    
    
   
        
    # if choose 2
    # if choose 3
    # if choose 4
    # if choose 5
    # if press Enter
    if desierd_item == "":
        break
