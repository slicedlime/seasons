import json
import os
import os.path as path
from colorsys import rgb_to_hsv, hsv_to_rgb

template_folder = 'templates'
output_folder = 'data/seasons/functions/generated'

vanilla_biome_folder = 'vanilla/biomes'

tag_file = 'data/seasons/tags/blocks/snowable_plants.json'
biome_tag_folder = 'data/seasons/tags/worldgen/biome'

snowy_ground = 'F4FEFF'

flowering_leaves = 'FF8CAF'
winter_branches = '7C6952'
snowy_leaves = 'FFFFFF'

fall_grass = [-35, -25, -5]
winter_grass = [-38, -55, -5]
spring_grass = [1, -10, 0]

fall_sky = [0, -20, -10]
winter_sky = [0, -28, -15]
spring_sky = [0, 0, 0]

early_fall_leaves = [-59, -10, 32]
late_fall_leaves = [-97, 11, -16]
spring_leaves = [0, 5, 32]

# Permanently summer: warm_ocean, badlands, desert, eroded_badlands, jungle, sparse jungle, mangrove swamp, wooded_badlands
# Permanently winter: frozen_peaks, ice_spikes, frozen_ocean, deep_frozen_ocean
# ???: Lukewarm ocean, swamp

# Mapping of biomes from vanilla biomes per season
# Default style: leaves shift colors, snowy winters, melting spring
# summer_rains: rain period in summer, dry all other seasons

season_biomes = {
    'beach': {
        'v_summer': 'beach',
        'v_winter': 'snowy_beach'
    },
    'birch_forest': {
        'v_summer': 'birch_forest'
    },
    'ocean': {
        'v_winter': 'cold_ocean',
        'v_summer': 'ocean'
    },
    'dark_forest': {
        'v_summer': 'dark_forest'
    },
    'deep_ocean': {
        'v_winter': 'deep_cold_ocean',
        'v_summer': 'deep_ocean'
    },
    'flower_forest': {
        'v_summer': 'flower_forest'
    },
    'forest': {
        'v_summer': 'forest'
    },
    'peaks': {
        'v_summer': 'stony_peaks',
        'v_winter': 'jagged_peaks'
    },
    'river': {
        'v_summer': 'river',
        'v_winter': 'frozen_river'
    },
    'grove': {
        'v_winter': 'grove'
    },
    'meadow': {
        'v_summer': 'meadow'
    },
    'mushroom_fields': {
        'v_summer': 'mushroom_fields'
    },
    'old_growth_birch_forest': {
        'v_summer': 'old_growth_birch_forest'
    },
    'old_growth_pine_taiga': {
        'v_summer': 'old_growth_pine_taiga'
    },
    'old_growth_spruce_taiga': {
        'v_summer': 'old_growth_spruce_taiga'
    },
    'plains': {
        'v_summer': ['plains', 'sunflower_plains'],
        'v_winter': 'snowy_plains'
    },
    'savanna': {
        'v_winter': ['savanna', 'windswept_savanna'],
        'style': 'summer_rains'
    },
    'savanna_plateu': {
        'v_winter': ['savanna_plateu'],
        'style': 'summer_rains'
    },
    'taiga': {
        'v_summer': 'taiga',
        'v_winter': 'snowy_taiga'
    },
    'stony_shore': {
        'v_summer': 'stony_shore'
    },
    'windswept_hills': {
        'v_summer': ['windswept_forest', 'windswept_gravelly_hills', 'windswept_hills']
    }
}

with open(tag_file) as file:
    data = json.load(file)
    values = data['values']

for filename in os.listdir(template_folder):
    template_path = path.join(template_folder, filename)
    if not path.isfile(template_path):
        continue

    with open(template_path) as file:
        template = file.readline()
    
    with open(path.join(output_folder, filename), 'w') as file:
        for value in values:
            file.write(template.replace('$plant', value))

def union(*args) -> list:
    list = []
    for l in args:
        list.extend(l)
    return list

def add_if_present(biomes: list, biome: dict, key: str):
    if key not in biome:
        return

    entry = biome[key]
    if isinstance(entry, list):
        biomes.extend([f'minecraft:{x}' for x in entry])
    else:
        biomes.append(f'minecraft:{entry}')

def hex_to_rgb(s: str) -> list:
    r = s[0:2]
    g = s[2:4]
    b = s[4:6]
    return [int(x, 16) for x in [r, g, b]]

def write_tag(id: str, biomes: list):
    data = {
        'replace': False,
        'values': biomes
    }
    with open(f'{biome_tag_folder}/{id}.json', 'w') as file:
        json.dump(data, file, indent=4)

winter_biomes = []

for id, biome in season_biomes.items():
    summer = [f'seasons:summer/{id}']
    fall = [f'seasons:fall_early/{id}', f'seasons:fall_late/{id}']
    winter = [f'seasons:winter_bare/{id}', f'seasons:winter_snowy/{id}']
    spring = [f'seasons:winter_melting/{id}', f'seasons:spring_default/{id}', f'seasons:spring_flowering/{id}']

    winter_biomes.extend(winter)

    vanilla = []
    add_if_present(vanilla, biome, 'v_summer')
    add_if_present(vanilla, biome, 'v_fall')
    add_if_present(vanilla, biome, 'v_winter')
    add_if_present(vanilla, biome, 'v_spring')

    non_summer = union(vanilla, fall, winter, spring)
    non_fall = union(vanilla, summer, winter, spring)
    non_winter = union(vanilla, summer, fall, spring)
    non_spring = union(vanilla, summer, fall, winter)

    write_tag(f'non_summer/{id}', non_summer)
    write_tag(f'non_fall/{id}', non_fall)
    write_tag(f'non_winter/{id}', non_winter)
    write_tag(f'non_spring/{id}', non_spring)

write_tag(f'winter', winter_biomes)
