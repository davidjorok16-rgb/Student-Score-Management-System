scores= []
Number= input("Number of scores to enter: ")
while Number>0
    scorevalue= input("Score Value: ")
    if scorevalue<0:
        print(input("Choose value between 0-100: "))
    elif scorevalue>100:
        print(input("Choose value between 0-100: "))
    else:
        scores.append(scorevalue)
    print("SCORES: ", scores)
