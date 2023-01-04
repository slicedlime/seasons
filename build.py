import json
import os
import os.path as path

template_folder = 'templates'
output_folder = 'data/seasons/functions/generated'

tag_file ='data/seasons/tags/blocks/snowable_plants.json'

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

