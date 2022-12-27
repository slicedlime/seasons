scoreboard players set $Snow _seasons 0
execute if block ~-1 ~-1 ~-1 snow run scoreboard players add $Snow _seasons 1
execute if block ~-1 ~-1 ~ snow run scoreboard players add $Snow _seasons 1
execute if block ~-1 ~-1 ~1 snow run scoreboard players add $Snow _seasons 1
execute if block ~-1 ~ ~-1 snow run scoreboard players add $Snow _seasons 1
execute if block ~-1 ~ ~ snow run scoreboard players add $Snow _seasons 1
execute if block ~-1 ~ ~1 snow run scoreboard players add $Snow _seasons 1
execute if block ~-1 ~1 ~-1 snow run scoreboard players add $Snow _seasons 1
execute if block ~-1 ~1 ~ snow run scoreboard players add $Snow _seasons 1
execute if block ~-1 ~1 ~1 snow run scoreboard players add $Snow _seasons 1
execute if block ~ ~-1 ~-1 snow run scoreboard players add $Snow _seasons 1
execute if block ~ ~-1 ~ snow run scoreboard players add $Snow _seasons 1
execute if block ~ ~-1 ~1 snow run scoreboard players add $Snow _seasons 1
execute if block ~ ~ ~-1 snow run scoreboard players add $Snow _seasons 1
execute if block ~ ~ ~ snow run scoreboard players add $Snow _seasons 1
execute if block ~ ~ ~1 snow run scoreboard players add $Snow _seasons 1
execute if block ~ ~1 ~-1 snow run scoreboard players add $Snow _seasons 1
execute if block ~ ~1 ~ snow run scoreboard players add $Snow _seasons 1
execute if block ~ ~1 ~1 snow run scoreboard players add $Snow _seasons 1
execute if block ~1 ~-1 ~-1 snow run scoreboard players add $Snow _seasons 1
execute if block ~1 ~-1 ~ snow run scoreboard players add $Snow _seasons 1
execute if block ~1 ~-1 ~1 snow run scoreboard players add $Snow _seasons 1
execute if block ~1 ~ ~-1 snow run scoreboard players add $Snow _seasons 1
execute if block ~1 ~ ~ snow run scoreboard players add $Snow _seasons 1
execute if block ~1 ~ ~1 snow run scoreboard players add $Snow _seasons 1
execute if block ~1 ~1 ~-1 snow run scoreboard players add $Snow _seasons 1
execute if block ~1 ~1 ~ snow run scoreboard players add $Snow _seasons 1
execute if block ~1 ~1 ~1 snow run scoreboard players add $Snow _seasons 1

execute if biome ~ ~ ~ seasons:winter_bare/forest run scoreboard players set $Snow _seasons 0

execute if score $Snow _seasons matches 0 if score SeasonRandom _seasons matches 1..3 run fillbiome ~ -64 ~ ~ 319 ~ seasons:spring_default/forest replace #seasons:non_spring/forest
execute if score $Snow _seasons matches 0 if score SeasonRandom _seasons matches 0 run fillbiome ~ -64 ~ ~ 319 ~ seasons:spring_flowering/forest replace #seasons:non_spring/forest

scoreboard players reset $Snow _seasons
