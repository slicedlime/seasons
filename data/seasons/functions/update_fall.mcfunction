# Update biomes
execute if score UpdateRandom _seasons matches 0 if score SeasonRandom _seasons matches 2..3 run fillbiome ~ -64 ~ ~ 319 ~ seasons:fall_early/forest replace #seasons:non_fall/forest
execute if score UpdateRandom _seasons matches 0 if score SeasonRandom _seasons matches 0..1 run fillbiome ~ -64 ~ ~ 319 ~ seasons:fall_late/forest replace #seasons:non_fall/forest

execute positioned ~ ~-1 ~ if block ~ ~ ~ snow run function seasons:melt_snow
