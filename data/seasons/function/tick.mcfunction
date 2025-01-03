# Main tick for the seasons pack

scoreboard players operation YearLength _seasons = SeasonLength _seasons
scoreboard players operation YearLength _seasons *= SeasonCount _seasons

execute store result score Day _seasons run time query day
execute store result storage seasons:random range int 16 run scoreboard players get Range _seasons

scoreboard players operation Day _seasons %= YearLength _seasons
scoreboard players operation Season _seasons = Day _seasons
scoreboard players operation Season _seasons /= SeasonLength _seasons

scoreboard players operation ToSpread _seasons = SpreadSpeed _seasons
function seasons:spread_r
scoreboard players reset ToSpread _seasons
scoreboard players operation ToSpread _seasons = BlockSpeed _seasons
function seasons:spread_blocks_r
scoreboard players reset ToSpread _seasons

execute as @a at @s run function seasons:check_snowed_plants
