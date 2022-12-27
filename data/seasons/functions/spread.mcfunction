# Spread the current season around the current location

summon marker ~ ~ ~ {Tags:["seasons_spreader"]}
spreadplayers ~ ~ 0 112 false @e[type=marker,tag=seasons_spreader]
#spreadplayers ~ ~ 0 32 false @e[type=marker,tag=seasons_spreader]

execute as @e[type=marker,tag=seasons_spreader] at @s run function seasons:update_season

kill @e[type=marker,tag=seasons_spreader]
