import time

currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = totalHours % 24

# print("The current Time: ", currentTime)
# print("Total Seconds: ", totalSeconds)
# print("Current Seconds: ", currentSecond)
# print("Total Minutes: ", totalMinutes)
# print("Current Minute: ", currentMinute)

print("The Current Time is: ", currentHour, ":", currentMinute, ":", currentSecond, "UTC")
print("The Current Time is: ", currentHour+9, ":", currentMinute, ":", currentSecond, "KST")