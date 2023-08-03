# Spread the current season around the current location

# If, for some reason, we end up overruning the command limit, that snowballs out of control with
# more and more entities, so for safety, make sure we kill before we start
function seasons:randomize_coordinates {destination:"storage seasons:update_data"}
# Now have -127..127 in x and z
data modify storage seasons:update_data payload set value "function seasons:update_season"
function seasons:project_and_run with storage seasons:update_data
function seasons:randomcleanup
