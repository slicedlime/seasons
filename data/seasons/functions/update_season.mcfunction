# Update the current position to be the current biome

scoreboard players set RandomBits _seasons 2
function seasons:random
scoreboard players operation SeasonRandom _seasons = Random _seasons
scoreboard players set RandomBits _seasons 4
function seasons:random
scoreboard players operation UpdateRandom _seasons = Random _seasons

# Debug:
#scoreboard players set UpdateRandom _seasons 0
#particle end_rod ~ ~2 ~ 0 0 0 0 0

execute if score Season _seasons matches 0 run function seasons:update_summer
execute if score Season _seasons matches 1 run function seasons:update_fall
execute if score Season _seasons matches 2 run function seasons:update_winter
execute if score Season _seasons matches 3 run function seasons:update_spring

scoreboard players reset Random _seasons
scoreboard players reset SeasonRandom _seasons
scoreboard players reset UpdateRandom _seasons
