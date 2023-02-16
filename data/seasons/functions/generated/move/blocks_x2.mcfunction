scoreboard players set branch_x_2 _seasons 0
execute if score x _seasons matches ..-2 run scoreboard players set branch_x_2 _seasons -1
execute if score x _seasons matches 2.. run scoreboard players set branch_x_2 _seasons 1

execute if score branch_x_2 _seasons matches -1 run scoreboard players add x _seasons 2
execute if score branch_x_2 _seasons matches 1 run scoreboard players remove x _seasons 2

execute if score branch_x_2 _seasons matches -1 positioned ~-2 ~ ~ run function seasons:generated/move/blocks_x1
execute if score branch_x_2 _seasons matches 0 run function seasons:generated/move/blocks_x1
execute if score branch_x_2 _seasons matches 1 positioned ~2 ~ ~ run function seasons:generated/move/blocks_x1
scoreboard players reset branch_x_2 _seasons
