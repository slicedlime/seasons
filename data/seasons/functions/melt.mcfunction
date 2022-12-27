execute if block ~ ~ ~ snow[layers=1] if score Season _seasons matches 3 run function seasons:set_spring_biome
execute if block ~ ~ ~ snow[layers=1] run setblock ~ ~ ~ air
execute if block ~ ~ ~ snow[layers=2] run setblock ~ ~ ~ snow[layers=1]
execute if block ~ ~ ~ snow[layers=3] run setblock ~ ~ ~ snow[layers=2]
execute if block ~ ~ ~ snow[layers=4] run setblock ~ ~ ~ snow[layers=3]
execute if block ~ ~ ~ snow[layers=5] run setblock ~ ~ ~ snow[layers=4]
execute if block ~ ~ ~ snow[layers=6] run setblock ~ ~ ~ snow[layers=5]
execute if block ~ ~ ~ snow[layers=7] run setblock ~ ~ ~ snow[layers=6]
execute if block ~ ~ ~ snow[layers=8] run setblock ~ ~ ~ snow[layers=7]
execute if block ~ ~ ~ ice run setblock ~ ~ ~ frosted_ice
