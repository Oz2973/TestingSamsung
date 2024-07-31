class SevenBoom():
    for i in range(0, 50, 1):
        if (i % 7 == 0):
            print(f"Boom {i} by div")
            continue  # if you want to not have doubles have this continue enabled
        num_as_str = str(i)
        if (num_as_str.count("7") > 0):
            print(f"Boom {i} by count")
