def student_report(**kwargs):    
    name = kwargs.get("name")
    scores= [score for key , score in kwargs.items() if key != "name"]
        
    avg = sum(scores) / len(scores)
    if avg >= 90:
        remark = "Excellent"
    elif avg >= 75:
        remark = "Good"
    else:
        remark = "Needs Improvement"

    print(f"Student: {name}")
    print(f"Average Score: {avg:.2f}")
    print(f"Performance: {remark}")

student_report(name="Dibash", math=95, science=85, english=90)

