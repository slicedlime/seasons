# Update biomes
fillbiome ~ -64 ~ ~ 319 ~ seasons:winter_melting/forest replace seasons:winter_snowy/forest
execute positioned ~ ~-1 ~ if block ~ ~ ~ snow run function seasons:melt_snow

execute if score UpdateRandom _seasons matches 0 if block ~ ~ ~ air run function seasons:set_spring_biome
