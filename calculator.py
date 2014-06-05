import arithmetic

sym_list = ["+","-","*","/","pow","mod","square","cube"]
func_list = ["add", "subtract","multiply","divide","power","mod","square","cube"]

def symbol_to_function_call(symbol):
    sym_index = sym_list.index(symbol)
    function = func_list[sym_index]
    func_call = getattr(arithmetic, function)
    return func_call

def calculate():
    calculator_quit = False

    while not calculator_quit:

        user_input = raw_input("> ")
        input_array = user_input.split(" ")

        first_sym = input_array[0]

        if first_sym in ["cube","square"]:
            func_call = symbol_to_function_call(first_sym)
            print func_call(int(input_array[1]))

        elif first_sym == "/":
            if input_array[2] == "0":
                print "Cannot divide by 0"
            else:
                func_call = symbol_to_function_call(first_sym)
                value = func_call(int(input_array[1]), int(input_array[2]))
                print "%.6f" %value

        elif first_sym in sym_list:
            func_call = symbol_to_function_call(first_sym)
            value = func_call(int(input_array[1]), int(input_array[2]))
            print value

        elif user_input == 'q':
            calculator_quit = True
        else:
            print "Unrecognized input"

def main():
    calculate()

if __name__ == "__main__":
    main()
