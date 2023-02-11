scoreboard players set branch _seasons 0
execute if score x _seasons matches ..-2 run scoreboard players set branch _seasons -1
execute if score x _seasons matches 2.. run scoreboard players set branch _seasons 1

execute if score branch _seasons matches -1 run scoreboard players add x _seasons 2
execute if score branch _seasons matches 1 run scoreboard players remove x _seasons 2

execute if score branch _seasons matches -1 positioned ~-2 ~ ~ run function seasons:generated/move/x1
execute if score branch _seasons matches 0 run function seasons:generated/move/x1
execute if score branch _seasons matches 1 positioned ~2 ~ ~ run function seasons:generated/move/x1
