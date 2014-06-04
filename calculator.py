import arithmetic

sym_list = ["+","-","*","/","pow","mod","square","cube"]
func_list = ["add", "subtract","multiply","divide","power","mod","square","cube"]

def symbol_to_function_call(symbol):
    sym_index = sym_list.index(symbol)
    function = func_list[sym_index]
    func_call = getattr(arithmetic, function)
    return func_call

def main():
    calculator_quit = False

    while calculator_quit == False:

        user_input = raw_input("> ")
        input_array = user_input.split(" ")

        first_sym = input_array[0]

        if first_sym in ["cube","square"]:
            func_call = symbol_to_function_call(first_sym)
            print func_call(int(input_array[1]))

        elif first_sym in sym_list:
            func_call = symbol_to_function_call(first_sym)
            value = func_call(int(input_array[1]), int(input_array[2]))

            if first_sym == "/":
                print "%.6f" %value
            else:
                print value

        elif user_input == 'q':
            calculator_quit = True
        else:
            print "unrecognized input"

if __name__ == "__main__":
    main()
