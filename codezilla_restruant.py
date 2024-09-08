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
message_1 = '''1. Pizaas
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
# intilizing list for Total
toatl = []

# -------------------------------------------------------------------
# print this message once
print("Welcom to codeizlla resturant")
# Loop until user press Enter
while True:
    print(message_1)
    # ask user for desierd item
    desierd_item = input("Please, Enter the number of item\
 you want (Enter to Exit): ")
    print("-"*60)
    # if choose 1 (pizaas)
    if desierd_item == "1":
        # confirm category (pizaas)
        category = pizzas
        order_type = "pizza"
        max_option = len(pizzas)
        # loop throgh pizaas dict
        # use enumerat for (num)
        for num, cat in enumerate(category, 1):
            # print num. pizaa kind: price EGP
            print(f"{num}. {cat}: {category[cat]} EGP")
        
    # elif choose 2 (burgers)
    elif desierd_item == "2":
        # confirm category (burgers)
        category = burgers
        order_type = "burger"
        max_option = len(burgers)
        # loop throgh burgers dict
        # use enumerat for (num)
        for num, cat in enumerate(category, 1):
            # print num. burgers kind: price EGP
            print(f"{num}. {cat}: {category[cat]} EGP")
        
    # elif choose 3 (Drinks)
    elif desierd_item == "3":
        # confirm category (drinks)
        category = drinks
        order_type = "drink"
        max_option = len(drinks)
        # loop throgh drinks dict
        # use enumerat for (num)
        for num, cat in enumerate(category, 1):
            # print num. drinks kind: price EGP
            print(f"{num}. {cat}: {category[cat]} EGP")
    # elif choose 4 (soups)
    elif desierd_item == "4":
        # confirm category (soups)
        category = soups
        order_type = "soup"
        max_option = len(soups)
        # loop throgh soups dict
        # use enumerat for (num)
        for num, cat in enumerate(category, 1):
            # print num. soups kind: price EGP
            print(f"{num}. {cat}: {category[cat]} EGP")
    # elif choose 5 (desserts)
    elif desierd_item == "5":
        # confirm category (desserts)
        category = desserts
        order_type = "dessert"
        max_option = len(desserts)
        # loop throgh desserts dict
        # use enumerat for (num)
        for num, cat in enumerate(category, 1):
            # print num. desserts kind: price EGP
            print(f"{num}. {cat}: {category[cat]} EGP")
    # elif press Enter
    elif desierd_item == "":
        break
    else :
        print("Invalid option")
        continue
       
    # ask user for item num, and 0 to return to main message
    item = int(input("Please, Enter the number of item\
you want (0 to return to the previos menu): "))   
    # if user choose 0
    if item == 0:
        continue
    else:
        if item <= max_option:
            # ask user for quantity
            quantity = int(input("Please, Enter the quantity: "))
            # get the item info (name,price,total price)
            cat_lst = list(category.keys())
            cat_price = list(category.values())
            get_item = cat_lst[item-1]
            get_price = cat_price[item-1]
            cat_total = quantity * get_price
            # add order info to dict 
            orders.update({get_item:{"price":get_price,
            "quantity":quantity,"cat_total":cat_total,
            "order type": order_type}})
            toatl.append(cat_total)
        else:
            print("Invalid option")
            continue

    # show user  message_2
    print(message_2)
    choice = input("Please Enter you choice: ")
    # if choice 1 (Add another item)
    if choice == "1":
        # return to the main loop
         continue
    # if choice 2 (view the order and return to main menu)
    elif choice == "2":
        print("-"*40)
        print("Your order is: ")
        print("-"*40)
        # loop through order dict 
        for order in orders:
            # print 
            print(f"Item: {order} {orders[order]["order type"]}") 
            print(f"Price: {orders[order]["price"]:.2f} EGP")
            print(f"Quantity: {orders[order]["quantity"]} units")
            print("-"*20)
            print(f"Item total:{orders[order]["cat_total"]:.2f} EGP")
            print("-"*40)
        print(f"Total: {sum(toatl):,.2f} EGP")
              
    # elif choice 3 (clear the order)
    elif choice == "3":
        # clear all orders data
        orders.clear()
        # cleal the total
        toatl.clear()
        # ptint order cleared
        print("Order Cleared")
    # if choice 4 (Exit )
    elif choice == "4":
    # Exit the program
        break      
    else :
         print("Invalid option")
         continue


# at the end of the programe print order info  
print("-"*40)
print("Your order is: ")
print("-"*40)
# loop through order dict 

for order in orders:
   # print 
    print(f"Item: {order}") 
    print(f"Price: {orders[order]["price"]:.2f} EGP")
    print(f"Quantity: {orders[order]["quantity"]} units")
    print("-"*20)
    print(f"Item total:{orders[order]["cat_total"]:.2f} EGP")
    print("-"*40)
print(f"Total: {sum(toatl):,.2f} EGP")
                  
        
        
    
    
    
    
   
        
   