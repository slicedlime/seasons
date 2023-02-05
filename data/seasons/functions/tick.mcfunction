# Main tick for the seasons pack

scoreboard players operation YearLength _seasons = SeasonLength _seasons
scoreboard players operation YearLength _seasons *= SeasonCount _seasons

execute store result score Day _seasons run time query day

scoreboard players operation Day _seasons %= YearLength _seasons
scoreboard players operation Season _seasons = Day _seasons
scoreboard players operation Season _seasons /= SeasonLength _seasons

scoreboard players operation ToSpread _seasons = SpreadSpeed _seasons
function seasons:spread_r
scoreboard players reset ToSpread _seasons

execute as @a at @s run function seasons:check_snowed_plants
