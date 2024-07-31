class for_Loop_Quick_Math:
    for i in range(0, 110, 10):
        print(f'the value of i is {i}')

    for i in range(0, 110):
        print(f'the value of i is {i}')

    for i in range(110):
        print(f'the value of i is {i}')

    for i in range(0, 11):
        value = i * 10
        if (value==20):
            continue
        print(f"the value is {value}")

        if (value > 50):
            break

    print('Test end')
