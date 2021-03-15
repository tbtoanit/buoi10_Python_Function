from re import split
from string import ascii_uppercase


def send_email():
    """
    :return:
    """
    return "send success"


def save_database():
    """
    :return:
    """
    return "save success"


def create_facebook_account(email, name, phone, address = "No data"):
    """
    :param email: this is an email information from the form
    :param name: this is name
    :param phone: ....
    :return: No returned value
    """
    print(address)
    if send_email() == "send success" and save_database() == "save success":
        return "account has been created"
    else:
        return "Cannot create account"

def hello(*name, word):
    for val in name:
        print(word+ " " + val.title())

hello("an","tran","bao", word="hello")

def my_title(value):
    v = value[0].upper() + value[1:len(value)]
    return v

print(my_title("toi"))

#print(my_string_title("toi ten la ton"))
s = "toi-ten-la-ton" # list_name = ["toi","ten","la","ton"]
list_name = s.split("-")
print(list_name)
#this is a new line for git
