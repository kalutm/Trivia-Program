import requests, sys, csv
from random import choice

def main():
    current_score, amount = get_questions(get_input())
    name = input("\nEnter Name: \n").strip().lower()
    print("\n-----------------------\n", f"   Name: {name.title()}\n   Current_Score: {current_score} out of {amount}\n   High_Score: {high_score(name, current_score, amount)} out of {amount}\n", "-----------------------\n", sep="\n")


def get_input():
    # dictionary of all possible question categories with thier respective id's
    categories = {
        "General Knowledge": 9,
        "Entertainment: Film": 11,
        "Entertainment: Music": 12,
        "Entertainment: Television":14,
        "Entertainment: Video Games": 15,
        "Science & Nature": 17,
        "Science: Computers": 18,
        "Sports": 21,
        "Geography": 22,
        "History": 23,
        "Animals": 27,
        "Entertainment: Japanese Anime & Manga": 31
    }

    # prompting the user to choose a category
    while True:
        print("\nEnter Category From The Given or Press Enter For Random\n")
        for i in categories:
            print(i)
        category = input("\n").strip().title()

        if category in categories:
            category = categories[category]
            break
        if category in "":
            category = ""
            break

    # prompting the user to choose a difficulty
    while True:
        print("\nEnter Difficulty From The Given or Press Enter For Random\nEasy\nMedium\nHard\n")
        difficulty = input("").strip().lower()
        if difficulty in ["easy", "medium", "hard"]:
            break
        if difficulty in "":
            break

    # prompting the user to choose a number of questions
    while True:
        try:
            print("\nEnter Amount of Questions\n5\n10\n")
            amount = int(input("").strip())
            if amount in [5, 10]:
                break
        except Exception as e:
            print(e)
    return (category, difficulty, amount)

# function for shuffling the multiple choices randomly and creating a dict object of choices and the letters A B C D
def shuffle_choices(choices):
    randomized = []
    while len(randomized) < 4:
        rand = choice(choices)
        if rand not in randomized:
            randomized.append(rand)
    return {j: randomized[l] for l, j in enumerate(["A", "B", "C", "D"])}

def get_questions(user_input):
    category, difficulty, amount = user_input
    try:
        response = requests.get(f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type=multiple")
        questions = response.json()['results']
        score = 0

        for i, question in enumerate(questions):
            # putting all the choices in one list
            choices = [k for k in question["incorrect_answers"]] + [question["correct_answer"]]
            choic = shuffle_choices(choices)

            while True:
                print(f"\n{i + 1}. {question["question"]}", f"A.{choic["A"]}   B.{choic["B"]}   C.{choic["C"]}   D.{choic["D"]}\n", sep="\n")
                anss = input('\n').strip().upper()
                if anss in ["A", "B", "C", "D"]:
                    ans = choic[f"{anss}"]
                    break

            # checking if the user has inputed the correct answer and adding to the score
            if ans == question["correct_answer"]:
                score += 1

        return (score, amount)
    except Exception as e:
        print(e)



def high_score(user_name, current_score, amount):
    scores = f"scores{amount}.csv"
    temp_scores = f"after{amount}.csv"

    with open(scores) as f, open(temp_scores, "w", newline="") as w:
        names = []
        dnames = []
        players = csv.DictReader(f)
        writer = csv.DictWriter(w,fieldnames=["name", "high_score"])

        # storing the player's high_score data in the memory
        for player in players:
            names.append(player["name"])
            dnames.append(player)

        # checking if the player is already on the high_score's data
        if user_name in names:
            player_index = names.index(user_name)

            # updating the high_score of the player
            if current_score > int(dnames[player_index]["high_score"]):
                dnames[player_index]["high_score"] = current_score
        else:

            # appending the high_score of a new player
            dnames.append({"name": user_name, "high_score": current_score})
        writer.writeheader()

        # storing the updated high_score data in the csv file
        for player in dnames:
            writer.writerow(player)

    # copying the temporary file's content back to the original one
    with open(temp_scores) as f, open(scores, "w", newline="") as w:
        names = []
        players = csv.DictReader(f)
        writer = csv.DictWriter(w,fieldnames=["name", "high_score"])
        writer.writeheader()

        # finding the player's high_score to return to the function
        for player in players:
            writer.writerow(player)
            names.append(player["name"])

        player_index = names.index(user_name)
        return dnames[player_index]["high_score"]


if __name__ == "__main__":
    main()
