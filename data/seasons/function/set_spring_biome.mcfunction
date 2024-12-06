function seasons:check_surrounding_snow

execute if score Snow _seasons matches 0 if score SeasonRandom _seasons matches 1..3 run function seasons:generated/set_spring_default
execute if score Snow _seasons matches 0 if score SeasonRandom _seasons matches 0 run function seasons:generated/set_spring_flowering

scoreboard players reset Snow _seasons
