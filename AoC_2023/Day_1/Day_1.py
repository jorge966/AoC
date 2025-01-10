
with open("input.txt") as f:
    raw_input = f.read().strip().split("\n")

print(raw_input)

num_words = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":0,"seven":7,"eight":8,"nine":9}

number = []
main_list = []
total = 0
for item in raw_input:
    inner_list = []
    for ind_char in item:
        if ind_char.isnumeric() == True:
            inner_list.append(int(ind_char))


    first_num = str(inner_list[0])
    last_num = str(inner_list[-1])
    combined_num = int(first_num + last_num)

    total += combined_num


print(total)