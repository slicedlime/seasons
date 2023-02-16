scoreboard players set branch_x_$max _seasons 0
execute if score x _seasons matches ..-$max run scoreboard players set branch_x_$max _seasons -1
execute if score x _seasons matches $max.. run scoreboard players set branch_x_$max _seasons 1

execute if score branch_x_$max _seasons matches -1 run scoreboard players add x _seasons $max
execute if score branch_x_$max _seasons matches 1 run scoreboard players remove x _seasons $max

execute if score branch_x_$max _seasons matches -1 positioned ~-$max ~ ~ run $payload
execute if score branch_x_$max _seasons matches 0 run $payload
execute if score branch_x_$max _seasons matches 1 positioned ~$max ~ ~ run $payload
scoreboard players reset branch_x_$max _seasons
