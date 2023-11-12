import webbrowser

class Appliance:
	def __init__(this, name, uses_elec = False, uses_water = False):
		this.name = name
		this.uses_elec = uses_elec
		this.uses_water = uses_water
		
		this.elec_cost = 0
		this.water_cost = 0
		
	def set_elec_cost(this, wattage, time):
		if this.uses_elec:
			this.elec_cost = int(wattage * time)
		else:
			this.elec_cost = 0
		return this.elec_cost
	
	def set_water_cost(this, amount, time):
		if this.uses_water:
			this.water_cost = int(amount / time)
		else:
			this.water_cost = 0
		return this.water_cost
	
	def usage_rate(this, frequency, time):
		return
	
	
	def get_elec_cost(this):
		return (
			this.elec_cost
		)
	
	def get_water_cost(this):
		return (
			this.water_cost
		)

furnace_wattage = 800 #values in kwh/month
dishwasher_wattage = 20.98
dishwasher_water = 116
ac_wattage = 500
laundry_wattage = 2.0 #kwh per load
laundry_water = 116
stove_wattage = 90
oven_wattage = 150
tv_wattage = 9
shower_wattage = 1582 #why does a shower need electricity lol; water consumption in terms of litres/month
bath_wattage = 150 #per bath
gheater_wattage = 2303 #do not use electricity; gas used m^3
eheater_wattage = 360
kWh_to_price = 0.2586

sum_water = 0
sum_electricity = 0

furnace = Appliance(name="furnace", uses_elec=True)
dishwasher = Appliance(name="dishwasher", uses_elec=True, uses_water=True)
ac = Appliance(name="ac", uses_elec=True)
laundry = Appliance(name="laundry", uses_elec=True)
gstove = Appliance(name="gstove", uses_elec=True)
estove = Appliance(name="estove", uses_elec=True)
oven = Appliance(name="oven", uses_elec=True)
tv = Appliance(name="tv", uses_elec=True)
shower = Appliance(name="shower", uses_elec=True)
bath = Appliance(name="bath", uses_elec=True)
gas_heater = Appliance(name="gas_heater", uses_elec=True)
elec_heater = Appliance(name="elec_heater", uses_elec=True)
		
		
		
		
		
		
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
sum_electricity = dishwasher.set_elec_cost((dishwasher_frequency * dishwasher_wattage), kWh_to_price)
sum_water =  dishwasher.set_water_cost((dishwasher_frequency * dishwasher_wattage), kWh_to_price)
print("------------------------------------------")

print("Is your AC always on?")
ac_frequency = int(input("""\n1. Yes
		\n2. sometimes
		\n3. No AC
		\nMake your selection: """))
if ac_frequency == 1:
		sum_electricity = sum_electricity + ac.set_elec_cost((ac_frequency * ac_wattage), kWh_to_price)
elif ac_frequency == 2:
		sum_electricity = sum_electricity + (ac.set_elec_cost((ac_frequency * ac_wattage), kWh_to_price))/2
elif ac_frequency == 3:
		sum_electricity = sum_electricity
print("------------------------------------------")

laundry_frequency = int(input("And how often do you guys do laundry per month: "))
if laundry_frequency == 0:
		print("You are crazy man.")
		sum_electricity = sum_electricity
		sum_water = sum_water
else:
		sum_electricity = sum_electricity + sum_electricity + laundry.set_elec_cost((laundry_frequency * laundry_wattage), kWh_to_price)
		sum_water = sum_water + laundry.set_water_cost((laundry_frequency * laundry_wattage), kWh_to_price)
print("------------------------------------------")

print("Cooking at home is a good habit.")
stove_frequency = int(input("How many times do you cook in a week(7 days): "))
if stove_frequency == 0:
		print("Nooo")
else:
		print("\nBy the way, is your stove \n1. gas-based\n2. electricity-based\nMake your choice: ")
		choice = int(input())
		if choice == 1:
				sum_gas = sum_electricity + gstove.set_elec_cost((stove_frequency * stove_wattage), kWh_to_price)
		elif choice == 2:
				sum_electricity = sum_electricity + estove.set_elec_cost((stove_frequency * stove_wattage), kWh_to_price)
			
			
print("\nSometimes, you might use oven to make your food.")
oven_frequency = int(input("How often do you use it in a month: "))
if oven_frequency != 0:
		oven_time = int(input("and how long do you use it for one time? (in minute): "))
		sum_electricity = sum_electricity + oven.set_elec_cost(((oven_frequency*oven_time)/60 * oven_wattage), kWh_to_price)
else:
		print("No worries (*╯3╰)")
print("------------------------------------------")

print("Watching TV is a good entertaining activity.")
tv_frequency = int(input("How often do you watch TV in a week: "))
if tv_frequency != 0:
		tv_time = int(input("and how long do you usually watch TV for one time in minute (just estimate): "))
		sum_electricity = sum_electricity + tv.set_elec_cost(((tv_frequency*tv_time)/60 * tv_wattage), kWh_to_price)
else:
		print("No problem!")

print("------------------------------------------")

print("Showering is a good way to recover yourself.")
shower_frequency = int(input("How often do you take a shower in a week: "))
if shower_frequency != 0:
		sum_water = sum_water + shower.set_elec_cost((shower_frequency * shower_wattage), kWh_to_price)
		print("\nTaking a bath is more comfortable than taking a shower.")
		bath_frequency = int(input("How often do you take a bath in a month then: "))
		if bath_frequency == 0:
				print("You should try it, you won't regret, trust me.")
		else:
				sum_water = sum_water + bath.set_elec_cost((bath_frequency * bath_wattage), kWh_to_price)
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
				sum_gas = sum_gas + gas_heater.set_elec_cost((gheater_wattage), kWh_to_price) 
				break
		elif heat == 2:
				sum_electricity = sum_electricity + elec_heater.set_elec_cost((eheater_wattage), kWh_to_price)
				break
		elif heat == 3:
				webbrowser.open('https://www.google.com/search?q=How+do+I+know+what+kind+of+heating+system+I+have&sca_esv=581597527&ei=4TFQZcqsMa-70PEP7uCgyAw&ved=0ahUKEwiKoY_prr2CAxWvHTQIHW4wCMkQ4dUDCBA&uact=5&oq=How+do+I+know+what+kind+of+heating+system+I+have&gs_lp=Egxnd3Mtd2l6LXNlcnAiMEhvdyBkbyBJIGtub3cgd2hhdCBraW5kIG9mIGhlYXRpbmcgc3lzdGVtIEkgaGF2ZTIIEAAYigUYkQIyCBAAGIoFGIYDMggQABiKBRiGAzIIEAAYigUYhgMyCBAAGIoFGIYDSLcXUOkBWOkBcAF4AZABAJgBdqABdqoBAzAuMbgBA8gBAPgBAfgBAqgCCsICFhAAGAMYjwEY5QIY6gIYtAIYjAPYAQHCAhYQLhgDGI8BGOUCGOoCGLQCGIwD2AEB4gMEGAAgQYgGAboGBAgBGAo&sclient=gws-wiz-serp')
				heat = int(input("""1. gas-based or 2. electricity-based
												\nNow make your selection: """))
				continue
print("------------------------------------------")
print("Thank you for your time.")
print("Base on the information you provided, we can conclude that...")
input("(press any key to see the result)")
input("3...")
input("2...")
input("1...")
print("\nResult")
