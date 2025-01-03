# Do block-based spread functions

function seasons:randomize_coordinates {destination:"storage seasons:update_data"}
# Now have -Range..Range in x and z
data modify storage seasons:update_data payload set value "function seasons:update_season_blocks"
function seasons:project_and_run with storage seasons:update_data
function seasons:randomcleanup
