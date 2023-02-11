scoreboard players set branch _seasons 0
execute if score z _seasons matches ..-64 run scoreboard players set branch _seasons -1
execute if score z _seasons matches 64.. run scoreboard players set branch _seasons 1

execute if score branch _seasons matches -1 run scoreboard players add z _seasons 64
execute if score branch _seasons matches 1 run scoreboard players remove z _seasons 64

execute if score branch _seasons matches -1 positioned ~ ~ ~-64 run function seasons:generated/move/z32
execute if score branch _seasons matches 0 run function seasons:generated/move/z32
execute if score branch _seasons matches 1 positioned ~ ~ ~64 run function seasons:generated/move/z32
