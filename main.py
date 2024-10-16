from game_data import data
from art import logo , vs
import random

def game():
    score = 0
    should_continue = True
    option_a = random.choice(data)
    while should_continue:
        if score>0:
            print("\n" * 20)
        option_b = random.choice(data)
        print(logo)
        if score>0:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")

        print(vs)
        print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")
        your_ans = input("Who has more follower? Type 'A' or 'B' : ").lower()
        if your_ans == 'a':
            if option_a['follower_count'] >= option_b['follower_count']:
                print("Correct answer")
                option_a = option_b
                score += 1
            else:
                print("\n" * 35)
                print(logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                should_continue = False
        elif your_ans == 'b':
            if option_b['follower_count'] >= option_a['follower_count']:
                print("Correct answer")
                score += 1
                option_a = option_b
            else:
                print("\n" * 35)
                print(logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                should_continue = False
        else:
            print("invalid input")
            should_continue = False



game()
