# Update biomes
execute if block ~ ~-1 ~ snow run fillbiome ~ -64 ~ ~ 319 ~ seasons:winter_snowy/forest replace #seasons:non_winter/forest
execute unless block ~ ~-1 ~ snow if score UpdateRandom _seasons matches 0 run fillbiome ~ -64 ~ ~ 319 ~ seasons:winter_bare/forest replace #seasons:non_winter/forest

execute if biome ~ ~ ~ #seasons:winter if predicate seasons:is_snowing positioned ~ ~-1 ~ if block ~ ~ ~ #seasons:snowable_plants run function seasons:snow_on_plants
