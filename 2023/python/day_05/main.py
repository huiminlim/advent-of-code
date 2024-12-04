import os
import sys

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#print(ROOT_DIR)

# Parse input
seeds_to_plant = []
with open(f"{ROOT_DIR}/seeds.txt", "r") as f:
    for line in f:
        seeds_to_plant = [int(x) for x in line.split(":")[-1].strip().split(" ")]
# print(seeds_to_plant)

# Dest = soil
# Src = seed
seed_to_soil_map = []
with open(f"{ROOT_DIR}/seed-soil.txt", "r") as f:
    f.readline()
    for line in f:
        temp = [int(x) for x in line.strip().split(" ")]
        dest_start = temp[0]
        src_start = temp[1]
        range_len = temp[2]
        # for idx in range(range_len):
        #     seed_to_soil_map[src_start+idx] = dest_start+idx
        seed_to_soil_map.append({"seed_start": src_start, "soil_start": dest_start, "count": range_len})
def seed_to_soil(seed):
    for map in seed_to_soil_map:
        seed_start = map["seed_start"]
        soil_start = map["soil_start"]
        range_len = map["count"]
        if seed in range(seed_start, seed_start+range_len):
            return soil_start + (seed - seed_start)
    return seed
# print(seed_to_soil(79))
# print(seed_to_soil(14))
# print(seed_to_soil(55))
# print(seed_to_soil(13))

# Dest = fertilizer
# Src = soil
soil_to_fertilizer_map = []
with open(f"{ROOT_DIR}/soil-fertilizer.txt", "r") as f:
    f.readline()
    for line in f:
        temp = [int(x) for x in line.strip().split(" ")]
        dest_start = temp[0]
        src_start = temp[1]
        range_len = temp[2]
        soil_to_fertilizer_map.append({"soil_start": src_start, "fertilizer_start": dest_start, "count": range_len})
        # for idx in range(range_len):
        #     soil_to_fertilizer_map[src_start+idx] = dest_start+idx
def soil_to_fertilizer(soil):
    for map in soil_to_fertilizer_map:
        soil_start = map["soil_start"]
        fertilizer_start = map["fertilizer_start"]
        range_len = map["count"]
        if soil in range(soil_start, soil_start+range_len):
            return fertilizer_start + (soil - soil_start)
    return soil

# Dest = water
# Src = fertilizer
fertilizer_to_water_map = []
with open(f"{ROOT_DIR}/fertilizer-water.txt", "r") as f:
    f.readline()
    for line in f:
        temp = [int(x) for x in line.strip().split(" ")]
        dest_start = temp[0]
        src_start = temp[1]
        range_len = temp[2]
        fertilizer_to_water_map.append({"fertilizer_start": src_start, "water_start": dest_start, "count": range_len})
        # for idx in range(range_len):
        #     fertilizer_to_water_map[src_start+idx] = dest_start+idx
def fertilizer_to_water(fertilizer):
    for map in fertilizer_to_water_map:
        fertilizer_start = map["fertilizer_start"]
        water_start = map["water_start"]
        range_len = map["count"]
        if fertilizer in range(fertilizer_start, fertilizer_start+range_len):
            return water_start + (fertilizer - fertilizer_start)
    return fertilizer

# Dest = light
# Src = water
water_to_light_map = []
with open(f"{ROOT_DIR}/water-light.txt", "r") as f:
    f.readline()
    for line in f:
        temp = [int(x) for x in line.strip().split(" ")]
        dest_start = temp[0]
        src_start = temp[1]
        range_len = temp[2]
        water_to_light_map.append({"water_start": src_start, "light_start": dest_start, "count": range_len})
        # for idx in range(range_len):
        #     water_to_light_map[src_start+idx] = dest_start+idx
def water_to_light(water):
    for map in water_to_light_map:
        water_start = map["water_start"]
        light_start = map["light_start"]
        range_len = map["count"]
        if water in range(water_start, water_start+range_len):
            return light_start + (water - water_start)
    return water

# Dest = temp
# Src = light
light_to_temp_map = []
with open(f"{ROOT_DIR}/light-temp.txt", "r") as f:
    f.readline()
    for line in f:
        temp = [int(x) for x in line.strip().split(" ")]
        dest_start = temp[0]
        src_start = temp[1]
        range_len = temp[2]
        light_to_temp_map.append({"light_start": src_start, "temp_start": dest_start, "count": range_len})
        # for idx in range(range_len):
        #     light_to_temp_map[src_start+idx] = dest_start+idx
def light_to_temp(light):
    for map in light_to_temp_map:
        light_start = map["light_start"]
        temp_start = map["temp_start"]
        range_len = map["count"]
        if light in range(light_start, light_start+range_len):
            return temp_start + (light - light_start)
    return light

# Dest = humid
# Src = temp
temp_to_humid_map = []
with open(f"{ROOT_DIR}/temp-humid.txt", "r") as f:
    f.readline()
    for line in f:
        temp = [int(x) for x in line.strip().split(" ")]
        dest_start = temp[0]
        src_start = temp[1]
        range_len = temp[2]
        temp_to_humid_map.append({"temp_start": src_start, "humid_start": dest_start, "count": range_len})
        # for idx in range(range_len):
        #     temp_to_humid_map[src_start+idx] = dest_start+idx
def temp_to_humid(temp):
    for map in temp_to_humid_map:
        temp_start = map["temp_start"]
        humid_start = map["humid_start"]
        range_len = map["count"]
        if temp in range(temp_start, temp_start+range_len):
            return humid_start + (temp - temp_start)
    return temp

# Dest = loc
# Src = humid
humid_to_loc_map = []
with open(f"{ROOT_DIR}/humid-loc.txt", "r") as f:
    f.readline()
    for line in f:
        temp = [int(x) for x in line.strip().split(" ")]
        dest_start = temp[0]
        src_start = temp[1]
        range_len = temp[2]
        humid_to_loc_map.append({"humid_start": src_start, "loc_start": dest_start, "count": range_len})
        # for idx in range(range_len):
        #     humid_to_loc_map[src_start+idx] = dest_start+idx
def humid_to_loc(humid):
    for map in humid_to_loc_map:
        humid_start = map["humid_start"]
        loc_start = map["loc_start"]
        range_len = map["count"]
        if humid in range(humid_start, humid_start+range_len):
            return loc_start + (humid - humid_start)
    return humid

loc = []
for seed in seeds_to_plant:
    loc.append(humid_to_loc(temp_to_humid(light_to_temp(water_to_light(fertilizer_to_water(soil_to_fertilizer(seed_to_soil(seed))))))))
loc.sort()
# print(loc[0])

# Part 2
lowest = sys.maxsize
for idx in range(0, len(seeds_to_plant), 2):
    seed_start = seeds_to_plant[idx]
    num = seeds_to_plant[idx+1]
    # print(seed_start, num)
    for seed in range(seed_start, seed_start+num):
        print(idx, len(seeds_to_plant), seed, seed_start+num)
        val = humid_to_loc(temp_to_humid(light_to_temp(water_to_light(fertilizer_to_water(soil_to_fertilizer(seed_to_soil(seed)))))))
        lowest = val if val < lowest else lowest
print(lowest)
