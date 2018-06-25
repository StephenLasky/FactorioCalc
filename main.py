import items as items

# module stats here
SPEED_MODULE_ENERGY = 0.7
SPEED_MODULE_SPEED = 0.5
SPEED_MODULE_PROD = 0.0

PROD_MODULE_ENERGY = 0.8
PROD_MODULE_SPEED = -0.15
PROD_MODULE_PROD = 0.1

ASSEMBLER3_CRAFT_SPEED = 1.25
# ASSEMBLER3_CRAFT_SPEED = 2.00

# input info
SPEED_MODULE_QUANTITY = 4
PROD_MODULE_QUANTITY = 4

# calculate net effects
net_speed_effect = SPEED_MODULE_QUANTITY * SPEED_MODULE_SPEED + PROD_MODULE_QUANTITY * PROD_MODULE_SPEED
net_prod_effect = SPEED_MODULE_QUANTITY * SPEED_MODULE_PROD + PROD_MODULE_QUANTITY * PROD_MODULE_PROD
craft_speed = ASSEMBLER3_CRAFT_SPEED * (1 + net_speed_effect)

# print net_speed_effect
# print net_prod_effect
# print craft_speed





def production(item):
    seconds_per_item = item.craft_time / craft_speed
    items_per_second = 1 / seconds_per_item

    net_items_per_second = items_per_second + items_per_second * net_prod_effect

    # add quantity amplifier
    net_items_per_second *= item.quantity

    print "PRODUCES:", net_items_per_second, str(item), "/ sec"

def consumption(item):
    seconds_per_item = item.craft_time / craft_speed
    items_per_second = 1 / seconds_per_item

    requirements = ""
    for req in item.requirements:
        requirements += str(item.quantity * req.quantity * items_per_second) + " " + str(req) + ", "

    print "REQUIRES:", requirements + "/ sec"

def prodAndCons(item):
    production(item)
    consumption(item)


# # green circuits
# production(items.GreenCircuit(1))
# consumption(items.GreenCircuit(1))
#
# # do blue circuits here #
# production(items.BlueCircuit(1))
# consumption(items.BlueCircuit(1))
#
# # red circuits
# production(items.RedCircuit(1))
# consumption(items.RedCircuit(1))
#
# # copper wire
# production(items.CopperWire(1))
# consumption(items.CopperWire(1))
#
# # copper wire
# production(items.IronPlate(1))
# consumption(items.IronPlate(1))
#
# # plastic bbar
# production(items.PlasticBar(1))
# consumption(items.PlasticBar(1))
#
# # speed module 1
# production(items.SpeedModule1(1))
# consumption(items.SpeedModule1(1))
#
# # rocket control unit
# production(items.RocketControlUnit(1))
# consumption(items.RocketControlUnit(1))
#
# # engine unit
# production(items.EngineUnit(1))
# consumption(items.EngineUnit(1))
#
# production(items.Pipe(1))
# consumption(items.Pipe(1))

prodAndCons(items.ElectricMiningDrill(1))
prodAndCons(items.Gear(4))
prodAndCons(items.PlasticBar(1))
