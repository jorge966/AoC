
with open("input.txt") as f:
    raw_input = f.read().strip().split("\n")

list_1 = []
list_2 = []

for i in raw_input:
    split_input = i.split()

    list_1.append(split_input[0])
    list_2.append(split_input[1])


list_1.sort()
list_2.sort()

current_index = 0
total = 0

for item1 in list_1:

    current_item2 = int(list_2[current_index])
    diff = abs(int(item1) - current_item2)
    total = total + diff

    current_index = current_index + 1

print(total)
        # total = 0
        # print(item1)
        # print(item2)
        # diff = abs(int(item1) - int(item2))
        #
        # total = total + diff

