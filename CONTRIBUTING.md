## Contributing

Pull requests and bug reports are accepted, although I retain the right to choose what type of
design changes to include. Make sure to include full descriptions of changes.

If you fork this and make your own version of it, please retain some form of credit to slicedlime,
and please consider making pull requests for fixes upstream.


## Developing

If you want to develop your own modifications to the pack, you might need to modify and/or run the
generator. This requires that you have python 3 installed, as well as the `imageio` library, which you
can install via:

```bash
$ python3 -m pip install imageio
```

If you don't have python or pip installed on your system, you can set up a portable conda-based distribution
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

Building the pack requires some vanilla files to derive the default values from (as they are copyrighted
parts of the official game they cannot be included in this repo).

1. Start by creating a folder named `vanilla` in the project root.
1. Then find a copy of the default / vanilla resource pack and extract the files `foliage.pnmg` and `grass.png`
from the `textures/colormap` folder and place them directly in the `vanilla` directory. These can be found
within the minecraft assets, but versions of the vanilla resource pack are commonly available, and as these
files change infrequently, it's not essential to have the most up-to-date version.
1. Next you'll need to obtain the `biome` folder from the default data pack. The easiest way to obtain
this is by extracting it directly from the Minecraft client JAR. **These files need to be from the same
version you'll be using your datapack with!** Within the Minecraft JAR, the `biome` folder can be found
within `data/minecraft/worlgen`. Extract the **entire folder** (including the `biome` folder itself) to
the `vanilla` folder in this repo.

Once you've obtained all the vanilla files and placed them in the right place,
run the build script without any arguments:

```bash
python build.py
```
