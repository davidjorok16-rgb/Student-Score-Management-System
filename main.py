print("STUDENT SCORE MANAGER")
scores= []
Number= input("How many scores? ")
while Number> 0:
    scorevalue= input("Enter score: ")
    if scorevalue<0:
        print(input("Choose value between 0-100: "))
    elif scorevalue>100:
        print(input("Choose value between 0-100: "))
    else:
        scores.append(scorevalue)
print("PERFORMANCE SUMMARY")
print("SCORES: ", scores)










