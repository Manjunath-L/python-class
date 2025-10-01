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

# chack card condition
if card_inset == "yes":
    user_pin = int(input("Enter a 4 digit pin : "))

    # chack PIN condition
    if user_pin == pin:
        print("Select a language")
        print("1.English")
        print("2.Kannada")
        language_inp = int(input("Enter 1 or 2: "))

        # chack lan condition
        while True:
            if language_inp == 1:
                print("Select English")
                print("<============================>")
                print("Select Options")
                print("1.Withdraw")
                print("2.Deposit")
                print("3.Balance Enquiry")

                options_inp = int(input("Enter your option : "))

                # deposit option condition
                if options_inp == 2:
                    dep_amo = int(input("Enter a amount to deposit :  "))
                    bal = bal + dep_amo
                    print("Your balance after a deposit : ", bal)
                    break

                # chack option condition
                if options_inp == 1:
                    print("Enter type of account")
                    print("1.Saving account")
                    print("2.Current account")
                    account_typ = int(input("Enter your account type : "))

                    # chack account condition
                    if account_typ == 1:
                        amount = int(input("Enter a amount : "))
                        print("Please wait")
                        print("Collect your cash")
                        balance = str(input("Do you want to see balance (Yes/No) : "))

                        # chack balance condition
                        if balance == "yes":
                            print("Your balance amount : ", bal - amount)
                            con_user = str(
                                input("Do you want to continue ? (yes/no) : ")
                            )
                            if con_user == "yes":
                                continue
                            else:
                                print("Thank you visit again")
                                break
                    print("Thank you visit again")
    else:
        print("PIN Incorrect")
else:
    print("Wrong input try again")
