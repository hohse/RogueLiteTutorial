from enum import auto, Enum

# An “Enum” is a set of named values that won’t change, so it’s perfect for things like this. auto assigns incrementing integer values automatically, so we don’t need to retype them if we add more values later on.
class RenderOrder(Enum):
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()