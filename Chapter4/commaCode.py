# Ch 4 Comma Code

spam = ["apples", "bananas", "tofu", "cats"]

supplies = ["pens", "staplers", "flamethrowers", "binders"]

pets = ["Dog", "Cat", "Moose"]

people = ["Alice", "Bob", "Carol", "David"]


def separate(listValue):
    lengthOfList = len(listValue)
    for i in range(lengthOfList):
        if i == 0:
            stringValue = listValue[i]
        if i != lengthOfList - 1:
            stringValue += ", " + listValue[i]
        else:
            stringValue += ", and " + listValue[i]
    return stringValue


print(separate(spam))
print(separate(supplies))
print(separate(pets))
print(separate(people))
