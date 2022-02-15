import random

def get_lotto_numbers(min = 1, max = 40, amount = 7):
    if min >= max or amount > max or amount < 0:
        raise Exception ("invalid numbers")
    lotto_numbers = set()
    while len(lotto_numbers) < amount:
        lotto_numbers.add(random.randint(min,max))
    return lotto_numbers


user_lotto = {1, 2, 3, 4, 5, 6, 7}
win_num_counter = 0
time_counter = 0
while win_num_counter < 7:
    random_lotto = get_lotto_numbers()
    x = len(user_lotto.intersection(random_lotto))
    time_counter = time_counter + 1
    if x > win_num_counter:
        win_num_counter = x
        if win_num_counter == 1:
            print("You got 1 correct! New highscore!")
            if time_counter == 1:
                print(f"It took {time_counter} week.")
            else:
                print(f"It took {time_counter} weeks.")
        elif win_num_counter == 2:
            print("You got 2 correct! New highscore!")
            if time_counter > 52:
                time_counter_year = int(time_counter/52)
                print(f"It took {time_counter_year} years")
            else:
                print(f"It took {time_counter} weeks")
        elif win_num_counter == 3:
            print("You got 3 correct! New highscore!")
            if time_counter > 52:
                time_counter_year = int(time_counter/52)
                print(f"It took {time_counter_year} years")
            else:
                print(f"It took {time_counter} weeks")
        elif win_num_counter == 4:
            print("You got 4 correct! New highscore!")
            if time_counter > 52:
                time_counter_year = int(time_counter/52)
                print(f"It took {time_counter_year} years")
            else:
                print(f"It took {time_counter} weeks")
        elif win_num_counter == 5:
            print("You got 5 correct! New highscore!")
            if time_counter > 52:
                time_counter_year = int(time_counter/52)
                print(f"It took {time_counter_year} years")
            else:
                print(f"It took {time_counter} weeks")
        elif win_num_counter == 6:
            print("You got 6 correct! New highscore!")
            if time_counter > 52:
                time_counter_year = int(time_counter/52)
                print(f"It took {time_counter_year} years")
            else:
                print(f"It took {time_counter} weeks")
        elif win_num_counter == 7:
            print("You got 7 correct! New highscore!")
            if time_counter > 52:
                time_counter_year = int(time_counter/52)
                print(f"It took {time_counter_year} years")
            else:
                print(f"It took {time_counter} weeks")