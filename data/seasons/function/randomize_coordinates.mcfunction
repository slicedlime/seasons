# Randomize x and z coordinates -127..127 into $(destination)
$execute store result $(destination) x int 1 run random value -127..127
$execute store result $(destination) z int 1 run random value -127..127
