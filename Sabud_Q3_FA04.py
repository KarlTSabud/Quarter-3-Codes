names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

totals = []

for i in range(3):
    totals.append(sum(steps[i]))

highest = max(totals)
lowest = min(totals)
top_person = names[totals.index(highest)]

print("Top Performer:", top_person)
print("Highest Total Steps:", highest)
print("Difference between Highest and Lowest:", highest - lowest)
