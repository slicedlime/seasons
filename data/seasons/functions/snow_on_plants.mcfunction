# Make snow layers replace replaceable plants, store data in markers

execute if block ~ ~ ~ grass align zxy run summon marker ~0.5 ~0.5 ~0.5 {Tags:["_seasons_snow","_seasons_new_snow"], data: {block: "grass"}, CustomName:'"Snowed Plant"'}

execute if entity @e[type=marker,tag=_seasons_new_snow] run setblock ~ ~ ~ snow
tag @e[type=marker,tag=_seasons_new_snow] remove _seasons_new_snow
