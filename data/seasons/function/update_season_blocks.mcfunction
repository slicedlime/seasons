execute if score Season _seasons matches 0 run function seasons:update_summer_blocks
execute if score Season _seasons matches 1 run function seasons:update_non_winter_blocks
execute if score Season _seasons matches 2 run function seasons:update_winter_blocks
execute if score Season _seasons matches 3 run function seasons:update_non_winter_blocks
function seasons:check_snowed_plants
