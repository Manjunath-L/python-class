import re
email_id = r"^[a-zA-Z0-9._+%-]+@(gmail|yahoo|pentagonspace)(\.com|\.in)$"
mob_num = r"^(\+91[-\s]?|91[-\s]?)[6-9]\d{4}[-\s]?\d{5}$"
email = input("Enter your email: ")
mobile = input("Enter your mobile number: ")
if re.match(mob_num,mobile):
    print("Your mobile number is valid")
else:
    print("Your mobile number is not valid")
if re.match(email_id,email):
    print("Your email is valid")
else:
    print("Your email is not valid")