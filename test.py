from christopher import Christopher

christopher = Christopher()

christopher.self_introduction()

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye christopher" or user_input.lower() == "quit" or user_input.lower() == "exit":
        break
    
    christopher.add_input("user", user_input)
    print("Christopher: ", end="")
    christopher.print_output()
    
