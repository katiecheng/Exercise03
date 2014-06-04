import arithmetic

def main():
    calculator_quit = False

    while calculator_quit == False:

        user_input = raw_input("> ")
        input_array = user_input.split(" ")

        sym_list_2var = ["+","-","*","/","pow","mod"]
        func_list_2var = ["add", "subtract","multiply","divide","power","mod"]
        sym_list_1var = ["square","cube"]

        first_sym = input_array[0]

        if first_sym in sym_list_2var:
            sym_index = sym_list_2var.index(first_sym)
            func = func_list_2var[sym_index]
            func_call = getattr(arithmetic, func)
            value = func_call(int(input_array[1]), int(input_array[2]))

            if first_sym == "/":
                print "%.6f" %value
            else:
                print value

        elif first_sym in sym_list_1var:
            sym_index = sym_list_1var.index(first_sym)
            func = sym_list_1var[sym_index]
            func_call = getattr(arithmetic, func)
            print func_call(int(input_array[1]))

        elif user_input == 'q':
            calculator_quit = True
        else:
            print "unrecognized input"

if __name__ == "__main__":
    main()
