from string_helper import is_name, get_title

title = "battleship"

get_title(title, 30, "-")

print("Give your name:", end = "")
your_name = input()

if is_name(your_name, ignore_case = False):
    print(f"Hello {your_name} and welcome to {title} - game", end="!")
else:
    print(f"{your_name} is not a proper name or properly capitalized")