from operator import index
from xmlrpc.client import Boolean

with open("input.txt") as f:
    raw_input = f.read().strip().split("\n")

list1 = []

for i in raw_input:
    split_input = i.split()
    int_swap = list(map(int, split_input))
    list1.append(int_swap)


print(type(list1))
safe_usage = 0

for inner_list in list1:
    if inner_list[0] < inner_list[1]:
        increasing = True
    if inner_list[0] > inner_list[1]:
        increasing = False

    prior_number = None
    for specific_number in inner_list:
        if prior_number == None:
            prior_number = specific_number
        else:

            if abs(prior_number - specific_number) >= 4:
                break
            if increasing: #increasing list
                if prior_number > specific_number or prior_number == specific_number:
                    # if the prior number is greater its no longer increasing so its false
                    break
            else: #decreasing list
                if prior_number < specific_number or prior_number == specific_number:
                    # if the number is less then the current number it is still increasing so its true:
                    break

            if len(inner_list)-1 == inner_list.index(specific_number):
                safe_usage += 1

            prior_number = specific_number


print(safe_usage)




