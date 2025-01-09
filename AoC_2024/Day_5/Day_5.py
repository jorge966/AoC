
with open("input_rules.txt") as f:
    raw_rules = f.read().strip().split("\n")

with open("input.txt") as x:
    raw_input = x.read().strip().split("\n")

corrected_list = []

rules = []
example_input = []
for x in raw_rules:
    rules.append(x.split("|"))

for element in raw_input:
    example_input.append(element.split(','))

bad_reports = 0

added_total = 0
for index in range(0, len(example_input)):
    workable_report = True
    element = example_input[index]

    for inner_index in range(0, len(element)):
        if not workable_report:
            break
        inner_list = element[inner_index]

        for rule in range(0, len(rules)):
            inner_rules = rules[rule]
            if inner_list == inner_rules[0]:
                if not workable_report:
                    break
                if inner_rules[1] in element:
                    second_rule = element.index(inner_rules[1])
                else:
                    continue
                if second_rule < inner_index:
                    print(str(element) + " is a bad report")
                    workable_report = False
                    bad_reports += 1
                    break

        if inner_index + 1 == len(element) and workable_report:
            middle = element[len(element)//2]
            added_number = int(middle)
            print(added_number)
            added_total += added_number





print(bad_reports)

print(added_total)