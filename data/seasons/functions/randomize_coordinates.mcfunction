# Randomize x and z coordinates -127..127 into $(destination)

function seasons:randomizecoordinate
$execute store result $(destination) x int 1 run scoreboard players get Random _seasons
function seasons:randomizecoordinate
$execute store result $(destination) z int 1 run scoreboard players get Random _seasons
