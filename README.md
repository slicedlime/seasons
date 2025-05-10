# Minecraft Seasons datapack

This is a datapack that adds seasonal shifts to vanilla Minecraft, made by slicedlime.

## Features

- Trees turn golden and red in the fall
- Rain turns to snow in the winter
- Snow covering trees turns leaves white
- Snow can cover small plants and flowers
- Rivers and some oceans freeze in the winter
- Snow and ice melts when winter has passed
- Leaves turn green with patches of pink flowering leaves in spring
- Sky colors shift slightly with seasons
- Wet and dry seasons in the savanna - when the summer rain season hits, the savanna comes alive
  in vibrant green
- Fully server-side - Multiplayer compatible and does not require a resource pack

## Compatibility

This datapack uses experimental world generation features to create seasonal variations of the
vanilla biomes. Because those features are experimental, the pack is expected to break with every
new version of Minecraft. It currently works with Minecraft 1.21.5 (and no other known version).

This also means that levels with the pack on will show a warning screen for of it using
experimental features.

Never try to upgrade a world using this pack without first checking for a new, compatible version
of the pack. This pack is currently in beta stage of development. Using it on worlds you care
about happens on your own risk.

**There is also no way to safely remove the pack**, so be sure you want to keep it when you install
it (or do so on a copy of the world). Removing the pack will replace all biomes where it has been
active with Plains.

### Performance

To keep track of some things like plants buried in snow, the pack uses marker entities. This means
it currently requires a reasonably capable computer to run.

The pack runs fully on the server side, so if you want to use it in Multiplayer, it will require a
strong server rather than a strong client computer. In multiplayer it also adds some network traffic,
so if you're playing in Multiplayer it will require a better network connection than the
corresponding world would without it.

Note that current versions of the pack are much more efficient than early versions were, both in
terms of CPU usage and network traffic.

### Mods and Other Packs

The pack should work with mods like shaders and optimization mods, but is unlikely to work together
with any mods that change world generation or any other datapacks that use experimental world
generation features.

### Commands

Because the pack replaces biomes, it will also mess with commands like `locate biome`. It also uses
the world time as the key for the season, so using commands like `time set <time>` will likely
reset the current season to Summer. Use `time add` instead to modify current time. As a special
case, `time add 20d` will fast-forward one season (using the default season length).

## Settings

You can modify the length of a a season, measured in in-game days (default: 20) with the following
command:

```mcfunction
/scoreboard players set SeasonLength _seasons <days>
```

To set the simulation distance used by the pack (default 12 chunks), run the following command:
```mcfunction
/scoreboard players set Range _seasons <chunks>
```

The number of season updates (full block column changing seasons - default: 1) and block updates
(things like plants snowing in, snow melting, etc - default: 8) done per tick can be configured
with the following:

```mcfunction
/scoreboard players set SpreadSpeed _seasons <count>
/scoreboard players set BlockSpeed _seasons <count>
```

## Design Notes

Each season is 20 in-game days as a compromise between the speed of seasons shifting and wanting
to be able to experience each season for a while before it shifts again.

Worlds always start in the summer, matching a normal Minecraft experience as much as possible -
although this does mean snowy vanilla biomes will melt and turn to summer when encountered.

The pack relies on snowy weather to get snow onto the ground, so if you skip the night every time
there is downfall, you'll see less snow in the winters.

Like vanilla Minecraft, this pack stays true to the world changing only around players. That means
seasons will slowly shift in the area around players. If you stay in the same place a long time and
then move, the place you move to will slowly start shifting directly to the current season.

Also like vanilla Minecraft, the pack stays true to the design idea that permanent changes to the
world should be player-driven. This means it attempts to avoid destructive changes - snow covers
flowers, but if that snow is broken, the flower drops. When the season changes, the flower
re-appears.

For the same reason, leaf blocks aren't replaced - their biome tint shifts. This means the leaves
that for some reason do not tint (like birch) do not show seasonal effects, and it also means there
is no way to obtain a "permanently winter-colored leaf block".

## Installing

This pack uses custom world generation features, so you'll get the "Experimental Features" warning
when you load a world with it. However, it doesn't actually change any world generation - biomes
are replaced as seasons shift. That means it can also be added to an already existing world.

Install on a new world by clicking the Data Packs button on the Create New World screen, then
drag and drop the zip file for the Seasons pack onto the Minecraft Window. This should make it show
up in the Available column.

Click the icon for the pack to move it to the Selected column, then hit Done. You will be warned
about the pack being experimental as you create the world.

### Installing on a pre-existing world

To install the pack on a pre-existing world, you'll need to copy the zip file for the pack to the
datapacks folder of the world folder. If you don't know where this is, click to Edit the world in
the Singleplayer Worlds list, then click the Open World Folder button.

Once the pack has been copied, you will need to close the world if you have it open, and it should
activate the next time the world is opened. On a server, you'll need to restart the server.

Note: `reload` is not sufficient to activate the pack, since it will not reload experimental
worldgen features.
