# Update biomes
scoreboard players set Snow _seasons 0
execute if block ~ ~-1 ~ snow run scoreboard players set Snow _seasons 1
execute if block ~ ~ ~ snow run scoreboard players set Snow _seasons 1

execute if score Snow _seasons matches 1 run function seasons:generated/set_winter_snowy
execute unless score Snow _seasons matches 1 if score UpdateRandom _seasons matches 0 run function seasons:generated/set_winter_bare
scoreboard players reset Snow _seasons

execute if biome ~ ~ ~ #seasons:snowy if predicate seasons:is_snowing positioned ~ ~-1 ~ if block ~ ~ ~ #seasons:snowable_plants run function seasons:snow_on_plants
execute if biome ~ ~ ~ #seasons:snowy positioned ~ ~-1 ~ if block ~ ~ ~ snow if block ~ ~-1 ~ grass_block align xyz positioned ~0.5 ~0.5 ~0.5 unless entity @e[type=marker,distance=..0.0001,tag=_seasons_snow] run function seasons:retain_snowy_grass
