with open("input.txt") as f:
    raw_input = f.read()

total = 0

enable = True
for index in range(0, len(raw_input)):
    element = raw_input[index]

    if element == "d" and  raw_input[index+1] == "o" and raw_input[index+2] == "n" and raw_input[index+3] == "'" and raw_input[index+4] == "t" and raw_input[index+5] == "(" and raw_input[index+6] == ")":
        enable = False
    if element == "d" and raw_input[index + 1] == "o" and raw_input[index + 2] == "(" and raw_input[index+3] == ")":
        enable = True

    if element == "m" and  raw_input[index+1] == "u" and raw_input[index+2] == "l" and raw_input[index+3] == "(":
        for innerindex in range(index, len(raw_input)):
            inner_element = raw_input[innerindex]
            if inner_element == ")":
                if innerindex > index + 12:
                    break
                else:
                    combined_function = raw_input[index:innerindex+1]
                    number_sub = (raw_input[index+4:innerindex].split(","))
                    if len(number_sub) != 2:
                        break

                    if type(int(number_sub[0])) == int and type(int(number_sub[1])) == int:
                        multi = int(number_sub[0]) * int(number_sub[1])
                        if enable:
                            total += multi
                        else:
                            break
                    else:
                        break



                    # workable_mul.append(raw_input[index:innerindex+1])
                    break




print(total)