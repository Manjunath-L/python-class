bal = 10000
pin = 1234

print(
    r"""
__        __   _                            _____          _  _____ __  __
\ \      / /__| | ___ ___  _ __ ___   ___  |_   _|__      / \|_   _|  \/  |
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \    / _ \ | | | |\/| |
  \ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) |  / ___ \| | | |  | |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|   |_|\___/  /_/   \_\_| |_|  |_|
"""
)

card_inset = str(input("Insert a card : "))

if card_inset == "yes":
    user_pin = int(input("Enter a 4 digit pin : "))
    if user_pin == pin:
        print("Select a language")
        print("1.English")
        print("2.Kannada")
        language_inp = int(input("Enter 1 or 2: "))

        if language_inp == 1:
            print("Select English")
            print("<============================>")
            print("Select Options")
            print("1.Withdraw")
            print("2.Deposit")
            print("3.Balance Enquiry")
            options_inp = int(input("Enter your option : "))
            if options_inp == 1:
                print("Enter type of account")
                print("1.Saving account")
                print("2.Current account")
                account_typ = int(input("Enter your account type : "))
                if account_typ == 1:
                    amount = int(input("Enter a amount : "))
                    print("Please wait")
                    print("Collect your cash")
                    balance = str(input("Do you want to see balance (Yes/No) : "))
                    if balance == "yes":
                        print("Your balance amount : " , bal - amount )
                        print("Thank you visit again")
                    print("Thank you visit again")

        else:
            print("We are working on both Deposit and Balance Enquiry ")
    else:
        print("We are working on it")

else:
        print("PIN Incorrect")
else:
    print("Wrong input try again")
