# Update biomes
execute if block ~ ~-1 ~ snow run fillbiome ~ -64 ~ ~ 319 ~ seasons:winter_snowy/forest replace #seasons:non_winter/forest
execute unless block ~ ~-1 ~ snow if score UpdateRandom _seasons matches 0 run fillbiome ~ -64 ~ ~ 319 ~ seasons:winter_bare/forest replace #seasons:non_winter/forest
#execute unless block ~ ~-1 ~ snow if score UpdateRandom _seasons matches 1.. run fillbiome ~ -64 ~ ~ 319 ~ seasons:winter_bare/forest replace #seasons:non_winter/forest
