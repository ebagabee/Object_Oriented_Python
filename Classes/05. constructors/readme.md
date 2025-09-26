It's rare in the real world to see a class that defines properties like this (as we did):

```python
class Soldier:
    name = "Legolas"
    armor = 2
    num_weapons = 2
```

A [constructor](<https://en.wikipedia.org/wiki/Constructor_(object-oriented_programming)>) is (usually) better. It's a specific method on a class called [`__init__`](https://docs.python.org/3/reference/datamodel.html#object.__init__) that is called automatically when you create a new instance of a class.

So, using a constructor, the code from above would look like this:

```python
class Soldier:
    def __init__(self):
        self.name = "Legolas"
        self.armor = 2
        self.num_weapons = 2
```

Not only is this *safer* (we'll talk about why later), but it also allows us to make the starting property values configurable:

```python
class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

soldier_one = Soldier("Legolas", 2, 10)
print(soldier_one.name)
# prints "Legolas"
print(soldier_one.armor)
# prints "2"
print(soldier_one.num_weapons)
# prints "10"

soldier_two = Soldier("Gimli", 5, 1)
print(soldier_two.name)
# prints "Gimli"
print(soldier_two.armor)
# prints "5"
print(soldier_two.num_weapons)
# prints "1"
```

## Assignment

**Add a constructor to the `Wall` class**.

1. [ ] It should take `depth`, `height` and `width` as parameters, in that order, and set them as instance properties.
2. [ ] Compute an additional property called `volume`. Volume is the depth times height times width
