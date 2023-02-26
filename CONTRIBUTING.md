## Contributing

Pull requests and bug reports are accepted, although I retain the right to choose what type of
design changes to include. Make sure to include full descriptions of changes.

If you fork this and make your own version of it, please retain some form of credit to slicedlime,
and please consider making pull requests for fixes upstream.


## Developing

If you want to develop your own modifications to the pack, you might need to modify and/or run the
generator. This requires that you have python 3 installed, as well as libraries used:

`pip3 install imageio`

If you don't have python installed on your system, you can set up  a portable conda-based distribution
such as [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) and then create
a dedicated development environment by nagivating to the root folder of this project and running:

```bash
$ mamba env create
```
(subsitute `conda` if needed).

You can then activate that environment using:

```bash
$ conda activate seasons
```


## Building

Building the pack requires some vanilla files to derive the default values from. Create a 'vanilla' folder and
copy the default 'foliage.png' and 'grass.png' files from the vanilla resource pack into it. Then
copy the entire 'worldgen/biome' folder from the vanilla data pack into the folder as 'biome'.

Run the script without any arguments:

`python build.py`
