# prompt the user for input

seconds = eval(input("Enter an integer for seconds: "))

minutes = seconds / 60
intMinutes = int(minutes)
remainingSeconds = seconds % 60

print(seconds, "seconds is ", intMinutes, "minutes and ", remainingSeconds, "seconds")