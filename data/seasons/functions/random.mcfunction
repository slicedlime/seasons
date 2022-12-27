# Generate [RandomBits _seasons] bits of randomness into Random

scoreboard players set 2 _seasons 2
scoreboard players set Random _seasons 0

function seasons:random_r

scoreboard players reset 2 _seasons
scoreboard players reset RandomBits _seasons
