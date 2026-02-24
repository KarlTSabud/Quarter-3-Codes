# 2D array example (scores)
scores = [
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
]

# loop through each row
for row in scores:
    print("Scores:", row)
    
    total = sum(row)
    average = total / len(row)
    
    print("Total:", total)
    print("Average:", average)
    print()

# find highest score
highest = max(scores[0])

for row in scores:
    if max(row) > highest:
        highest = max(row)

print("Highest score:", highest)
