with open("example.txt") as f:
    raw_input = f.read().strip().split("\n")

list_1 = []
list_2 = []

for i in raw_input:
    split_input = i.split()

    list_1.append(split_input[0])
    list_2.append(split_input[1])


list_1.sort()
list_2.sort()

combined = 0
total = 0

copied_elements = {}

for element in list_2:
    if element in copied_elements:
        copied_elements[element] = copied_elements[element] + 1
    else:
        copied_elements[element] = 1

print(copied_elements)
# for item1 in list_1:
#     current_found = 0
#     for item2 in list_2:
#         if int(item1) == int(item2):
#             current_found = current_found + 1
#     total = total + (int(item1) * current_found)



        # total = 0
        # print(item1)
        # print(item2)
        # diff = abs(int(item1) - int(item2))
        #
        # total = total + diff
