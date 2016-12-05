# Create a Rocket class.
# It should take 3 parameters in its constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9".
# 2nd parameter: the starting fuel level as a number, defaults to 0.
# 3rd parameter: number of launches as a number, defaults to 0.
#
# It should have 3 methods:
#
# launch()
# it should use 1 fuel if it's a falcon1 and 9 fuels if it's a falcon9.
# it should increment the launches by one if it had enough fuel for the launch.
#
# refill()
# it should refill the rocket's fuel level to 5 if falcon1 and to 20 if falcon9.
# it should return the amount of fuel used for the refill.
# example: if the rocket is a falcon1 and has fuel level 3, then it should return 2.
#
# getStats()
# it should return its stats as a string like: "name: falcon9, fuel: 11, launches: 1"

################################################

class Rocket():

    def __init__(self, rocket_type='', fuel_level=0, launches_count=0):
        self.rocket_type = rocket_type
        self.fuel_level = fuel_level
        self.launches_count = launches_count

        self.launch_fuel = {'falcon1': 1, 'falcon9': 9}
        self.refill_levels = {'falcon1': 5, 'falcon9': 20}

    def launch(self):
        self.fuel_level -= self.launch_fuel[self.rocket_type]
        if self.fuel_level >= 0:
            self.launches_count += 1

    def refill(self):
        fuel_needed = self.refill_levels[self.rocket_type] - self.fuel_level
        self.fuel_level += fuel_needed
        return fuel_needed

    def getStats(self):
        return 'name: {}, fuel: {}, launches: {}'.format(self.rocket_type, self.fuel_level, self.launches_count)

'''
# NOTE: Code commented out since this file acts as module for fifth.py and shouldn't run.

falcon1 = Rocket('falcon1')
returned_falcon9 = Rocket('falcon9', 11, 1)

falcon1.refill() # 5
falcon1.launch()

print(falcon1.getStats()) # name: falcon1, fuel: 4, launches: 1
print(returned_falcon9.getStats()) # name: falcon9, fuel: 11, launches: 1
'''
