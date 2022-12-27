scoreboard players operation Random _seasons *= 2 _seasons
execute if predicate seasons:random_chance run scoreboard players add Random _seasons 1
scoreboard players remove RandomBits _seasons 1
execute if score RandomBits _seasons matches 1.. run function seasons:random_r
