execute as @e[type=marker,distance=..10,tag=_seasons_snow] at @s if block ~ ~ ~ air run function seasons:restore_snowed_plant
execute as @e[type=marker,distance=..10,tag=_seasons_snow] at @s unless block ~ ~ ~ snow run function seasons:pop_snowed_plant
