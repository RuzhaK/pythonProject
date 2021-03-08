items = input().split(", ")
data = input()


def is_item_in_list(items, item):
    if item in items:
        return True
    else:
        return False


def collect_item(items, item):
    if not is_item_in_list(items, item):
        items.append(item)
    return items


def renew_item(items, item):
    if is_item_in_list(items,item):
        items.remove(item)
        items.append(item)
    return items


def combine_item(items, old_item, new_item):
    if is_item_in_list(items,old_item):
        index_of_old_item=items.index(old_item)
        #todo взимане на индекс
        items.insert(index_of_old_item+1,new_item)
    return items


def drop_this_item(items, item):
    if is_item_in_list(items, item):
        items.remove(item)
    return items


while not data == "Craft!":
    command, item = data.split(" - ")
    if command == "Collect":
        collect_item(items, item)

    if command == "Drop":
        drop_this_item(items, item)
    if command == "Combine Items":
        old_item, new_item = item.split(":")
        combine_item(items, old_item, new_item)
    if command == "Renew":
        renew_item(items, item)
    data = input()

print(', '.join(items))
