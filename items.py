

RAW_MATERIAL_CRAFT_TIME = 0
RAW_MATERIAL_REQUIREMENTS = []
RAW_MATERIAL_QUANTITY = 0

class Item:
    def __init__(self, craft_time, requirements, quantity):
        self.craft_time = craft_time
        self.requirements = requirements
        self.quantity = quantity

    def printItem(self):
        print "craft time:", self.craft_time
        req_str = ""
        for req in self.requirements:
            req_str += str(req) + ","
        print "requirements:", req_str

    def __str__(self):
        return self.__class__.__name__


# RAW MATERIALS
class CopperOre(Item):
    def __init__(self, quantity):
        Item.__init__(self,RAW_MATERIAL_CRAFT_TIME, RAW_MATERIAL_REQUIREMENTS, quantity)

class IronOre(Item):
    def __init__(self, quantity):
        Item.__init__(self,RAW_MATERIAL_CRAFT_TIME, RAW_MATERIAL_REQUIREMENTS, quantity)

class CoalOre(Item):
    def __init__(self, quantity):
        Item.__init__(self, RAW_MATERIAL_CRAFT_TIME, RAW_MATERIAL_REQUIREMENTS, quantity)

class PetroleumGas(Item):
    def __init__(self, quantity):
        Item.__init__(self, RAW_MATERIAL_CRAFT_TIME, RAW_MATERIAL_REQUIREMENTS, quantity)

class SulfuricAcid(Item):
    def __init__(self, quantity):
        Item.__init__(self, RAW_MATERIAL_CRAFT_TIME, RAW_MATERIAL_REQUIREMENTS, quantity)

# INTERMEDIATE ITEMS
class CopperPlate(Item):
    def __init__(self, quantity):
        Item.__init__(self, 3.5, [CopperOre(1)], quantity)

class IronPlate(Item):
    def __init__(self, quantity):
        Item.__init__(self, 3.5, [IronOre(1)], quantity)


class SteelPlate(Item):
    def __init__(self, quantity):
        Item.__init__(self, 17.5, [IronPlate(5)], quantity)

class CopperWire(Item):
    def __init__(self, quantity):
        Item.__init__(self, 0.5, [CopperPlate(0.5)], quantity)

class GreenCircuit(Item):
    def __init__(self, quantity):
        Item.__init__(self, 0.5, [CopperWire(3), IronPlate(1)], quantity)

class RedCircuit(Item):
    def __init__(self, quantity):
        Item.__init__(self, 6, [CopperWire(4), GreenCircuit(2), PlasticBar(2)], quantity)

class BlueCircuit(Item):
    def __init__(self, quantity):
        Item.__init__(self, 10, [GreenCircuit(20), RedCircuit(2), SulfuricAcid(5)], quantity)

class PlasticBar(Item):
    def __init__(self, quantity):
        Item.__init__(self, 1, [CoalOre(1), PetroleumGas(20)], quantity)


class SpeedModule1(Item):
    def __init__(self, quantity):
        Item.__init__(self, 15, [GreenCircuit(5), RedCircuit(5)], quantity)

class RocketControlUnit(Item):
    def __init__(self, quantity):
        Item.__init__(self, 30, [BlueCircuit(1), SpeedModule1(1)], quantity)

class Gear(Item):
    def __init__(self, quantity):
        Item.__init__(self, 0.5, [IronPlate(2)], quantity)

class Pipe(Item):
    def __init__(self, quantity):
        Item.__init__(self, 0.5, [IronPlate(1)], quantity)

class EngineUnit(Item):
    def __init__(self, quantity):
        Item.__init__(self, 10, [Gear(1), SteelPlate(1), Pipe(2)], quantity)

class ElectricMiningDrill(Item):
    def __init__(self, quantity):
        Item.__init__(self, 2, [Gear(15), IronPlate(10), GreenCircuit(3)], quantity)


# Science packs
class SciencePack3(Item):
    def __init__(self, quantity):
        Item.__init__(self, 12, [RedCircuit(1), ElectricMiningDrill(1), EngineUnit(1)], quantity)