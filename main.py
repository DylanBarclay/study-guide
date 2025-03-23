import random
import pandas as pd
import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_definitions(sheets, sheet_names):
    while (True):
        print ("Pick a section to study from. List numbers with commas in between to choose multiple (e.g. type \"1,2,3\" to study from sections 1, 2, and 3). Type \"quit\" to quit:")

        for sheet_num in range(len(sheet_names)):
            print(sheet_num + 1, ". ", sheet_names[sheet_num]);

        sheet_input = input("Section(s): ")

        if (sheet_input.lower() == "quit"):
            print("Quitting")
            sys.exit(0);

        definitions = {}

        try:
            study_sheet_nums = sheet_input.split(",")

            for study_sheet_num in study_sheet_nums:
                for index, row in sheets[sheet_names[int(study_sheet_num) - 1]].iterrows():
                    definitions[row[0]] = row[1]
        except Exception as e:
            print("Invalid selection!")
            print(e)
            continue;

        return definitions;

def play_guess_def(keys, definitions):
    random.shuffle(keys)
    num_correct = 0

    for index in range(len(keys)):
        clear()
        print("Question ", index + 1, " out of ", len(keys))
        key = keys[index]
        print("Definition: ", definitions[key])
        user_input = input("Term: ")

        if user_input.lower() == "quit":
            return num_correct

        if user_input.lower() == key.lower().strip():
            num_correct = num_correct + 1
            print("\nCorrect! Total number correct so far: ", num_correct)
        else:
            print("\nIncorrect! The correct answer was ", key, ". Total number correct so far: ", num_correct)
        input()

    return num_correct

def main():
    file = pd.ExcelFile("LMSW.xlsx")
    sheets = pd.read_excel(file, None, header=None)
    sheet_names = list(sheets.keys())
    play_game = True

    while(play_game):
        clear()
        definitions = get_definitions(sheets, sheet_names)
        clear()

        keys = list(definitions.keys())
        total_questions = len(keys)
        num_correct = play_guess_def(keys, definitions)

        clear()
        print("Game complete! You got ", num_correct, " out of ", total_questions, " correct!")
        play_game = input("Play again? (y/n): ").lower() == "y"
        
main()