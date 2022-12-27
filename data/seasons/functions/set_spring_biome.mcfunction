function seasons:check_surrounding_snow

execute if score Snow _seasons matches 0 if score SeasonRandom _seasons matches 1..3 run fillbiome ~ -64 ~ ~ 319 ~ seasons:spring_default/forest replace #seasons:non_spring/forest
execute if score Snow _seasons matches 0 if score SeasonRandom _seasons matches 0 run fillbiome ~ -64 ~ ~ 319 ~ seasons:spring_flowering/forest replace #seasons:non_spring/forest

scoreboard players reset Snow _seasons
