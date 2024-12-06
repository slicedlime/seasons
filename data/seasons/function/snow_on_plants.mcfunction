# Make snow layers replace replaceable plants, store data in markers

function seasons:generated/create_snow_marker
execute if block ~ ~-1 ~ grass_block align zxy run data modify entity @e[type=marker,distance=..1,tag=_seasons_new_snow,limit=1] data.on_grass set value 1

execute if entity @e[type=marker,tag=_seasons_new_snow] run setblock ~ ~ ~ snow
tag @e[type=marker,tag=_seasons_new_snow] remove _seasons_new_snow
