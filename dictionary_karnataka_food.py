karnataka_food = {
    "bengalure" : "bis bele bath",
    "mysore" : "mysore dosa" ,
    "hampi" : "ragi mudde",
    "udupi" : "udupi sambar",
    "coorg" : "coorgi pork curry",
    "mangalore" : "neer dosa",
    "chikmagalur" : "karnataka coffee",
    "bellary" : "bellary onion dosa",
    "hubli" : "jolada rotti",
    "dharwad" : "dharwad pedha",
    "kolar" : "kolar vada",
    "chitradurga" : "chitradurga chicken curry",
    "bagalkot" : "bagalkot kachori",
    "gadag" : "gadag dosa",
    "raichur" : "raichur puliogare",
    "mandya" : "mandya akki rotti",
    "tumkur" : "tumkur benne dosa",
    "chikkaballapur" : "chikkaballapur idli",
    "hassan" : "hassan puliyogare",
    "koppal" : "koppal kachori",                            
}
print(karnataka_food)
print("Karnataka food dictionary created successfully.")
print("This dictionary contains popular dishes from various cities in Karnataka.")
print("You can access the food items by their respective city names.")      
def get_karnataka_food_info():
    return karnataka_food
def get_karnataka_food_info_by_key(key):
    if key in karnataka_food:
        return karnataka_food[key]
    else:
        return "Key not found"
def get_karnataka_food_info_by_value(value):
    for key, val in karnataka_food.items():
        if val == value:
            return key
    return "Value not found"    