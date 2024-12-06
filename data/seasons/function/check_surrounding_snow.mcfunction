# Set Snow in the _seasons scoreboard to indicate surrounging snow cover

scoreboard players set Snow _seasons 0
execute if block ~-1 ~-1 ~-1 snow run scoreboard players add Snow _seasons 1
execute if block ~-1 ~-1 ~ snow run scoreboard players add Snow _seasons 1
execute if block ~-1 ~-1 ~1 snow run scoreboard players add Snow _seasons 1
execute if block ~-1 ~ ~-1 snow run scoreboard players add Snow _seasons 1
execute if block ~-1 ~ ~ snow run scoreboard players add Snow _seasons 1
execute if block ~-1 ~ ~1 snow run scoreboard players add Snow _seasons 1
execute if block ~-1 ~1 ~-1 snow run scoreboard players add Snow _seasons 1
execute if block ~-1 ~1 ~ snow run scoreboard players add Snow _seasons 1
execute if block ~-1 ~1 ~1 snow run scoreboard players add Snow _seasons 1
execute if block ~ ~-1 ~-1 snow run scoreboard players add Snow _seasons 1
execute if block ~ ~-1 ~ snow run scoreboard players add Snow _seasons 1
execute if block ~ ~-1 ~1 snow run scoreboard players add Snow _seasons 1
execute if block ~ ~ ~-1 snow run scoreboard players add Snow _seasons 1
execute if block ~ ~ ~ snow run scoreboard players add Snow _seasons 1
execute if block ~ ~ ~1 snow run scoreboard players add Snow _seasons 1
execute if block ~ ~1 ~-1 snow run scoreboard players add Snow _seasons 1
execute if block ~ ~1 ~ snow run scoreboard players add Snow _seasons 1
execute if block ~ ~1 ~1 snow run scoreboard players add Snow _seasons 1
execute if block ~1 ~-1 ~-1 snow run scoreboard players add Snow _seasons 1
execute if block ~1 ~-1 ~ snow run scoreboard players add Snow _seasons 1
execute if block ~1 ~-1 ~1 snow run scoreboard players add Snow _seasons 1
execute if block ~1 ~ ~-1 snow run scoreboard players add Snow _seasons 1
execute if block ~1 ~ ~ snow run scoreboard players add Snow _seasons 1
execute if block ~1 ~ ~1 snow run scoreboard players add Snow _seasons 1
execute if block ~1 ~1 ~-1 snow run scoreboard players add Snow _seasons 1
execute if block ~1 ~1 ~ snow run scoreboard players add Snow _seasons 1
execute if block ~1 ~1 ~1 snow run scoreboard players add Snow _seasons 1
execute if biome ~ ~ ~ #seasons:bare_winter run scoreboard players set Snow _seasons 0
