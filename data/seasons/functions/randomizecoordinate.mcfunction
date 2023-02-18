# Generate a number between -112 and +112 into [Random _seasons]

scoreboard players set RandomBits _seasons 8
function seasons:random
scoreboard players remove Random _seasons 128
