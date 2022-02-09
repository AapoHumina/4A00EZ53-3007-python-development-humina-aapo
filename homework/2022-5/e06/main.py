from string_helper import is_name, get_title

title2 = "battleship"

print(get_title(title2, 30, "-"))

print("Give your name:", end = "")
your_name = input()

if is_name(your_name, ignore_case = False):
    print(f"Hello {your_name} and welcome to {title2.capitalize()} - game", end="!")
    print("")
else:
    print(f"{your_name} is not a proper name or properly capitalized")

try:
    age = int(input("GIVE AGE: "))
except:
    print("please give a number")
else:
    print("everything went fine")
