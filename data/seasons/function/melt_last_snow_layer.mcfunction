setblock ~ ~ ~ air
execute align xyz positioned ~0.5 ~0.5 ~0.5 as @e[type=marker,tag=_seasons_snow,distance=..0.0001] at @s run function seasons:check_snowed_plant
