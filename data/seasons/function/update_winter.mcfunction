# Update biomes
scoreboard players set Snow _seasons 0
execute if block ~ ~-1 ~ snow run scoreboard players set Snow _seasons 1
execute if block ~ ~ ~ snow run scoreboard players set Snow _seasons 1

execute if score Snow _seasons matches 1 run function seasons:generated/set_winter_snowy
execute unless score Snow _seasons matches 1 if score UpdateRandom _seasons matches 0 run function seasons:generated/set_winter_bare
scoreboard players reset Snow _seasons
