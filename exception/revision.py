while True:
    try:
        age = int(input("Enter your age: "))

        if age < 18:
            raise Exception("Not eligible to vote")

        print("Eligible to vote")
        break  # exit loop if valid

    except ValueError:
        print("Please enter numbers only")

    except Exception as e:
        print(e)
