class Arrays:

    nums = [10,20,30,40,23]
    names = ["Amit","Eden","Ran"]
    new_nums = []

    var_0 = nums[0]
    var_1 = names[1]
    length_my_list = len(nums) # how to get the length of list
    before_last_exmaple_1 = nums[length_my_list-1] # how to get the last variable of list
    before_last_exmaple_2 = nums[-1:] # slicing exmaple
    example = nums[-2:]
    example_2 = nums [:2] #not including the 3rd value (shows 2 values)
    nums [2:]
    index = names.index("Eden")
    names.append("Shira")
    names.insert(1,"Aviv")
    names.remove("Aviv")
    names.insert(1,"Ronaldo")


    # example how to go over all list

    for name in names:
        print(f"My name is {name}")

    print("test end")

    for num in nums:
        new_num = num+5
        print(f'{new_num}')
        new_nums.append(new_num)

    tzioni = [1,2,"asd","asdasdasdga","n what"]
    print(tzioni[3])