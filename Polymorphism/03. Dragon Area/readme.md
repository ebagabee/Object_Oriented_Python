# Dragon Area

Our `Unit` class has its simple version of `in_area` - it just checks if the *center point* of the unit is within the given area. But the Dragon is a big creature, and it doesn't make sense to check if a single point is within the area. So, we'll use a *hit box* instead!

This is the current behavior:

![](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/BH4Vn3Z.png)

We want to change it so that a dragon is within an area if its hit box overlaps with it:

![](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/cVTThOL-530x400.png)

Since `Dragon` is a child class of `Unit`, it can *override* the `in_area` of the `Unit` class with its own *behavior*. Yay polymorphism! The `Dragon` still acts like a `Unit` (has an `in_area` method), but it has its own implementation.

## Assignment

1. [ ] Complete the Dragon's constructor:
   1. [ ] Call constructor of the `Unit` class with the provided parameters
   2. [ ] Set the dragon-specific parameters as instance variables
   3. [ ] Create a new private `__hit_box` member. It's a `Rectangle` object representing the dragon's hit box. *See the tips below if you need help*.
2. [ ] Override the `in_area` method in the `Dragon` class:
   1. [ ] Create a new rectangle object with the given corner positions.
   2. [ ] Use the rectangle's `overlaps` method to check if the Dragon's `self.__hit_box` is inside it, and return the result.

The given `pos_x` and `pos_y` for any unit is the center point of that unit!

## Tips

- The [`super()`](https://docs.python.org/3/library/functions.html#super) function allows you to call methods of a parent class.
- To calculate the Dragon's hit box:
  - `x1` should be the dragon's `pos_x` (center x) minus half of its width.
  - `y1` should be the dragon's `pos_y` (center y) minus half of its height.
  - `x2` should be the dragon's `pos_x` (center x) plus half of its width.
  - `y2` should be the dragon's `pos_y` (center y) plus half of its height.
