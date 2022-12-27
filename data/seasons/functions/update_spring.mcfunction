# Update biomes
fillbiome ~ -64 ~ ~ 319 ~ seasons:winter_melting/forest replace seasons:winter_snowy/forest
execute positioned ~ ~-1 ~ if block ~ ~ ~ #seasons:meltables run function seasons:melt

execute if score UpdateRandom _seasons matches 0 if block ~ ~ ~ air run function seasons:set_spring_biome
