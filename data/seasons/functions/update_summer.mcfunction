# Update biomes
execute if score UpdateRandom _seasons matches 0 run fillbiome ~ -64 ~ ~ 319 ~ seasons:summer_default/forest replace #seasons:non_summer/forest

execute positioned ~ ~-1 ~ if block ~ ~ ~ snow run function seasons:melt_snow
