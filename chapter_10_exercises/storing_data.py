import json
import os


class CreateUser:
    def __init__(self, username, password, department):
        self.username = username
        self.password = password
        self.department = department


"""Ask input for data"""


def get_user_data():
    user_name = input("Enter your name: ")
    password = input("Password: ")
    department = input("Department: ")

    return {"_userName": user_name, "_password": password, "_department": department}


""" Storing or dumping data """


def store_data(userData):
    path = (
        r"E:/Users/Angie Villalba/Documents/Kenny/Pythnon/chapter_10_exercises/accounts/"
        + userData["_userName"]
        + ".json"
    )
    contents = {
        "userName": userData["_userName"],
        "password": userData["_password"],
        "department": userData["_department"],
    }

    try:
        if os.path.exists(path):
            with open(path, "r") as files:
                data = json.load(files)
                print(data)
    except FileNotFoundError:
        print("Sorry your file doesn't exist! ")
    else:
        with open(path, "w") as files:
            json.dump(contents, files)

    return contents


store_data(get_user_data())
