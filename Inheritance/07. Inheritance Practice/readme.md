# Inheritance Practice

Siege weapons (battering rams, catapults, etc.) are special units in Age of Dragons. Let's write the logic for how they move around the map.

## Assignment

Complete the `Siege`, `BatteringRam`, and `Catapult` classes:

1. [ ] Complete the `Siege` class:
   1. [ ] Complete the constructor. It accepts two parameters (in order) and sets them as public instance variables with the same name: `max_speed` and `efficiency`
   2. [ ] Complete the `get_trip_cost()` method. It calculates the cost of a trip and returns it. The formula for calculating the cost is: `(distance / efficiency) * food_price`. *It costs food to move siege weapons, those things are heavy!*
   3. [ ] Leave the `get_cargo_volume()` method as empty. Use the [`pass`](https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement) keyword. Child classes will override this method.
2. [ ] Complete the `BatteringRam` class:
   1. [ ] Complete the constructor. It calls the parent constructor, then sets the extra battering-ram-only instance variables as member variables.
   2. [ ] The `get_trip_cost()` method uses the parent `get_trip_cost()` method to calculate the cost of food for a trip, plus the extra cost of carrying a load. The formula for calculating the cost: `get_trip_cost() + (load_weight * 0.01)`
   3. [ ] The `get_cargo_volume()` method calculates and returns the cargo capacity in cubic meters. To get the volume of the battering-ram's 'cargo' (`bed_area`), multiply its area by its depth, which is always 2 meters.
3. [ ] Complete the `Catapult` class:
   1. [ ] The constructor calls the parent constructor, then sets the extra catapult-only instance variable as a member variable.
   2. [ ] Do not override the `get_trip_cost()` method. It's inherited from the parent class.
   3. [ ] The `get_cargo_volume()` method just returns the cargo capacity of the catapult. This is already set by the constructor.

## Tips

You know this already: the [super()](https://docs.python.org/3/library/functions.html#super) method returns a proxy of the parent class, so use it to call the parent class's constructor and other methods.
