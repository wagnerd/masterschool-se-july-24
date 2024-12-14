
user_input = int(input("Which id: "))

# if user_input == 1:
#     print("")
# elif user_input == 2:

match user_input:
    case 1:
        print("1")
    case 2: 
        print("2")
    case 3 | 4:
        print("3 or 4")
    case _:
        raise ValueError("Wrong input!")