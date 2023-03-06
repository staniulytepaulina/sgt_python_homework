import os.path
import sys
from os import path, makedirs, listdir
from datetime import date

name = str(input("Please provide your name: "))
surname = str(input("Please provide your surname: "))
personal_id = 0
file_path = ""
current_date = date.today().strftime("%Y-%m-%d")


def get_personal_id():
    try:
        global personal_id
        personal_id = int(input("Please provide your ID number: "))
    except ValueError:
        print("Not a number provided. Try again.")
        get_personal_id()


def create_dir():
    if not path.exists(current_date):
        makedirs(current_date)


def get_file_path():
    global file_path
    file_path = path.join(current_date, f"{personal_id}.txt")


def write_into_file():
    with open(file_path, "w") as f:
        f.write(f"Name: {name}\nSurname: {surname}\nPersonal ID: {personal_id}\n")


def ask_if_wants_to_override():
    wants_to_override = str(input("Do you want to override this file? Yes/No")).lower()
    if wants_to_override == "yes" or wants_to_override == "y":
        return True
    elif wants_to_override == "no" or wants_to_override == "n":
        return False
    else:
        print("Didn't understand you, please try again.")
        ask_if_wants_to_override()


def write_info_into_file():
    if not os.path.exists(file_path):
        write_into_file()
    else:
        print("File with such id already exists.")
        if ask_if_wants_to_override():
            write_into_file()
        else:
            sys.exit()


def print_out_files_info():
    for file in listdir(current_date):
        with open(path.join(current_date, file), "r") as f:
            print(f.read())


get_personal_id()
create_dir()
get_file_path()
write_info_into_file()
print_out_files_info()
