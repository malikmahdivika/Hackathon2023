import webbrowser

print("Welcome!")
print("This is the Accommodation Energy Estimation System")
input("(press any key to continue)")

terminate = input("""\nWe will collect some infomation from you
                  \nIf you disagree, enter '0' to exit
                  \nOr enter anything to continue\n""")

if terminate == "0":
    print("Bye~")
    exit()
else:
    print("Thank you!")



dishwasher_frequency = int(input("So, how many times do you usually use dishwasher in a week: "))
sum_electricity = 0 #+ function_dishwasher_elctricity
sum_water = 0 #+ function_dishwaher_water
print("------------------------------------------")

print("Is your AC always on?")
ac_frequency = int(input("""\n1. Yes
    \n2. sometimes
    \n3. No AC
    \nMake your selection: """))
if ac_frequency == 1:
    sum_electricity = sum_electricity #+ function_ac
elif ac_frequency == 2:
    sum_electricity = sum_electricity #+ function_ac
elif ac_frequency == 3:
    sum_electricity = sum_electricity
print("------------------------------------------")

laundry_frequency = int(input("And how often do you guys do laundry per month: "))
if laundry_frequency == 0:
    print("You are crazy man.")
    sum_electricity = sum_electricity
    sum_water = sum_water
else:
    sum_electricity = sum_electricity #+ function_laundry
    sum_water = sum_water #+ function_laundry
print("------------------------------------------")

print("Cooking at home is a good habit.")
stove_frequency = int(input("How many times do you cook in a week(7 days): "))
if stove_frequency == 0:
    print("Nooo")
else:
    print("\nBy the way, is your stove \n1. gas-based\n2. electricity-based\nMake your choice: ")
    choice = int(input())
    if choice == 1:
        sum_gas = 0 #+ function_stove
    elif choice == 2:
        sum_electricity = sum_electricity #+ function_stove


print("\nSometimes, you might use oven to make your food.")
oven_frequency = int(input("How often do you use it in a month: "))
if oven_frequency != 0:
    oven_time = int(input("and how long do you use it for one time? (in minute): "))
    sum_electricity = sum_electricity #+ function_oven
else:
    print("No worries (*╯3╰)")
print("------------------------------------------")

print("Watching TV is a good entertaining activity.")
tv_frequency = int(input("How often do you watch TV in a week: "))
if tv_frequency != 0:
    tv_time = int(input("and how long do you usually watch TV for one time in minute (just estimate): "))
else:
    print("No problem!")
sum_electricity = sum_electricity #+ function_tv
print("------------------------------------------")

print("Showering is a good way to recover yourself.")
shower_frequency = int(input("How often do you take a shower in a week: "))
if shower_frequency != 0:
    sum_water = sum_water #+ function_shower
    print("\nTaking a bath is more comfortable than taking a shower.")
    bath_frequency = int(input("How often do you take a bath in a month then: "))
    if bath_frequency == 0:
        print("You should try it, you won't regret, trust me.")
    else:
        sum_water = sum_water #+ function_bath 
else:
    print("Eww")
print("------------------------------------------")

print("One More Thing!")
input()
print("""I believe every accommodation in Alberta should have a heat system for dealing with winter
      \nSo please tell me the heat system in your place is 1. gas-based or 2. electricity-based
      \nIf you don't know, press '3' to see the instruction
      \nOr you can press '0' if you don't have heat system in your place w(ﾟДﾟ)w
      \nPlease Make your selection: """)

heat = int(input())
while True:
    if heat == 0:
        print("Work harder.")
        break
    elif heat == 1:
        sum_gas = 0 #+ function_heat_system_g
        break
    elif heat == 2:
        sum_electricity = sum_electricity #+ function_heat_system_e
        break
    elif heat == 3:
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
print("\nResult")












   






