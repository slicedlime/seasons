# Update biomes
execute if score UpdateRandom _seasons matches 0 if score SeasonRandom _seasons matches 2..3 run function seasons:generated/set_fall_early
execute if score UpdateRandom _seasons matches 0 if score SeasonRandom _seasons matches 0..1 run function seasons:generated/set_fall_late
