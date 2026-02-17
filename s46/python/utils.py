
def max(li):
    m = li[0]
    for item in li:
        if item > m:
            m = item
    return m


def min(li):
    m = li[0]
    for item in li:
        if item<m:
            m = item
    return m

def students(path):
    file = open(path, "r")

    stu = []
    for row in file:
        row = row.replace("\n", "")
        stu.append(row)

    return stu


def login(name, path):
    users = students(path)

    for item in users:
        if name == item:
            return True
        
    return False

