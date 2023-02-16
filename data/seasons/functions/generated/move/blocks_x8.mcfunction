scoreboard players set branch_x_8 _seasons 0
execute if score x _seasons matches ..-8 run scoreboard players set branch_x_8 _seasons -1
execute if score x _seasons matches 8.. run scoreboard players set branch_x_8 _seasons 1

execute if score branch_x_8 _seasons matches -1 run scoreboard players add x _seasons 8
execute if score branch_x_8 _seasons matches 1 run scoreboard players remove x _seasons 8

execute if score branch_x_8 _seasons matches -1 positioned ~-8 ~ ~ run function seasons:generated/move/blocks_x4
execute if score branch_x_8 _seasons matches 0 run function seasons:generated/move/blocks_x4
execute if score branch_x_8 _seasons matches 1 positioned ~8 ~ ~ run function seasons:generated/move/blocks_x4
scoreboard players reset branch_x_8 _seasons
