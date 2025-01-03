# Randomize x and z coordinates -Range..Range into $(destination) - range value copied from scoreboard each tick
$data modify storage seasons:random destination set value "$(destination)"
function seasons:randomize_coordinates_internal with storage seasons:random