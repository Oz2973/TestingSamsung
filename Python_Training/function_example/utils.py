class utils:

    # example of function that gets parameters and returns variable

    def summary_calc(num1, num2):
        summary = num1 + num2
        print(f'Summary found the value is {summary}')
        if (summary > 0):
            print(f'The summary of {num1} and {num2} is positive')

            return summary

        # example of function that only gets the parameters

    def print_string(string_to_print):
        print(string_to_print)

    # example of function without parameters that does not return a variable
    def print_hello(self):
        print("Hello")

    def length_And_Print(count_And_Print):
        len_Of_Stuff = len (count_And_Print)
        print(f'Length of the text is {len_Of_Stuff}')
        return len_Of_Stuff

