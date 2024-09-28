binary_code = "00100100010100101001000010100000"
count = 1
for i in binary_code:
    if i == "1":
        if len(str(count)) != 2:
            print(f"0{count}. - {i}")
        else:
            print(f"{count}. - {i}")
    count += 1