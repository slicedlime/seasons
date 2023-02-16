# Spread the current season around the current location

# If, for some reason, we end up overruning the command limit, that snowballs out of control with
# more and more entities, so for safety, make sure we kill before we start
kill @e[type=marker,tag=seasons_spreader]
summon marker ~ ~ ~ {Tags:["seasons_spreader"]}
execute as @e[type=marker,tag=seasons_spreader] at @s run function seasons:randomposition
execute as @e[type=marker,tag=seasons_spreader] at @s run function seasons:update_season

kill @e[type=marker,tag=seasons_spreader]
