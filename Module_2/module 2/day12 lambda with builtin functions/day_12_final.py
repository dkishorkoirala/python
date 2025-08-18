print("Day 12 - Final Challenge Project: Student Report Generator\n")

students = [
    {"name": "Alice", "scores": [85, 90, 78]},
    {"name": "Bob", "scores": [70, 88, 95]},
    {"name": "Charlie", "scores": [90, 92, 85]},
    {"name": "David", "scores": [80, 82, 84]}
]

# Step 1: 
students_with_avg = list(map(
    lambda x: {**x, "average": round(sum(x["scores"]) / len(x["scores"]), 2)},
    students
))

# Step 2: 
topper = max(students_with_avg, key=lambda x: x["average"])
lowest_scorer = min(students_with_avg, key=lambda x: x["average"])
most_consistent = max(students_with_avg, key=lambda x: min(x["scores"]))

# Step 3: 
sorted_by_avg = sorted(students_with_avg, key=lambda x: x["average"])
sorted_by_highest_score = sorted(students_with_avg, key=lambda x: max(x["scores"]), reverse=True)

# Step 4: 
print(f"Topper: {topper['name']} with average {topper['average']}")
print(f"Lowest Scorer: {lowest_scorer['name']} with average {lowest_scorer['average']}")
print(f"Most consistent performer (best lowest score): {most_consistent['name']} with min score {min(most_consistent['scores'])}")

print("\nSorted by average score:")
for student in sorted_by_avg:
    print(f"{student['name']} - {student['average']}")

print("\nSorted by highest score:")
for student in sorted_by_highest_score:
    print(f"{student['name']} - {max(student['scores'])}")
