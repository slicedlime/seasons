execute as @a at @s run function seasons:spread
scoreboard players remove ToSpread _seasons 1
execute if score ToSpread _seasons matches 1.. run function seasons:spread_r
