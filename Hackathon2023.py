print("Hello World!")


class Appliance:
    def __init__(this, name, uses_elec = False, uses_water = False):
        this.name = name
        this.uses_elec = uses_elec
        this.uses_water = uses_water

        this.elec_cost = 0
        this.elec_cost = 0
    
    def set_elec_cost(this, cost):
        if this.has_elec:
            this.elec_cost = cost
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
