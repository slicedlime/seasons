# Do block-based spread functions

kill @e[type=marker,tag=seasons_spreader]
summon marker ~ ~ ~ {Tags:["seasons_spreader"]}
execute as @e[type=marker,tag=seasons_spreader] at @s run function seasons:randomposition
execute as @e[type=marker,tag=seasons_spreader] at @s run function seasons:update_season_blocks

kill @e[type=marker,tag=seasons_spreader]
