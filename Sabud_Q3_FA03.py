steps = [
    [4500, 5200, 4800, 5500, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

for i in range(3):
    total = sum(steps[i])
    average = total / 5
    minimum = min(steps[i])
    maximum = max(steps[i])

    print(f"Friend {i+1} - Total Steps: {total} | Average: {average} | Min: {minimum} | Max: {maximum}")
