# score = int(input("Please enter score"))
# if score >= 70:
#     print("distinction")
# elif score >= 40:
#     print("pass")
# else:
#     print("fail")


# score = int(input("Please enter score"))
# if score >= 40:
#     if score >= 70:
#         print("pass with merit")
#     else:
#         print("pass")
# else:
#     print("fail")


# w2s3 if-else practice problems

# age = int(input("Enter your age: "))
# if age < 5:
#     print("free entry")
# elif age <= 17:
#     print("child ticket")
# elif age <= 64:
#     print("adult ticket")
# else:
#     print("senior ticket")

# days_late = int(input("enter number of days late:"))
# if days_late == 0:
#     print("no fine")
# elif days_late <= 5:
#     print("fine: £1")
# elif days_late <=10:
#     print("fine: £5")
# else:
#     print("fine: £10 and membership review")


# score = int(input("enter your exam score (0-100): "))
# if score > 40:
#     if score <=42:
#         print("borderline pass, consider review")
#     else:
#         print("clear pass")
# else:
#     print("fail")


# is_student = input("are you a student? (yes/no): ")
# age = int(input("enter age: "))
# if is_student == "yes" or age < 18:
#     print("discount applied")
# else:
#     print("no discount")


# colour = input("enter traffic light colour (red, amber, green")
# if colour == "red":
#     print("stop")
# elif colour == "amber":
#     print("get ready")
# elif colour == "green":
#     print("go")
# else:
#     print("invalid colour")


# number = int(input("enter a number: "))
# if number % 3 == 0 and number % 5 == 0:
#     print("fizzbuzz")
# elif number % 3 == 0:
#     print("fizz")
# elif number % 5 == 0:
#     print("buzz")
# else:
#     print("no match")


# time_of_day = input("enter time of day (morning/afternoon/evening): ")
# is_hungry = input("are you hungry? (yes/no): ")
# if is_hungry == "no":
#     print("have some water and rest")
# else:
#     if time_of_day == "morning":
#         print("have breakfast")
#     elif time_of_day == "afternoon":
#         print("have lunch")
#     elif time_of_day == "evening":
#         print("have dinner")
#     else:
#         print("snack time")


# coursework = int(input("enter coursework mark (0-100): "))
# exam = int(input("enter exam mark (0-100): "))
# average = (coursework + exam) / 2
# if coursework < 35 or exam < 35:
#     print("automatic fail (component below 35) ")
# elif average >= 40:
#     print("module passed.")
# else:
#     print("module failed (average below 40) ")


# pin = input("enter your 4 digit pin: ")
# if pin == "1234":
#     colour = input("what is your favourite colour? ")
#     if colour == "blue":
#         print("access granted")
#     else:
#         print("security answer incorrect")
# else:
#     print("wrong pin")

# weather = input("enter weather (sunny/rainy/cold): ")
# mood = input("enter mood (active/tired: ")
# if weather == "sunny" and mood == "active":
#     print("go for a run")
# elif weather == "sunny" and mood == "tired":
#     print("relax in the park")
# elif weather == "rainy":
#     print("indoor workout")
# elif weather == "cold":
#     print("go to the gym")
# else:
#     print("no suggestion available")