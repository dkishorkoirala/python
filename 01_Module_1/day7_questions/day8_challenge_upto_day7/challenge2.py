#challenge: Student score analyzer

student = {}
for i in range(5):
    name = input("Enter student name: ")
    subject = {}
    
    for j in ["math","science", "english"]:
        score = int(input(f"Enter the score of {j} score for {name}: "))
        subject[j] = score

    student[name] = subject

print(student)

topper = ""
top_avg = 0

for name,score in student.items():
    avg = sum(score.values()) / len(score)
    print (f"{name}'s average score: {avg:.2f}")

    if avg > top_avg:
        top_avg = avg
        topper = name
        
print(f"\nTopper : {topper} with average score: {top_avg:.2f}")