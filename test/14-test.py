# # if today is Tuesday,
# # => what day of the week will be in 100 days
# # week => Mon = 1 , Tue = 2
# # 2 = Tue
# # 100 = after hundred days
# # 7 = number of total days in one week
#
# after_hundred_days = (2 + 100) % 7
#
# if after_hundred_days == 1:
#     print("If today is Tuesday, after 100 days will be: Monday")
# elif after_hundred_days == 2:
#     print("If today is Tuesday, after 100 days will be: Tuesday")
# elif after_hundred_days == 3:
#     print("If today is Tuesday, after 100 days will be: Wednesday")
# elif after_hundred_days == 4:
#     print("If today is Tuesday, after 100 days will be: Thursday")
# elif after_hundred_days == 5:
#     print("If today is Tuesday, after 100 days will be: Friday")
# elif after_hundred_days == 6:
#     print("If today is Tuesday, after 100 days will be: Saturday")
# else:
#     print("If today is Tuesday, after 100 days will be: Sunday")


today = eval(input("What day is it Today? "))
# today = 1 # Tuesday
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
after = (today + 100) % 7 # the day after 100 days

print("If today is: ", days[today])
print("After 100 days: ", days[after])