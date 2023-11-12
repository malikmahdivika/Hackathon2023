print("Welcome!")
print("This is the Accommodation Energy Estimation System")
input("(press any key to continue)")

terminate = input("""We will collect some infomation from you
                  \nif you disagree, enter '0' to exit
                  \nor enter anything to continue\n""")

if terminate == "0":
    print("Bye~")
    exit()
else:
    print("Thank you!")



dishwasher_frequency = int(input("So, how many times do you usually use dishwasher in 2 days?"))
sum_electricity = #function_dishwasher_elctricity
sum_water = #function_dishwaher_water
print("------------------------------------------")

print("Is your ac always on?")
ac_frequency = int(input("""1. Yes
      \n 2. sometimes
      \n 3. No AC"""))
if ac_frequency == 1:
    sum_electricity = sum_electricity + #function_ac
elif ac_frequency == 2:
    sum_electricity = sum_electricity + #function_ac
elif ac_frequency == 3:
    sum_electricity = sum_electricity
print("------------------------------------------")

laundry_frequncy = int(input("And how often do you guys do laundry per month?"))
sum_electricity = sum_electricity + #function_laundry
sum_water = sum_water + #function_laundry
print("------------------------------------------")

stove_frequency = int(input("Cooking at home is a good habit, let's say, how many times do you cook in a week(7 days)?"))
if stove_frequency == 0:
    print("Nooo")
else:
    print("By the way, is your stove 1.gas-based or 2.electricity-based?")
    if int(input()) == 1:
        sum_gas = #function_stove
    elif int(input()) == 2:
        sum_electricity = sum_electricity + #function_stove

print("\n Sometimes, you might use oven to cook your food.")
oven_frequncy = int(input("how often do you use it in a month: "))
oven_time = int(input("and how long do you use it for one time? (in miuite): "))
sum_electricity = sum_electricity + #function_oven
print("------------------------------------------")

print("Watching TV is a good entertaining activity.")
tv_frequncy = int(input("how often do you watch TV in a week: "))
tv_time = int(input("and how long do you usually watch TV for one time? (in miuite): "))
sum_electricity = sum_electricity + #function_tv
print("------------------------------------------")





   






