subjects = ( "Mathematics", "English", "Physics", "Chemistry", "Computer Science" )
print(f"All subjects: {subjects}")
print(f"First subject: {subjects[0]}")
print(f"Last subject: {subjects[-1]}")
print(f"Total number of subjects: {len(subjects)}")
Enter= input("Enter subject: ")
if Enter in subjects:
    print("Subject is available")
else:
    print("Subject not available")
