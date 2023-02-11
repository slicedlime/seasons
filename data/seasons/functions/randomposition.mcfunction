# Move @s to a random location within 112 blocks on either axis

function seasons:randomizecoordinate
scoreboard players operation x _seasons = Random _seasons
function seasons:randomizecoordinate
scoreboard players operation z _seasons = Random _seasons

function seasons:generated/move/z64
scoreboard players reset x _seasons
scoreboard players reset z _seasons
scoreboard players reset branch _seasons

execute at @s store success score spread _seasons run spreadplayers ~ ~ 0 1 false @s
execute if score spread _seasons matches 0 positioned ~ 319 ~ run function seasons:findsurface
scoreboard players reset spread _seasons
scoreboard players reset Random _seasons
