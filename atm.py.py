ID = int(input("Enter your id here: "))
Pin = int(input("Enter Your four digit pin:"))

if(ID == 9113) and (Pin == 8252):
    print("Welcome karan")
    Balance = 25000

    while True:
        print("\n--- ATM --- ")
        print("1 Check Balance")
        print("2 Deposit")
        print("3 Withdrawl")
        print("4 change Pin")
        print("5 Exit")

        choice = input("choose (1-4): ")

        if choice == "1":
            print("your Updated Balance: ", Balance)

        elif choice == "2":
            amount= int(input("Enter Your Amount: "))
            Balance = amount + Balance
            print("your Updated Balance: ", Balance)

        elif choice == "3":
            amount = int(input("Enter Your Amount: "))
            if amount<=Balance:
                Balance = Balance - amount
                print("Your updated Balance is : ", Balance)
            else:
                print("Low Balance")
        elif choice == "4":
            new_pin = int(input("Enter Your New pin: "))
            Pin = new_pin 
            print("Change sucess Fully")

        elif choice == "5":
            print("Thank you")
            break

        else:
            print("wrong choice")

else:
    print("Invalid ID or Pin")
        
           



    

        

    

    
    

    


        




        


        




    




     
       




