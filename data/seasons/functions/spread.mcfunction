# Spread the current season around the current location

# If, for some reason, we end up overruning the command limit, that snowballs out of control with
# more and more entities, so for safety, make sure we kill before we start
kill @e[type=marker,tag=seasons_spreader]
summon marker ~ ~ ~ {Tags:["seasons_spreader"]}
spreadplayers ~ ~ 0 112 false @e[type=marker,tag=seasons_spreader]
# Debug:
#spreadplayers ~ ~ 0 32 false @e[type=marker,tag=seasons_spreader]

execute as @e[type=marker,tag=seasons_spreader] at @s run function seasons:update_season
execute as @e[type=marker,tag=seasons_spreader] at @s run function seasons:check_snowed_plants

kill @e[type=marker,tag=seasons_spreader]
