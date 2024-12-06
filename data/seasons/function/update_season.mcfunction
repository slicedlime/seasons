# Update the current position to be the current biome

execute store result score SeasonRandom _seasons run random value 0..3
execute store result score UpdateRandom _seasons run random value 0..3

# Debug:
#scoreboard players set UpdateRandom _seasons 0
#particle end_rod ~ ~2 ~ 0 0 0 0 0

execute if score Season _seasons matches 0 run function seasons:update_summer
execute if score Season _seasons matches 1 run function seasons:update_fall
execute if score Season _seasons matches 2 run function seasons:update_winter
execute if score Season _seasons matches 3 run function seasons:update_spring

scoreboard players reset SeasonRandom _seasons
scoreboard players reset UpdateRandom _seasons
