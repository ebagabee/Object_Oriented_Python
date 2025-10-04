# Get Edges

In the last chapter we checked if a unit's `(x, y)` **point** was within a rectangle (the Dragon's breath). But units aren't really points - they have their own areas.

So we're going to check if a dragon's body (a rectangle) is within the fire (also a rectangle). The image below contains an example of fire breath hitting a dragon.

![](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/cVTThOL-530x400.png)

Later we'll write the `overlap` method, but first we'll just write a method to find the edges of a rectangle.

## Assignment

We changed the coordinates themselves to be private by adding two underscores to them. We now need to write `getter` methods to access them.

**Complete the following methods**:

1. [ ] `get_left_x()`: Returns the leftmost (smallest) x value
2. [ ] `get_right_x()`: Returns the rightmost (largest) x value
3. [ ] `get_top_y()`: Returns the topmost (largest) y value
4. [ ] `get_bottom_y()`: Returns the bottom-most (smallest) y value

Remember that we're working with a standard [Cartesian plane](https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

We will explain the `__repr__` method later, don't worry too much about it.

## Tips

You may find Python's built-in [min](https://docs.python.org/3/library/functions.html#min) and [max](https://docs.python.org/3/library/functions.html#max) functions useful.
