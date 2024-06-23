from enum import Enum

user = 0

class Permissions(Enum):
    CREATE = 1 << 0 # 0b0001
    READ = 1 << 1   # 0b0010
    UPDATE = 1 << 2 # 0b0100
    DELETE = 1 << 3 # 0b1000

def set_permissions(*permissions):
    global user
    for permission in permissions:
        user |= permission.value

def delete_permissions(*permissions):
    global user
    for permission in permissions:
        user &= ~permission.value

#########

set_permissions(Permissions.READ)

if (user & Permissions.READ.value):
    print("You can read this!")
else:
    print("Permissions denied")

#########

delete_permissions(Permissions.READ)

if user & Permissions.READ.value:
    print("You can read this!")
else:
    print("Permissions denied")
