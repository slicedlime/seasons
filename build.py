import json
import os
import os.path as path
import imageio.v3 as imageio
import numpy.typing
from colorsys import rgb_to_hsv, hsv_to_rgb

template_folder = 'templates'
output_folder = 'data/seasons/functions/generated'

vanilla_biome_folder = 'vanilla/biome'
vanilla_grass_texture = 'vanilla/grass.png'
vanilla_foliage_texture = 'vanilla/foliage.png'

tag_file = 'data/seasons/tags/blocks/snowable_plants.json'
biome_tag_folder = 'data/seasons/tags/worldgen/biome'
biome_folder = 'data/seasons/worldgen/biome'

seasons = ['summer', 'fall', 'winter', 'spring']

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
# default: leaves shift colors, snowy winters, melting spring
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
    'savanna_plateau': {
        'v_winter': ['savanna_plateau'],
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

vanilla_grass_image = imageio.imread(vanilla_grass_texture)
vanilla_foliage_image = imageio.imread(vanilla_foliage_texture)

def union(*args) -> list:
    result = []
    for l in args:
        result.extend(l)
    return result

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

def create_tags(id, biome, winter_biomes):
    summer_list = [f'seasons:summer/{id}']
    fall_list = [f'seasons:fall_early/{id}', f'seasons:fall_late/{id}']
    winter_list = [f'seasons:winter_bare/{id}', f'seasons:winter_snowy/{id}']
    spring_list = [f'seasons:winter_melting/{id}', f'seasons:spring_default/{id}', f'seasons:spring_flowering/{id}']

    winter_biomes.extend(winter_list)

    vanilla = []
    for season in seasons:
        add_if_present(vanilla, biome, f'v_{season}')

    non_summer = union(vanilla, fall_list, winter_list, spring_list)
    non_fall = union(vanilla, summer_list, winter_list, spring_list)
    non_winter = union(vanilla, summer_list, fall_list, spring_list)
    non_spring = union(vanilla, summer_list, fall_list, winter_list)

    write_tag(f'non_summer/{id}', non_summer)
    write_tag(f'non_fall/{id}', non_fall)
    write_tag(f'non_winter/{id}', non_winter)
    write_tag(f'non_spring/{id}', non_spring)

def calculate_color(downfall: float, temperature: float, colormap: numpy.typing.NDArray) -> int:
    product = downfall * temperature
    x = int((1.0 - temperature) * 255.0)
    y = int((1.0 - product) * 255.0)
    if y >= colormap.shape[0] or x >= colormap.shape[1]:
        return -65281

    pixel = colormap[y, x]
    return int(pixel[0] << 16) | int(pixel[1] << 8) | int(pixel[2])

def load_biome(id: str):
    filename = f'{vanilla_biome_folder}/{id}.json'
    with open(filename, 'r') as file:
        biome = json.load(file)
    effects = biome['effects']
    downfall = biome['downfall']
    temperature = biome['temperature']
    if 'grass_color' not in effects:
        effects['grass_color'] = calculate_color(downfall, temperature, vanilla_grass_image)
    if 'foliage_color' not in effects:
        effects['foliage_color'] = calculate_color(downfall, temperature, vanilla_foliage_image)
    return biome

def get_first_template(biome, season):
    key = f'v_{season}'
    template = biome.get(key, None)
    if isinstance(template, list):
        return template[0]
    return template

def create_biomes(id: str, biome: dict):
    type = biome.get('type', 'default')
    summer_template = get_first_template(biome, 'summer')
    
    if summer_template is not None:
        template = load_biome(summer_template)
    else:
        # Try to find a fallback and use as template
        for season in seasons:
            other_template = get_first_template(biome, season)
            if other_template is not None:
                template = load_biome(other_template)
                # TODO: Transform that biome back to summer state

    with open(f'{biome_folder}/summer/{id}.json', 'w') as file:
        json.dump(template, file, indent=2)

winter_biomes = []
for id, biome in season_biomes.items():
    create_tags(id, biome, winter_biomes)
    create_biomes(id, biome)

write_tag(f'winter', winter_biomes)
