class StringSlices():
    string_for_demo = 'Hello world'
    slice_from_begin = string_for_demo[:5]
    print (slice_from_begin)

    slice_to_end = string_for_demo[5:]
    print(slice_to_end)

    slice_middle=string_for_demo[5:7]
    print(slice_middle)
    slice_to_end_1=string_for_demo[-3:]
    print(slice_to_end_1)

    index = string_for_demo.index(" ")
    #can only see this result in debug mode
    slice_index_exampole = string_for_demo[index:5]
    #index is a variable that equals to space
    counter_i=string_for_demo.count("o") #count the number of "o" into string_for_Demo
    sub="world"
    is_into="world"
    is_num=string_for_demo.isalnum()
    #booelan true or false checks if it contains ONLY numbers
    string_for_demo.replace("hello","hi")
    print(string_for_demo)
    #replace changes things in the variable, changes from now on (like JavaScript)
    print ('test end')