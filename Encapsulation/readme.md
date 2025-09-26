# Encapsulation

[Encapsulation](<https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)>) is the practice of hiding complexity inside a ["black box"](https://en.wikipedia.org/wiki/Black_box) so that it's easier to focus on the problem at hand.

![](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/8gu3Y0s-964x544.png)

The simplest example of encapsulation is a function. The caller of a function doesn't need to worry too much about what happens inside, they just need to understand the inputs and outputs.

```py
# who even knows how this function works???
# I sure don't, I just call it and assume
# it calculates the acceleration correctly
acceleration = calc_acceleration(initial_speed, final_speed, time)
```

To *use* the `calc_acceleration` function, we don't need to think about each line of code inside the function definition. We just need to know that if we give it the inputs:

- `initial_speed`
- `final_speed`
- `time`

It will produce the correct `acceleration` as an output.

## Public and Private

By default, all properties and methods in a class are *public*. That means that you can access them with the `.` operator:

```python
wall.height = 10
print(wall.height)
# 10
```

[Private](https://docs.python.org/3/tutorial/classes.html#tut-private) data members are a way to encapsulate logic and data *within a class definition*. To make a property or method private just prefix it with two underscores:

```python
class Wall:
    def __init__(self, armor, magic_resistance):
        self.__armor = armor
        self.__magic_resistance = magic_resistance

    def get_defense(self):
        return self.__armor + self.__magic_resistance

front_wall = Wall(10, 20)

# This results in an error
print(front_wall.__armor)

# This works
print(front_wall.get_defense())
# 30
```

We do this to make it *easier to use our class*. Now when another developer (or even ourselves) use the `Wall` class, they don't need to think about how `armor` and `magic_resistance` affect the `defense` of a `Wall`. In fact, we don't even allow them to access `armor` and `magic_resistance` directly by making them private with `__`.

They simply call the public `get_defense()` method and know that the correct value will be returned.

## Assignment

Complete the `Wizard` class's constructor.

1. [ ] Set 2 **private** properties (be sure to include the private `__` prefix):
   1. [ ] `stamina`
   2. [ ] `intelligence`
2. [ ] Set 3 public properties:
   1. [ ] `name`: Use the value passed into the constructor
   2. [ ] `health`: 100x the value of "stamina"
   3. [ ] `mana`: 10x the value of "intelligence"
