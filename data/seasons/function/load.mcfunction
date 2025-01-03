# On load

scoreboard objectives add _seasons dummy "Seasons Data"
scoreboard players add SeasonLength _seasons 0
execute if score SeasonLength _seasons matches 0 run scoreboard players set SeasonLength _seasons 20
scoreboard players set SeasonCount _seasons 4
scoreboard players add SpreadSpeed _seasons 0
execute if score SpreadSpeed _seasons matches 0 run scoreboard players set SpreadSpeed _seasons 1
scoreboard players add BlockSpeed _seasons 0
execute if score BlockSpeed _seasons matches 0 run scoreboard players set BlockSpeed _seasons 8
scoreboard players add Range _seasons 0
execute if score Range _seasons matches 0 run scoreboard players set Range _seasons 12

gamerule snowAccumulationHeight 8
