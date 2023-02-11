scoreboard players set branch _seasons 0
execute if score z _seasons matches ..-2 run scoreboard players set branch _seasons -1
execute if score z _seasons matches 2.. run scoreboard players set branch _seasons 1

execute if score branch _seasons matches -1 run scoreboard players add z _seasons 2
execute if score branch _seasons matches 1 run scoreboard players remove z _seasons 2

execute if score branch _seasons matches -1 positioned ~ ~ ~-2 run function seasons:generated/move/z1
execute if score branch _seasons matches 0 run function seasons:generated/move/z1
execute if score branch _seasons matches 1 positioned ~ ~ ~2 run function seasons:generated/move/z1
