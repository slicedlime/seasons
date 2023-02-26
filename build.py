import copy
import json
import os
import os.path as path
import pathlib
from colorsys import hsv_to_rgb, rgb_to_hsv
from typing import Any

import imageio.v3 as imageio
import numpy.typing

template_folder = "templates"
output_folder = "data/seasons/functions/generated"

vanilla_biome_folder = "vanilla/biome"
vanilla_grass_texture = "vanilla/grass.png"
vanilla_foliage_texture = "vanilla/foliage.png"

tag_file = "data/seasons/tags/blocks/snowable_plants.json"
biome_tag_folder = "data/seasons/tags/worldgen/biome"
biome_folder = "data/seasons/worldgen/biome"

seasons = ["summer", "fall", "winter", "spring"]

# Constants

snowy_ground = "F4FEFF"

flowering_leaves = "FF8CAF"
winter_branches = "7C6952"
snowy_leaves = "FFFFFF"

fall_grass = [-25, -25, -5]
winter_grass = [-27, -55, -5]
spring_grass = [1, -10, 0]

fall_sky = [0, -20, -10]
winter_sky = [0, -28, -15]
spring_sky = [0, 0, 0]

early_fall_leaves = [-41, -10, 32]
late_fall_leaves = [-69, 11, -16]
spring_leaves = [0, 5, 32]

fall_temperature = -0.4
winter_temperature = -0.8
spring_temperature = -0.3

# Conversions
to_summer_temperature: dict[str, dict[str, float]] = {
    "default": {
        "fall": -fall_temperature,
        "winter": -winter_temperature,
        "spring": -spring_temperature,
    },
    "summer_rains": {"fall": 0, "winter": 0, "spring": 0},
}

# Permanently summer: warm_ocean, badlands, desert, eroded_badlands, jungle, sparse jungle, mangrove swamp, wooded_badlands
# Permanently winter: frozen_peaks, ice_spikes, frozen_ocean, deep_frozen_ocean
# ???: Lukewarm ocean, swamps

# Mapping of biomes from vanilla biomes per season
# default: leaves shift colors, snowy winters, melting spring
# summer_rains: rain period in summer, dry all other seasons

season_biomes: dict[str, dict[str, str | dict[str, float] | list[str]]] = {
    "beach": {"v_summer": "beach", "v_winter": "snowy_beach"},
    "birch_forest": {"v_summer": "birch_forest"},
    "ocean": {
        "v_winter": "cold_ocean",
        "v_summer": "ocean",
        "winter": {"temperature": -0.3},
    },
    "dark_forest": {"v_summer": "dark_forest"},
    "deep_ocean": {
        "v_winter": "deep_cold_ocean",
        "v_summer": "deep_ocean",
        "winter": {"temperature": -0.3},
    },
    "flower_forest": {"v_summer": "flower_forest"},
    "forest": {"v_summer": "forest"},
    "peaks": {"v_summer": "stony_peaks", "v_winter": "jagged_peaks"},
    "river": {"v_summer": "river", "v_winter": "frozen_river"},
    "grove": {"v_winter": "grove"},
    "meadow": {"v_summer": "meadow"},
    "mushroom_fields": {"v_summer": "mushroom_fields"},
    "old_growth_birch_forest": {"v_summer": "old_growth_birch_forest"},
    "old_growth_pine_taiga": {"v_fall": "old_growth_pine_taiga"},
    "old_growth_spruce_taiga": {"v_fall": "old_growth_spruce_taiga"},
    "plains": {"v_summer": ["plains", "sunflower_plains"], "v_winter": "snowy_plains"},
    "savanna": {"v_winter": ["savanna", "windswept_savanna"], "type": "summer_rains"},
    "savanna_plateau": {"v_winter": ["savanna_plateau"], "type": "summer_rains"},
    "taiga": {
        "v_summer": "taiga",
        "v_winter": "snowy_taiga",
        "default": {"temperature": 0.5},
    },
    "stony_shore": {"v_fall": "stony_shore"},
    "windswept_hills": {
        "v_spring": ["windswept_forest", "windswept_gravelly_hills", "windswept_hills"]
    },
}

with open(tag_file) as file:
    data = json.load(file)
    values = data["values"]


def instantiate_template(type, values):
    folder = template_folder + "/" + type
    for filename in os.listdir(folder):
        template_path = path.join(folder, filename)
        if not path.isfile(template_path):
            continue

        with open(template_path) as file:
            template = file.read()

        with open(path.join(output_folder, filename), "w") as file:
            for value in values:
                file.write(template.replace(f"${type}", value))


instantiate_template("plant", values)


def generate_move(template_name: str, output_name: str, max: int, delegate: str):
    template_path = template_folder + "/move/" + template_name + ".mcfunction"
    with open(template_path) as file:
        template = file.read()
    pathlib.Path(output_folder + "/move").mkdir(parents=True, exist_ok=True)

    i = 1
    while i <= max:
        payload = f"function seasons:generated/move/{output_name}{int(i / 2)}"
        if i == 1:
            payload = delegate

        with open(
            path.join(output_folder, f"move/{output_name}{i}.mcfunction"), "w"
        ) as file:
            file.write(template.replace("$max", str(i)).replace("$payload", payload))
        i *= 2


vanilla_grass_image = imageio.imread(vanilla_grass_texture)
vanilla_foliage_image = imageio.imread(vanilla_foliage_texture)


def union(*args) -> list:
    result = []
    for l in args:
        result.extend(l)
    return result


def add_if_present(biomes: list, biome: dict, key: str) -> None:
    if key not in biome:
        return

    entry = biome[key]
    if isinstance(entry, list):
        biomes.extend([f"minecraft:{x}" for x in entry])
    else:
        biomes.append(f"minecraft:{entry}")


def hex_to_rgb(s: str) -> tuple[float, ...]:
    r = s[0:2]
    g = s[2:4]
    b = s[4:6]
    return tuple(int(x, 16) / 255.0 for x in [r, g, b])


def write_tag(id: str, biomes: list):
    data = {"replace": False, "values": biomes}
    with open(f"{biome_tag_folder}/{id}.json", "w") as file:
        json.dump(data, file, indent=4)


def create_tags(
    biome_id, biome, winter_biomes: list, bare_winter_biomes: list, snowy_biomes: list
):
    summer_list = [f"seasons:summer/{biome_id}"]
    fall_list = [f"seasons:fall_early/{biome_id}", f"seasons:fall_late/{biome_id}"]
    bare_winter_biome = f"seasons:winter_bare/{biome_id}"
    winter_list = [bare_winter_biome, f"seasons:winter_snowy/{biome_id}"]
    melting_list = [f"seasons:winter_melting/{biome_id}"]
    spring_list = [
        f"seasons:spring_default/{biome_id}",
        f"seasons:spring_flowering/{biome_id}",
    ]

    winter_biomes.extend(winter_list)
    bare_winter_biomes.append(bare_winter_biome)

    vanilla: list[str] = []
    for season in seasons:
        add_if_present(vanilla, biome, f"v_{season}")

    type = biome.get("type", "default")
    if type == "default":
        snowy_biomes.extend(winter_list)

    non_summer = union(vanilla, fall_list, winter_list, melting_list, spring_list)
    non_fall = union(vanilla, summer_list, winter_list, melting_list, spring_list)
    non_winter = union(vanilla, summer_list, fall_list, melting_list, spring_list)
    non_spring = union(vanilla, summer_list, fall_list, winter_list, melting_list)
    any = union(vanilla, summer_list, fall_list, winter_list, melting_list, spring_list)

    write_tag(f"non_summer/{biome_id}", non_summer)
    write_tag(f"non_fall/{biome_id}", non_fall)
    write_tag(f"non_winter/{biome_id}", non_winter)
    write_tag(f"non_spring/{biome_id}", non_spring)
    write_tag(f"any/{biome_id}", any)


def int_to_rgb(color: int) -> tuple[float, ...]:
    r = (color >> 16) & 0xFF
    g = (color >> 8) & 0xFF
    b = color & 0xFF
    return r / 255.0, g / 255.0, b / 255.0


def rgb_to_int(r: float, g: float, b: float) -> int:
    r = r * 255
    g = g * 255
    b = b * 255
    return ((int(r) & 0xFF) << 16) | ((int(g) & 0xFF) << 8) | (int(b) & 0xFF)


def calculate_color(
    downfall: float, temperature: float, colormap: numpy.typing.NDArray
) -> int:
    product = downfall * temperature
    x = int((1.0 - temperature) * 255.0)
    y = int((1.0 - product) * 255.0)
    if y >= colormap.shape[0] or x >= colormap.shape[1]:
        return -65281

    pixel = colormap[y, x]
    return rgb_to_int(pixel[0] / 255.0, pixel[1] / 255.0, pixel[2] / 255.0)


def remap_color(color: int, mapping: list[float]) -> int:
    r, g, b = int_to_rgb(color)
    h, s, v = rgb_to_hsv(r, g, b)
    h += mapping[0] / 255.0
    s += mapping[1] / 100.0
    v += mapping[2] / 100.0
    if h > 1.0:
        h -= 1.0
    if h < 0:
        h += 1.0
    r, g, b = hsv_to_rgb(h, s, v)
    color = rgb_to_int(r, g, b)
    return color


def load_biome(biome_id: str) -> dict[str, Any]:
    filename = f"{vanilla_biome_folder}/{biome_id}.json"
    with open(filename, "r") as file:
        biome = json.load(file)
    set_default_colors(biome)
    return biome


def set_default_colors(biome, override=False):
    effects = biome["effects"]
    downfall = biome["downfall"]
    temperature = biome["temperature"]
    if "grass_color" not in effects or override:
        effects["grass_color"] = calculate_color(
            downfall, temperature, vanilla_grass_image
        )
    if "foliage_color" not in effects or override:
        effects["foliage_color"] = calculate_color(
            downfall, temperature, vanilla_foliage_image
        )


def get_first_template(biome: dict, season: str) -> str | None:
    key = f"v_{season}"
    template = biome.get(key, None)
    if isinstance(template, list):
        return template[0]
    return template


def remap(biome, key, mapping):
    effects = biome["effects"]
    effects[key] = remap_color(effects[key], mapping)


def set_color(biome, key, hex):
    r, g, b = hex_to_rgb(hex)
    effects = biome["effects"]
    effects[key] = rgb_to_int(r, g, b)


def apply_overrides(biome_data, conversion, season):
    if not season in conversion:
        return
    for key, item in conversion[season].items():
        biome_data[key] = item


def update_precipitation(biome):
    if biome["precipitation"] == "none":
        return
    temperature = biome["temperature"]
    if temperature < 0.15:
        biome["precipitation"] = "snow"
    else:
        biome["precipitation"] = "rain"


def write_biome(biome_id, biome, season):
    with open(f"{biome_folder}/{season}/{biome_id}.json", "w") as file:
        json.dump(biome, file, indent=2)


def create_biomes(biome_id: str, biome: dict):
    biome_type = biome.get("type", "default")
    templates: dict[str, str | None] = {}
    for season in seasons:
        templates[season] = get_first_template(biome, season)

    if templates["summer"] is not None:
        template = load_biome(templates["summer"])
    else:
        # Try to find a fallback and use as template
        for season in seasons:
            other_template = templates[season]
            if other_template is not None:
                template = load_biome(other_template)
                template["temperature"] += to_summer_temperature[biome_type][season]
                set_default_colors(template)
                break

    apply_overrides(template, biome, "default")

    if biome_type == "default":
        summer = copy.deepcopy(template)
        update_precipitation(summer)
        write_biome(biome_id, summer, "summer")

        if templates["fall"]:
            fall_template = load_biome(templates["fall"])
        else:
            fall_template = None

        if fall_template:
            fall_early = copy.deepcopy(fall_template)
        else:
            fall_early = copy.deepcopy(template)
            fall_early["temperature"] += fall_temperature
            remap(fall_early, "grass_color", fall_grass)
            remap(fall_early, "sky_color", fall_sky)
        # Vanilla doesn't have fall colors, so just transform as if the template was summer regardless
        remap(fall_early, "foliage_color", early_fall_leaves)
        apply_overrides(fall_early, biome, "fall")
        update_precipitation(fall_early)
        write_biome(biome_id, fall_early, "fall_early")

        if fall_template:
            fall_late = copy.deepcopy(fall_template)
        else:
            fall_late = copy.deepcopy(template)
            fall_late["temperature"] += fall_temperature
            remap(fall_late, "grass_color", fall_grass)
            remap(fall_late, "sky_color", fall_sky)
        # Vanilla doesn't have fall colors, so just transform as if the template was summer regardless
        remap(fall_late, "foliage_color", late_fall_leaves)
        apply_overrides(fall_late, biome, "fall")
        update_precipitation(fall_late)
        write_biome(biome_id, fall_late, "fall_late")

        if templates["winter"]:
            winter_template = load_biome(templates["winter"])
        else:
            winter_template = None

        if winter_template:
            winter_bare = copy.deepcopy(winter_template)
        else:
            winter_bare = copy.deepcopy(template)
            winter_bare["temperature"] += winter_temperature
            remap(winter_bare, "grass_color", winter_grass)
            remap(winter_bare, "sky_color", winter_sky)
        set_color(winter_bare, "foliage_color", winter_branches)
        apply_overrides(winter_bare, biome, "winter")
        update_precipitation(winter_bare)
        if winter_bare["precipitation"] != "snow":
            print(f"Warning: winter biome for {biome_id} doesnt snow")
        write_biome(biome_id, winter_bare, "winter_bare")

        winter_snowy = copy.deepcopy(winter_bare)
        set_color(winter_snowy, "grass_color", snowy_ground)
        set_color(winter_snowy, "foliage_color", snowy_leaves)
        write_biome(biome_id, winter_snowy, "winter_snowy")

        winter_melting = copy.deepcopy(winter_snowy)
        winter_melting["temperature"] = template["temperature"] + spring_temperature
        if "spring" in biome and "temperature" in biome["spring"]:
            winter_melting["temperature"] = biome["spring"]["temperature"]
        update_precipitation(winter_melting)
        if winter_melting["precipitation"] != "rain":
            print(f"Warning: melting winter biome for {biome_id} snows")
        write_biome(biome_id, winter_melting, "winter_melting")

        if templates["spring"]:
            spring_template = load_biome(templates["spring"])
        else:
            spring_template = None

        if spring_template:
            spring_default = copy.deepcopy(spring_template)
        else:
            spring_default = copy.deepcopy(template)
            spring_default["temperature"] += spring_temperature
        remap(spring_default, "grass_color", spring_grass)
        remap(spring_default, "sky_color", spring_sky)
        remap(spring_default, "foliage_color", spring_leaves)
        apply_overrides(spring_default, biome, "spring")
        update_precipitation(spring_default)
        write_biome(biome_id, spring_default, "spring_default")

        spring_flowering = copy.deepcopy(spring_default)
        set_color(spring_flowering, "foliage_color", flowering_leaves)
        write_biome(biome_id, spring_flowering, "spring_flowering")

    elif biome_type == "summer_rains":
        dry = copy.deepcopy(template)
        write_biome(biome_id, dry, "winter_bare")
        write_biome(biome_id, dry, "winter_snowy")
        write_biome(biome_id, dry, "winter_melting")
        write_biome(biome_id, dry, "spring_default")
        write_biome(biome_id, dry, "spring_flowering")
        write_biome(biome_id, dry, "fall_early")
        write_biome(biome_id, dry, "fall_late")
        wet = copy.deepcopy(template)
        wet["downfall"] = 0.75
        wet["precipitation"] = "rain"
        set_default_colors(wet, True)
        write_biome(biome_id, wet, "summer")

    else:
        raise ValueError("Unknown biome type:", biome_type)


winter_biomes: list[str] = []
bare_winter_biomes: list[str] = []
snowy_biomes: list[str] = []
for biome_id, biome in season_biomes.items():
    create_tags(biome_id, biome, winter_biomes, bare_winter_biomes, snowy_biomes)
    create_biomes(biome_id, biome)

write_tag(f"winter", winter_biomes)
write_tag(f"bare_winter", bare_winter_biomes)
write_tag(f"snowy", snowy_biomes)

instantiate_template("biome", season_biomes.keys())

generate_move("z", "z", 64, "function seasons:generated/move/x64")
generate_move(
    "x", "x", 64, "execute positioned ~ 319 ~ run function seasons:findsurface"
)
generate_move("z", "blocks_z", 64, "function seasons:generated/move/blocks_x64")
generate_move(
    "x",
    "blocks_x",
    64,
    "execute positioned ~ 319 ~ run function seasons:findsurface_blocks",
)
