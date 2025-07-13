from typing import Tuple

import numpy as np  # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb.

# ch: The character, represented in integer format. We’ll translate it from the integer into Unicode.
# fg: The foreground color. “3B” means 3 unsigned bytes, which can be used for RGB color codes.
# bg: The background color. Similar to fg.

graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data.

# walkable: A boolean that describes if the player can walk across this tile.
# transparent: A boolean that describes if this tile does or does not block the field of view. Not used in this chapter, but will be in chapter 4.
# dark: This uses our previously defined dtype, which holds the character to print, the foreground color, and the background color. Why is it called dark? Because later on, we’ll want to differentiate between tiles that are and aren’t in the field of view. dark will represent tiles that are not in the current field of view. Again, we’ll cover that in part 4.
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked over.
        ("transparent", np.bool),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
        ("light", graphic_dt),  # Graphics for when the tile is in FOV.
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

# floor is both walkable and transparent. Its dark attribute consists of the space character (feel free to change this to something else, a lot of roguelikes use “#”) and defines its foreground color as white (won’t matter since it’s an empty space) and a background color.
floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (214, 134, 66)), # bissel dunkler als sandy brown
    light=(ord(" "), (255, 255, 255), (244, 164, 96)), # sandy brown
)

wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (102, 51, 0)), # bissel dunkler als saddle brown?
    light=(ord(" "), (255, 255, 255), (139, 69, 19)), # saddle brown
)

down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(">"), (0, 0, 100), (51, 25, 150)),
    light=(ord(">"), (255, 255, 255), (90, 55, 19)),
)