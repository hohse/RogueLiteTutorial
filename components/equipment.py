from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Actor, Item

# To sum up, this component holds references to equippable entities, calculates the bonuses the player gets from them (which will get added to the player’s power and defense values), and gives a way to equip or remove the items.

class Equipment(BaseComponent):
    parent: Actor

    # The weapon and armor attributes are what will hold the actual equippable entity. Both can be set to None, which represents nothing equipped in those slots. Feel free to add more slots as you see fit (perhaps you want armor to be head, body, legs, etc. instead, or allow for off-hand weapons/shields).
    def __init__(self, weapon: Optional[Item] = None, armor: Optional[Item] = None):
        self.weapon = weapon
        self.armor = armor

    # These properties do the same thing, just for different things. Both calculate the “bonus” gifted by equipment to either defense or power, based on what’s equipped. Notice that we take the “power” bonus from both weapons and armor, and the same applies to the “defense” bonus. This allows you to create weapons that increase both attack and defense (maybe some sort of spiked shield) and armor that increases attack (something magical, maybe). We won’t do that in this tutorial (weapons will only increase power, armor will only increase defense), but you should experiment with different equipment types on your own.
    @property
    def defense_bonus(self) -> int:
        bonus = 0

        if self.weapon is not None and self.weapon.equippable is not None:
            bonus += self.weapon.equippable.defense_bonus

        if self.armor is not None and self.armor.equippable is not None:
            bonus += self.armor.equippable.defense_bonus

        return bonus

    @property
    def power_bonus(self) -> int:
        bonus = 0

        if self.weapon is not None and self.weapon.equippable is not None:
            bonus += self.weapon.equippable.power_bonus

        if self.armor is not None and self.armor.equippable is not None:
            bonus += self.armor.equippable.power_bonus

        return bonus

    def item_is_equipped(self, item: Item) -> bool:
        return self.weapon == item or self.armor == item

    def unequip_message(self, item_name: str) -> None:
        self.parent.gamemap.engine.message_log.add_message(
            f"You remove the {item_name}."
        )

    def equip_message(self, item_name: str) -> None:
        self.parent.gamemap.engine.message_log.add_message(
            f"You equip the {item_name}."
        )

    def equip_to_slot(self, slot: str, item: Item, add_message: bool) -> None:
        current_item = getattr(self, slot)

        if current_item is not None:
            self.unequip_from_slot(slot, add_message)

        setattr(self, slot, item)

        if add_message:
            self.equip_message(item.name)

    def unequip_from_slot(self, slot: str, add_message: bool) -> None:
        current_item = getattr(self, slot)

        if add_message:
            self.unequip_message(current_item.name)

        setattr(self, slot, None)

    # Finally, we have toggle_equip, which is the method that will actually get called when the player selects an equippable item. It checks the equipment’s type (to know which slot to put it in), and then checks to see if the same item is already equipped to that slot. If it is, the player presumably wants to remove it. If not, the player wants to equip it.
    def toggle_equip(self, equippable_item: Item, add_message: bool = True) -> None:
        if (
            equippable_item.equippable
            and equippable_item.equippable.equipment_type == EquipmentType.WEAPON
        ):
            slot = "weapon"
        else:
            slot = "armor"

        if getattr(self, slot) == equippable_item:
            self.unequip_from_slot(slot, add_message)
        else:
            self.equip_to_slot(slot, equippable_item, add_message)