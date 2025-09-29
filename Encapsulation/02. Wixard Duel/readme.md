# Wizard Duel

Let's give our wizards the ability to launch fireballs *at each other*.

## Assignment

1. [ ] Complete the `cast_fireball` method:
   1. [ ] If there isn't enough mana to cast a fireball (based on the `fireball_cost` argument), `raise` an `Exception` with the message `____ cannot cast fireball`, where `____` is the wizard's name.
   2. [ ] If the wizard has enough mana, reduce their mana by the `fireball_cost` and call `get_fireballed` on the target wizard with the given `fireball_damage`.
2. [ ] Complete the `is_alive` method. It should return `True` if the wizard's health is greater than `0` and `False` otherwise.
