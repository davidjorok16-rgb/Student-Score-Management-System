print("STUDENT SCORE MANAGER")
scores= []
Number= int(input("How many scores? "))
for number in range(Number):
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
average= total/Number
print(f"Average: {average}")
highest= max(scores)
print(f"Highest: {highest}")
lowest= min(scores)
print(f"Lowest: {lowest}")
passed= len([scorevalue for scorevalue in scores if scorevalue>=50])
print(f"Passed: {passed}")
failed= len([scorevalue for scorevalue in scores if scorevalue<50])
print(f"Failed: {failed}")
scoretoreplace= int(input("Enter score to replace: "))
if scoretoreplace not in scores:
    print("Not among list of scores")
else:
    Newvalue= int(input("Enter new score: "))
    scores.remove(scoretoreplace)
    scores.append(Newvalue)
print("Updated Scores: ", scores)








