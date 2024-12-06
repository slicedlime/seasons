execute if block ~ ~ ~ air unless block ~ ~-1 ~ air run tag @s add _seasons_melting
execute if entity @s[tag=_seasons_melting] run function seasons:restore_snowed_plant
execute unless entity @s[tag=_seasons_melting] run function seasons:pop_snowed_plant
