userName = input("Enter your name: ")
userBirthDate = int(input("Enter your birth year: "))
userTotalBalance = int(input("Enter your total balance: "))
youWantToBeMember = input("Do you want to be a member (yes/no): ").lower()
userAge = 2024 - userBirthDate
if(youWantToBeMember == "yes"):  
    getUserMembershipType = input("Enter your membership (gold, silver): if you want gold membership then charge RS 500 and if you want silver membership then charge RS 300: ").lower()
    if(userTotalBalance < 1000):
        print("You have not enough balance!! Please Update your balance")
    else:
        if(getUserMembershipType == "gold"):
            print("Welcome" + userName + " , your membership is " + getUserMembershipType + " . we charge Rs 500")
            print("Your total balance is " + str(userTotalBalance - 500))
            userTotalBalance = userTotalBalance - 500
        elif(getUserMembershipType == "silver"):
            print("Welcome" + userName + " , your membership is " + getUserMembershipType + " . we chargeed Rs 300") 
            print("Your total balance is " + str(userTotalBalance - 300))  
            userTotalBalance = userTotalBalance - 300 
        else:
            print("Invalid membership type entered.! Plese try again")     
else:
    print("Welcome" + userName + " , you are not a member. but you can join if you want any Product" )

youWantShoping = input("Do you want to shop (yes/no): ").lower()
if(youWantShoping == "yes"):
     print("which product you want to buy?   We give yoy discount for your Age and Membership")
     print("We have the following products \n 1. Shirt \n 2. Pants \n 3. Watch \n 4. Mobile    ")
     print("All product prices are Rs 800 each")
     getUserMembershipType = input("Show your membership (gold, silver or none): ").lower()
     if(getUserMembershipType == "gold"):
      print("You have a 30% discount")
      userFinalBalance = userTotalBalance - (userTotalBalance * 0.3)
      print("Your final balance is " + str(userFinalBalance))
     elif(getUserMembershipType == "silver" and userAge >= 60):
      print("You have a 25% discount")
      userFinalBalance = userTotalBalance - (userTotalBalance * 0.25)
      print("Your final balance is " + str(userFinalBalance))
     elif(getUserMembershipType == "silver" and userAge < 60):
      print("You have a 20% discount")
      userFinalBalance = userTotalBalance - (userTotalBalance * 0.2)
      print("Your final balance is " + str(userFinalBalance))
     elif(getUserMembershipType == "none"):
      print("You have a 5% discount")
      userFinalBalance = userTotalBalance - (userTotalBalance * 0.05)
      print("Your final balance is " + str(userFinalBalance))
     else:
      print("You have a 5% discount")
      userFinalBalance = userTotalBalance - (userTotalBalance * 0.05)
      print("Your final balance is " + str(userFinalBalance))

else:
    print("Welcome " + userName + " , you can not shop now! phari Phari aaudai garnu la Maya Na marnu")

 