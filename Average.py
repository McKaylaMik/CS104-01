howManyEntered = 0
total = 0
average = 0

howMany = int(input("How many test scores would you like to average? "))

while howManyEntered < howMany:
    testScore = int(input("Enter test score: "))
    total += testScore
    howManyEntered += 1

if howMany == 0:
    average = 0
else:
    average = total/howMany

txt = "The average for the test scores you entered is: {}"
print(txt.format(average))

