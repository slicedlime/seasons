# Update biomes
function seasons:generated/set_winter_melting

execute if score UpdateRandom _seasons matches 0 if block ~ ~ ~ air run function seasons:set_spring_biome
