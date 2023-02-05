# Update biomes
execute if block ~ ~-1 ~ snow run function seasons:generated/set_winter_snowy
execute unless block ~ ~-1 ~ snow if score UpdateRandom _seasons matches 0 run function seasons:generated/set_winter_bare

execute if biome ~ ~ ~ #seasons:winter if predicate seasons:is_snowing positioned ~ ~-1 ~ if block ~ ~ ~ #seasons:snowable_plants run function seasons:snow_on_plants
