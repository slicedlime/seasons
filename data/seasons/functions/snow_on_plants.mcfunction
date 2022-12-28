# Make snow layers replace replaceable plants, store data in markers

function seasons:generated/create_snow_marker

execute if entity @e[type=marker,tag=_seasons_new_snow] run setblock ~ ~ ~ snow
tag @e[type=marker,tag=_seasons_new_snow] remove _seasons_new_snow
