import os
import random
import art
import game_data

print(art.logo)
dataCopy = game_data.data

def getValue(index, key):
    return dataCopy[index].get(key)

def randomIntGen():
    number = random.randint(0, len(dataCopy)-1)
    return number

def game_init():
    randomA = randomIntGen()
    randomB = randomIntGen()
    return (randomA, randomB)

def game_start(intA, intB):
    print(f'Compare A: {getValue(intA, "name")}, {getValue(intA, "description")}, from {getValue(intA, "country")}')
    print(f"\n{art.vs}\n")
    print(f'Against B: {getValue(intB, "name")}, {getValue(intB, "description")}, from {getValue(intB, "country")}')

def game_continue(intA, intB, score):
    os.system('cls')
    print(art.logo)
    print(f"You're right! Current score: {score}")
    print(f'Compare A: {getValue(intA, "name")}, {getValue(intA, "description")}, from {getValue(intA, "country")}')
    print(f"\n{art.vs}\n")
    print(f'Against B: {getValue(intB, "name")}, {getValue(intB, "description")}, from {getValue(intB, "country")}')
    
def checkAnswer(a, b):
    answer_player = input("Who has more followers? Type 'A' or 'B': ")
    answer = "A"
    if b > a:
        answer = "B"
    print(answer, answer_player)
    if answer == answer_player:
        return False
    else:
        return True

a, b = game_init()

game_start(a, b)
score = 0
gamelost = False

while (gamelost != True):
    gamelost = checkAnswer(getValue(a, "follower_count"), getValue(b, "follower_count"))
    if gamelost == True:
        os.system('cls')
        print(art.logo)
        print(f"Sorry, that's wrong, Final score: {score}")
        break
    else:
        score += 1
        a = b
        b = randomIntGen()
        game_continue(a, b, score)
    print("anan")
    



