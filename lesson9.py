# loops

while True:
    print("Hello, loops")
    break

scores = [90, 76, 54, 24, 78, 17, 90, 23, 90, 45, 78, 34, 73, 54, 98, 56]

# for each score
for score in scores:
    if score >= 80 and score <= 98 and score % 2 == 0:
        print(score)
