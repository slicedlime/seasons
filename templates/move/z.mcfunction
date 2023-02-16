scoreboard players set branch_z_$max _seasons 0
execute if score z _seasons matches ..-$max run scoreboard players set branch_z_$max _seasons -1
execute if score z _seasons matches $max.. run scoreboard players set branch_z_$max _seasons 1

execute if score branch_z_$max _seasons matches -1 run scoreboard players add z _seasons $max
execute if score branch_z_$max _seasons matches 1 run scoreboard players remove z _seasons $max

execute if score branch_z_$max _seasons matches -1 positioned ~ ~ ~-$max run $payload
execute if score branch_z_$max _seasons matches 0 run $payload
execute if score branch_z_$max _seasons matches 1 positioned ~ ~ ~$max run $payload
scoreboard players reset branch_z_$max _seasons
