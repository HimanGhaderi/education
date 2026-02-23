def my_min(my_list):
    min = my_list[0]
    for item in my_list:
        if min>item:
            min=item
    return min


def my_max(li):
    max = li[0]
    for item in li:
        if max<item:
            max = item

    print(max)


def find(li: list, name: str) -> bool:
    """
    I get a list with a name
    and in the end I return True or False
    True: means I find the name
    False: means I didn't find the name
    """
    for item in li:
        if item == name:
            return True
    return False



# result = my_min([15, 17, 19,20])

# if result == 0:
#     print("we have a very weak student")
# elif result>=15:
#     print("This class is strong in match")


# l = ["Reza", "Ebrahim", "Amin"]
# name = "Reza"

# result = find()
# print(result)