from string_helper import is_name

print("Your name:")
your_name = input()

if is_name(your_name, ignore_case = True):
    print(f"Hello {your_name}", end="!")
else:
    print(f"{your_name} is not a proper name or properly capitalized")