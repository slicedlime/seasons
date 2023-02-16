scoreboard players set branch_x_64 _seasons 0
execute if score x _seasons matches ..-64 run scoreboard players set branch_x_64 _seasons -1
execute if score x _seasons matches 64.. run scoreboard players set branch_x_64 _seasons 1

execute if score branch_x_64 _seasons matches -1 run scoreboard players add x _seasons 64
execute if score branch_x_64 _seasons matches 1 run scoreboard players remove x _seasons 64

execute if score branch_x_64 _seasons matches -1 positioned ~-64 ~ ~ run function seasons:generated/move/blocks_x32
execute if score branch_x_64 _seasons matches 0 run function seasons:generated/move/blocks_x32
execute if score branch_x_64 _seasons matches 1 positioned ~64 ~ ~ run function seasons:generated/move/blocks_x32
scoreboard players reset branch_x_64 _seasons
