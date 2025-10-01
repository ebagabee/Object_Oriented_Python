# Dragons

In "Age of Dragons" there are Orcs, Humans, Goblins, Dragons, etc. All of those different creatures are called "units". The only thing specific to a unit is that it has a `position` on the game map (x and y coordinates) and a `name`.

Dragons are a specific type of unit. They can breathe fire in a large area dealing damage to any units touched by its fiery blaze.

## The Game Grid

Our game map is just a [Cartesian plane](https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

![](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/Gb4m8LE.png)

## Example of Fire Breath

![](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/BH4Vn3Z-600x396.png)

The example above uses a `__fire_range` of `1` centered at `(1, 1)`.

## Assignment

**Complete the following methods**:

1. [ ] Complete the unit's `in_area` method. It accepts an "area" represented by four points: `x_1`, `y_1`, `x_2`, and `y_2`. The coordinates `x_1` and `y_1` represent the bottom-left corner, while `x_2` and `y_2` represent the top-right corner.
   1. [ ] Determine if the unit is within the given area by using the unit's position coordinates `pos_x` and `pos_y`.
   2. [ ] Return `True` if the unit's position falls *inside or on the edge of* the rectangle. Otherwise, return `False`.
2. [ ] Complete the dragon's `breathe_fire` method. It causes the dragon to breathe a swath of fire at the target area.
   1. [ ] The target area is centered at `(x, y)`. The area stretches for `__fire_range` in both directions *inclusively*.
   2. [ ] Iterate over each unit in the `units` list, and check if the unit is in the area. If it is, add it to a new list that keeps track of the units hit by the blast.
   3. [ ] Return the list of units hit by the blast.
