import math
class Castle:
    def __init__(self):
        self.estetics = ""
        self.treasury = 500
        self.mainKeepLVL = 1
        self.wallLVL = 0
        self.westTowerLVL = 0
        self.eastTowerLVL = 0
        self.farmLVL = 1
        self.weather = 1 #0 = rain, 1 cloud, 2 some sun, 3, sunny, 4 = rainbow
        self.region = "" #Europa or Japan

    def tax(self, tick):
        if tick % 10 == 0:
            farm_tax = self.farmLVL * self.weather  # Use wether as a multiplier for farmLVL
            excluded_attributes = ['weather', 'farmLVL', 'treasury']  # Attributes to exclude
            total_tax = 0

            for attr, value in self.__dict__.items():
                if attr not in excluded_attributes and isinstance(value, (int, float)):
                    total_tax += value
            return math.ceil(int(total_tax + farm_tax))
        else:
            return 0
    def upgrading_price(self, building_lvl):
        base_cost = 100  # Cost of the first upgrade
        upgrade_factor = 1.5  # Adjust this factor to suit the cost increase rate

        # Calculate the cost based on the building level
        upgrade_cost = base_cost * (upgrade_factor ** (building_lvl - 1))
        return math.ceil(upgrade_cost)
    
    def upgrade_building(self, building_name):
        # Check if the building exists in the castle
        if hasattr(self, building_name):
            current_level = getattr(self, building_name + 'LVL')
            upgrade_cost = self.upgrading_price(current_level + 1)

            # Check if the castle has enough resources to perform the upgrade
            if upgrade_cost <= self.treasury:
                # Deduct the upgrade cost and perform the upgrade
                self.treasury -= upgrade_cost
                setattr(self, building_name + 'LVL', current_level + 1)
                print(f"{building_name} upgraded to level {current_level + 1}")
            else:
                print("Insufficient coins to upgrade")

        else:
            print("Building not found")

    #def save():
        
    #def load():

    #def setWeather(self, weather):
        #Set ewther based on castle level?

    #def wind(self, region):

class EuropeanCastle(Castle):
    def __init__(self):
        super().__init__()
        self.region = "Europe"
        self.gateLVL = 0
        #self.armoryLVL = 0  # Additional attribute specific to European castles
        #self.moat = 0


class JapaneseCastle(Castle):
    def __init__(self):
        super().__init__()
        self.region = "Japan"
        self.dojoLVL = 0  # Additional attribute specific to Japanese castles
    


japan = JapaneseCastle()

#japan.upgrade_building("mainKeep")

