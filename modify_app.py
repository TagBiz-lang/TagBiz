user_fund = 0
total_amount = 0
price = 0
item_in_the_cart =[]

def Tagbiz():
    global user_fund,total_amount,item_in_the_cart,price
    TagBiz = {}
    TagBiz["Ladies_wears"]=["top","skirt","polo"]
    TagBiz["Electronics"]=["kettle","stove","iron","lamp","bulb"]
    TagBiz["Babies_wears"]=["socks","tissue","feeder"]
    TagBiz["Men_wears"]=["shirt","trouser","sniker"]
    TagBiz["Ladies_wears_prices"]=[2000,1000,5000]
    TagBiz["Electronic_prices"]=[5000,1800,7000,1200,900]
    TagBiz["Babies_wears_prices"]=[1500,3000,5000]
    TagBiz["Men_wears_prices"]=[4000,7000,20000]
    
    order = int(input("Select the department you want to shop from\n1. Ladies_wears\n2. Electronics\n3. Babies_wears\n4. Men_wears\n"))
    if order == 1:
        print("Welcome to TagBiz Ladies_wears store\n")
        input_order = input(" What would you like to buy from us?\n")
        for order in TagBiz["Ladies_wears"]:
            if input_order == order:
                if  order == TagBiz["Ladies_wears"][0]:
                    price = TagBiz["Ladies_wears_prices"][0]
                    if user_fund>= 5:
                            total_amount = total_amount + price
                            user_fund = user_fund - price
                            item_in_the_cart.append(TagBiz["Ladies_wears"][0])
                            return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))  
                elif order == TagBiz["Ladies_wears"][1]:
                    price = TagBiz["Ladies_wears_prices"][1]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Ladies_wears"][1])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))  

                elif  order == TagBiz["Ladies_wears"][2]:
                    price = TagBiz["Ladies_wears_prices"][2]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Ladies_wears"][2])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))  

                elif  order == TagBiz["Ladies_wears"][3]:
                    price = TagBiz["Ladies_wears_prices"][3]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Ladies_wears"][3])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))  

                elif  order == TagBiz["Ladies_wears"][4]:
                    price = TagBiz["Ladies_wears_prices"][4]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Ladies_wears"][4])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))  

            print("Succesfully added to the cart")
            total_amount = total_amount + price
            print("The total amount in your cart is:", total_amount )
            break
        else:
                print("out of stock")
    elif order == 2:
        print("Welcome to TagBiz Electronics store\n")
        input_order = input(" What would you like to buy from us?\n")
        for order in TagBiz["Electronics"]:
            if input_order == order:
                if  order == TagBiz["Electronics"][0]:
                    price = TagBiz["Electronic_prices"][0]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Electronics"][0])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))  

                elif order == TagBiz["Electronics"][1]:
                    price = TagBiz["Electronic_prices"][1]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Electronics"][1])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))  

                elif  order == TagBiz["Electronicss"][2]:
                    price = TagBiz["Electronic_prices"][2]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Electronics"][2])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))  

                elif  order == TagBiz["Electronics"][3]:
                    price = TagBiz["Electronic_prices"][3]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Electronics"][3])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))  

                elif  order == TagBiz["Electronics"][4]:
                    price = TagBiz["Electronic_prices"][4]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Electronics"][4])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))  

                print("Succesfully added to the cart")
                total_amount = total_amount + price
                print("The total amount in your cart is:", total_amount )
                break
            else:
                print("out of stock")
                
    elif order == 3:
        print("Welcome to TagBiz Babies_wears store\n")
        input_order = input(" What would you like to buy from us?\n")
        for order in TagBiz["Babies_wears"]:
            if input_order ==order:
                 if  order == TagBiz["Babies_wears"][0]:
                    price = TagBiz["Babies_wears_prices"][0]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Babies_wears"][0])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))          
                 elif order == TagBiz["Babies_wears"][1]:
                    price = TagBiz["Babies_wears_prices"][1]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Babies_wears"][1])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))             
    
                 elif  order == TagBiz["Babies_wears"][2]:
                    price = TagBiz["Babies_wears_prices"][2]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Babies_wears"][2])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))  
                 elif  order == TagBiz["Babies_wears"][3]:
                    price = TagBiz["Babies_wears_prices"][3]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Babies_wears"][3])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))        
    
                 elif  order == TagBiz["Babies_wears"][4]:
                    price = TagBiz["Babies_wears_prices"][4]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Babies_wears"][4])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))  
                 print("Succesfully added to the cart")
                 total_amount = total_amount + price
                 print("The total amount in your cart is:", total_amount )
                 break
            else:
                print("out of stock")


    elif order == 4:
        print("Welcome to TagBiz Men_wears store\n")
        input_order = input(" What would you like to buy from us?\n")
        for order in TagBiz["Men_wears"]:
            if input_order ==order:
             if  order == TagBiz["Men_wears"][0]:
                    price = TagBiz["Men_wears_prices"][0]
                    if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Men_wears"][0])
                        return user_fund,total_amount, item_in_the_cart
                    else:
                        print("Sorry, you have insuffient fund in your wallet\n")
                        user_fund = int(input("Please fund your wallet: ")) 
                        with open("file.txt","a") as file:
                            file.write(str(user_fund))       
            elif order == TagBiz["Men_wears"][1]:
                price = TagBiz["Men_wears_prices"][1]
                if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Men_wears"][0])
                        return user_fund,total_amount, item_in_the_cart
                else:
                    print("Sorry, you have insuffient fund in your wallet\n")
                    user_fund = int(input("Please fund your wallet: ")) 
                    with open("file.txt","a") as file:
                        file.write(str(user_fund))  
            elif  order == TagBiz["Men_wears"][2]:
                price = TagBiz["Men_wears_prices"][2]
                if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Men_wears"][0])
                        return user_fund,total_amount, item_in_the_cart
                else:
                    print("Sorry, you have insuffient fund in your wallet\n")
                    user_fund = int(input("Please fund your wallet: ")) 
                    with open("file.txt","a") as file:
                        file.write(str(user_fund))  
            elif  order == TagBiz["Men_wears"][3]:
                price = TagBiz["Men_wears_prices"][3]
                if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Men_wears"][0])
                        return user_fund,total_amount, item_in_the_cart
                else:
                    print("Sorry, you have insuffient fund in your wallet\n")
                    user_fund = int(input("Please fund your wallet: ")) 
                    with open("file.txt","a") as file:
                        file.write(str(user_fund))  
            elif  order == TagBiz["Men_wears"][4]:
                price = TagBiz["Men_wears_prices"][4]
                if user_fund>= price:
                        total_amount = total_amount + price
                        user_fund = user_fund - price
                        item_in_the_cart.append(TagBiz["Men_wears"][0])
                        return user_fund,total_amount, item_in_the_cart
                else:
                    print("Sorry, you have insuffient fund in your wallet\n")
                    user_fund = int(input("Please fund your wallet: ")) 
                    with open("file.txt","a") as file:
                        file.write(str(user_fund))  
                print("Succesfully added to the cart")
                
                total_amount = total_amount + price
                print("The total amount in your cart is:", total_amount )
                break
            else:
                print("out of stock")
    else:
        print("You are in a wrong store")
    while user_fund >= 1:
        user_fund,total_amount,cart = Tagbiz()
        print(f"your remaining balance is {user_fund} and the total sum of your purchase is {total_amount}.\n The item in your cart is {cart} ")
        optional_order = input("Do you want to continue shopping?")
        if optional_order.lower() == "yes":
            Tagbiz()
        else:
            print("Thank you for shopping with TagBiz, hopping to see you again")
            break

def user_login():
    username = ""
    user_password = ""
    actual_email = ""
    actual_password = ""
    email_password = ""
   
    print("\n\t\t\t******************SIGN IN PAGE*******************************")
    welcome_message = "\nWelcome to the homepage of Tagbiz!"
   
    username = input("Enter your username: ")
   
   
    with open("data_file.txt", "r", encoding="UTF-8") as file:
        for element in file:
            if username in element:
                email_password = element
                break  # Stop looping once we find the user
   
    # The program should split email and password only if email_password is found
    if email_password:
        actual_email, actual_password = email_password.strip().split(sep="|")
        if username == actual_email:
            user_password = input("Enter your password: ")
            if user_password == actual_password:
                print(welcome_message)
            else:
                print("The password you entered is not associated with that username. Kindly check the password and try again!")
                exit()
        else:
            print("sorry, this email not found in the database")
            exit()
    else:
        print("Either the username is incorrect or does not exist. Kindly check your username and try again!")
        return  # This return statement causes the program to exit the function since user not found

   
    Tagbiz()

def sign_up():
    import string as special
    full_name = ""
    address = ""
    phone_number = ""
    age = 0
    account_number = ""
    bank = ""
    username = ""
    password = ""
    valid_extensions = ["@gmail.com", "@yahoo.com", "@bing.com", "@outlook.com"]
    password_length = 0
    uppercase_count = 0
    lowercase_count = 0
    special_char_count = 0
    numbers_count = 0
    email_confirm_checker = ""
   
    print("Welcome to Tagbiz Store!, Perfect place for your classy shopping\n")
   
    full_name = input("Enter your full name: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")
    age = int(input("Enter your age (numbers only): "))
    username = input("Enter a valid email address: ")
    with open("data_file.txt","r") as email_checker:
        for line in email_checker:
            if username in line:
                print("This email address has already been taken")
                exit()
    for extension in valid_extensions:
        if extension in username:
            password = input("Create a password: ")          
            password_length = len(password)
           
            if password_length >= 8:
                uppercase_count = sum(1 for char in password if char.isupper())
                lowercase_count = sum(1 for char in password if char.islower())
                numbers_count = sum(1 for char in password if char.isdigit())
                special_char_count = sum(1 for char in password if char in special.punctuation)
               
                if uppercase_count >= 1 and lowercase_count >= 1 and numbers_count >= 1 and special_char_count >= 1:
                    print("Your account is now active! Please wait while we redirect you to the sign-in page")
                    email_password = username + "|" + password + "\n"
                    with open("data_file.txt", "a", encoding="UTF-8") as file:
                        file.write(email_password)
                   
                    user_login()
                else:
                    print("Password must contain at least one uppercase, lowercase, number, and special character!")
            else:
                print("Password must be at least 8 characters in length!")
            break
    else:
        print("Please enter a valid email address to continue!")
sign_up()