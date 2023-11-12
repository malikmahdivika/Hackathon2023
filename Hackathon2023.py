print("Hello World!")


class Appliance:
    def __init__(this, name, uses_elec = False, uses_water = False):
        this.name = name
        this.uses_elec = uses_elec
        this.uses_water = uses_water

        this.elec_cost = 0
        this.elec_cost = 0
    
    def set_elec_cost(this, wattage, time):
        if this.uses_elec:
            this.elec_cost = int(wattage * time)
        else:
            this.elec_cost = 0

    def set_water_cost(this, cost):
        if this.has_water:
            this.water_cost = cost
        else:
            this.water_cost = 0

    def get_elec_cost(this):
        return {
            this.elec_cost
        }
    
    def get_water_cost(this):
        return {
            this.water_cost
        }

furnace_wattage = 2000
kWh_to_price = 0.2586
time = int(input("How long do you want to use the furnace: "))
f_kwats = time * furnace_wattage

furnace = Appliance(name="Oven", uses_elec=True)

furnace.set_elec_cost(f_kwats, kWh_to_price)

print("Furnace costs are: ", furnace.get_elec_cost())