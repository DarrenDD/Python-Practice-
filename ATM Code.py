import babel.numbers

print("Welcome to ABC Bank\n\nInsert your card!")
balance = 10000.8
password = 1234
choice = 0

pin = int(input("Enter pin code: "))
if password == pin:
    
    while choice != 4:
        
        print("**** Menu ****")
        print("1 == balance")
        print("2 == deposit") 
        print("3 == withdraw")
        print("4 == cancel")
        
        choice = int(input("\nEnter your option\n"))
        
        if choice == 1:
            print(babel.numbers.format_currency( balance, "ZAR", locale='en_ZA'))
    
else:
    print("Pin incorrect")
    