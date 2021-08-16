# Trivia Challenge 
#Trivia game that reads a plain text file. 

import sys
import pickle 
 
def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file    

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line
    
def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    points = next_line(the_file)
    
    correct = next_line(the_file)
    if correct:
        correct = correct[0] 
        
    explanation = next_line(the_file)
    
    return category, question, answers, points, correct, explanation   
        
def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
    print("\t\tThe current high score list is:")
    try:
        score_board = open("trivia10 High Scores Final.dat", "rb")
    except IOError:
        input("\n\nNo scores available yet, press the enter key to continue.")
    else: 
        scores = pickle.load(score_board)
        score_board.close()
        print("\n")
        print("\t\t\tHighScores:", scores)
        
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    name = input("What is your name?: ")
    score = 0 
    
    # get first block 
    category, question, answers, points, correct, explanation = next_block(trivia_file)
    while category:
    #ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer 
        if answer == correct:
            print("\nRight!", end=" ")
            score += int(points)
        else:
            print("\nWrong.", end=" ")
            print(explanation)
            print("Score:", score, "\n\n")
        
         
        final_score = [name, score]
        
        # get next block 
        category, question, answers, points, correct, explanation = next_block(trivia_file)
    try:
        score_board = open("trivia10 High Scores Final.dat", "rb")
    except IOError:
        score_board = open("trivia10 High Scores Final.dat", "wb")
    else:
        scores = pickle.load(score_board)
         
    new_scores = [scores]       
    new_scores.append(final_score)
    score_board.close()
    
    score_board = open("trivia10 High Scores Final.dat", "wb")
    pickle.dump(new_scores, score_board)
    score_board.close()
    trivia_file.close()

    print("That was the last question!")
    print("Your final score is", score)

main()
input("\n\nPress the enter key to exit.")