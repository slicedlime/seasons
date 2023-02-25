## Contributing

Pull requests and bug reports are accepted, although I retain the right to choose what type of
design changes to include. Make sure to include full descriptions of changes.

If you fork this and make your own version of it, please retain some form of credit to slicedlime,
and please consider making pull requests for fixes upstream.

## Developing

If you want to develop your own modifications to the pack, you might need to modify and/or run the
generator. This requires that you have python 3 installed, as well as libraries used:

`pip3 install imageio`

It requires some vanilla files to derive the default values from. Create a 'vanilla' folder and
copy the default 'foliage.png' and 'grass.png' files from the vanilla resource pack into it. Then
copy the entire 'worldgen/biome' folder from the vanilla data pack into the folder as 'biome'.

Run the script without any arguments:

`python build.py`
