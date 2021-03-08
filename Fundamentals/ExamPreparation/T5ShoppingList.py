groceries = input().split("!")
data = input()


def it_exist(products, item):
    if item in products:
        return True
    else:
        return False


def add_item(products, item):
    if not it_exist(products, item):
        products.insert(0, item)
    return products


def remove_item(products, item):
    if it_exist(products, item):
        products.remove(item)
    return products


def correct_item(products, old_item, new_item):
    if it_exist(products, old_item):
        index = products.index(old_item)
        products.insert(index, new_item)
        products.remove(old_item)
    return products


def rearrange_item(products, item):
    if it_exist(products, item):
        products.remove(item)
        products.append(item)
    return products


while not data == "Go Shopping!":
    command = data.split()
    if command[0] == "Urgent":
        add_item(groceries, command[1])

    elif command[0] == "Unnecessary":
        remove_item(groceries, command[1])

    elif command[0] == "Correct":
        correct_item(groceries, command[1], command[2])

    elif command[0] == "Rearrange":
        rearrange_item(groceries, command[1])

    data = input()

print(', '.join(groceries))
