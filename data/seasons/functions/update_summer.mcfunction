# Update biomes
execute if score UpdateRandom _seasons matches 0 run function seasons:generated/set_summer

execute positioned ~ ~-1 ~ if block ~ ~ ~ #seasons:meltables run function seasons:melt
