import arithmetic

def main():
    calculator_quit = False
    while calculator_quit == False:
        user_input = raw_input("> ")
        input_array = user_input.split(" ")
        if input_array[0] == "+":
            print arithmetic.add(int(input_array[1]),int(input_array[2]))
        elif user_input == 'q':
            calculator_quit = True
        else:
            print "unrecognized input"

if __name__ == "__main__":
    main()
