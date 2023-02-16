scoreboard players set branch_z_8 _seasons 0
execute if score z _seasons matches ..-8 run scoreboard players set branch_z_8 _seasons -1
execute if score z _seasons matches 8.. run scoreboard players set branch_z_8 _seasons 1

execute if score branch_z_8 _seasons matches -1 run scoreboard players add z _seasons 8
execute if score branch_z_8 _seasons matches 1 run scoreboard players remove z _seasons 8

execute if score branch_z_8 _seasons matches -1 positioned ~ ~ ~-8 run function seasons:generated/move/z4
execute if score branch_z_8 _seasons matches 0 run function seasons:generated/move/z4
execute if score branch_z_8 _seasons matches 1 positioned ~ ~ ~8 run function seasons:generated/move/z4
scoreboard players reset branch_z_8 _seasons
