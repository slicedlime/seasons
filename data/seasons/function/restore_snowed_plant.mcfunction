execute if entity @s[nbt={data:{on_grass:1}}] if block ~ ~-1 ~ dirt run setblock ~ ~-1 ~ grass_block
function seasons:generated/restore_snow_marker
kill @s
