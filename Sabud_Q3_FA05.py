days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

daily_totals = []

for d in range(5):
    total = 0
    for p in range(3):
        total += steps[p][d]
    daily_totals.append(total)
    print(days[d], "- Total Steps:", total)

most_active = max(daily_totals)
best_day = days[daily_totals.index(most_active)]

print("Most Active Day:", best_day)
