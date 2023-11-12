import webbrowser

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
sum_electricity = 0 #+ function_dishwasher_elctricity
sum_water = 0 #+ function_dishwaher_water
print("------------------------------------------")

print("Is your ac always on?")
ac_frequency = int(input("""1. Yes
      \n 2. sometimes
      \n 3. No AC"""))
if ac_frequency == 1:
    sum_electricity = sum_electricity #+ function_ac
elif ac_frequency == 2:
    sum_electricity = sum_electricity #+ function_ac
elif ac_frequency == 3:
    sum_electricity = sum_electricity
print("------------------------------------------")

laundry_frequency = int(input("And how often do you guys do laundry per month?"))
sum_electricity = sum_electricity #+ function_laundry
sum_water = sum_water #+ function_laundry
print("------------------------------------------")

stove_frequency = int(input("Cooking at home is a good habit, let's say, how many times do you cook in a week(7 days)?"))
if stove_frequency == 0:
    print("Nooo")
else:
    print("By the way, is your stove 1.gas-based or 2.electricity-based?")
    if int(input()) == 1:
        sum_gas = 0 #+ function_stove
    elif int(input()) == 2:
        sum_electricity = sum_electricity #+ function_stove

print("\n Sometimes, you might use oven to cook your food.")
oven_frequency = int(input("how often do you use it in a month: "))
oven_time = int(input("and how long do you use it for one time? (in miuite): "))
sum_electricity = sum_electricity #+ function_oven
print("------------------------------------------")

print("Watching TV is a good entertaining activity.")
tv_frequency = int(input("how often do you watch TV in a week: "))
if tv_frequency != 0:
    tv_time = int(input("and how long do you usually watch TV for one time? (in miuite): "))
else:
    print("No problem!")
sum_electricity = sum_electricity #+ function_tv
print("------------------------------------------")

print("Showering is a good way to recover yourself.")
shower_frequency = int(input("How often do you guys take a shower in a week? "))
if shower_frequency != 0:
    sum_water = sum_water #+ function_shower
    bath_frequency = int(input("""Taking a bath is more comfortable than taking a shower.
                               \nHow often do you take a bath in a month then: """))
    sum_water = sum_water #+ function_bath 
else:
    print("Eww")
print("------------------------------------------")

print("""One more thing!
      \nI believe every accommodation in Alberta should have a heat system for dealing with winter
      \nSo the heat system in your place is 1. gas-based or 2. electricity-based
      \n If you don't know, press 0 to see the instruction
      \n Make your selection: """)

heat = int(input())
while True:
    if heat == 1:
        sum_gas = sum_gas #+ function_heat_system_g
        break
    elif heat == 2:
        sum_electricity = sum_electricity #+ function_heat_system_e
        break
    elif heat == 0:
        webbrowser.open('https://www.google.com/search?q=How+do+I+know+what+kind+of+heating+system+I+have&sca_esv=581597527&ei=4TFQZcqsMa-70PEP7uCgyAw&ved=0ahUKEwiKoY_prr2CAxWvHTQIHW4wCMkQ4dUDCBA&uact=5&oq=How+do+I+know+what+kind+of+heating+system+I+have&gs_lp=Egxnd3Mtd2l6LXNlcnAiMEhvdyBkbyBJIGtub3cgd2hhdCBraW5kIG9mIGhlYXRpbmcgc3lzdGVtIEkgaGF2ZTIIEAAYigUYkQIyCBAAGIoFGIYDMggQABiKBRiGAzIIEAAYigUYhgMyCBAAGIoFGIYDSLcXUOkBWOkBcAF4AZABAJgBdqABdqoBAzAuMbgBA8gBAPgBAfgBAqgCCsICFhAAGAMYjwEY5QIY6gIYtAIYjAPYAQHCAhYQLhgDGI8BGOUCGOoCGLQCGIwD2AEB4gMEGAAgQYgGAboGBAgBGAo&sclient=gws-wiz-serp')
        heat = int(input("""1. gas-based or 2. electricity-based
                        \nNow make your selection: """))
        continue
print("------------------------------------------")
print("Thank you for your time.")
print("Base on the infomation you provided, we can conclude that...")
input("(press any key to see the result)")
input("3...")
input("2...")
input("1...")
print("0")












   






