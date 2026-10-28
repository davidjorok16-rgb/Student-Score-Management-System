print("STUDENT SCORE MANAGER")
scores= []
Numberofstudents = int(input("How many student scores? "))
for number in range(Numberofstudents):
    scorevalue= int(input("Enter score: "))
    if scorevalue<0:
        print(int(input("Choose value between 0-100: ")))
    elif scorevalue>100:
        print(int(input("Choose value between 0-100: ")))
    else:
        scores.append(scorevalue)
print("PERFORMANCE SUMMARY")
print("SCORES: ", scores)
total= int(sum(scores))
print(f"Total: {total}")
average= total/Numberofstudents
print(f"Average: {average}")
highest= max(scores)
print(f"Highest: {highest}")
lowest= min(scores)
print(f"Lowest: {lowest}")
passed= len([scorevalue for scorevalue in scores if scorevalue>=50])
print(f"Passed: {passed}")
failed= len([scorevalue for scorevalue in scores if scorevalue<50])
print(f"Failed: {failed}")
# scoretoreplace= int(input("Enter score to replace: "))
# if scoretoreplace not in scores:
#     print("Not among list of scores")
# else:
#     Newvalue= int(input("Enter new score: "))
#     scores.remove(scoretoreplace)
#     scores.append(Newvalue)
# print("Updated Scores: ", scores)


# while True:
#     scoretoreplace= int(input("Enter score to replace: "))
#     if s

try:
    score_to_replace= int(input("Enter score to replace: "))
    if score_to_replace in scores:
        # while True:
            try:
                New_score= float(input("Enter new score: "))
                if 0<= New_score <= 100:
                    idx= scores.index(score_to_replace)
                    scores[idx]= New_score
                else:
                    print("Invalid score. ")
            except ValueError:
                print("Invalid input") 
                  
            print(f"Updated score: {scores}")

            total= int(sum(scores))
            print(f"Total: {total}")
            average= total/Numberofstudents
            print(f"Average: {average}")
            highest= max(scores)
            print(f"Highest: {highest}")
            lowest= min(scores)
            print(f"Lowest: {lowest}")

            passed=0 
            failed=0
            for s in scores:
                if s>=50:
                    passed += 1
                else:
                    failed += 1
            print(f"Passed: {passed}")
            print(f"Failed: {failed}")
    else:
        print(f"The score {score_to_replace} you want to replace does not exist.")
except ValueError:
    print("Invalid input")



