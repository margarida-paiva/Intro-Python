#program that prompts the user to insert a coin to pay for a 50 cent coke

a=50 #Amount owed

#Program to handle payment
while a>0:
    print("Amount Due:",a)
    c=int(input("Insert Coin: "))

    #Checks if the coin is valid
    if c==25 or c==10 or c==5:
        #Gives the remain
        a-=c
    else:
        print("Invalid coin")
        
print("Change Owed:",abs(a))