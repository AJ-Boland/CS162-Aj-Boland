password = "123"


def get_password(id):
    if id == "Aj":
        print(f"Id is: {id}")
        return "123"
    else:
        print(f"Else statement")
        return ""

def login(username):
    pass_attempt= input("Please login with your password: ")
    login_code = get_password( username ) 
    print(username)
    if pass_attempt == login_code:
        print("Successful Login! Welcome User")
    else:
        print("You messed with the wrong 6 line program bud")


def boot():
    login("Aj")
boot()