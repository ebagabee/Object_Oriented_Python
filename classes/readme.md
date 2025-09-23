# Classes

A [class](https://docs.python.org/3/tutorial/classes.html) is a special type in an object-oriented programming language like Python. If you squint really hard, it's kinda like a dictionary in that it usually stores named value pairs:

```py
# Defines a new class called "Soldier"
# with three properties: health, armor, damage
class Soldier:
    health = 5
    armor = 3
    damage = 2
```

Just like a string, integer or float, a class is a *type*, but instead of being a built-in type, classes are custom types that you define.

## Objects

So if a class is a new custom type, what's an object? Objects are just [instance](https://stackoverflow.com/questions/20461907/what-is-meaning-of-instance-in-programming)s of a class.

Yeah I know, "instance" is another fancy programming word. It just means "an example of" or "a specific case of". For example, "Lane is an instance of a human" or "My Chemical Romance is an instance of a band".

For example:

```python
health = 50
# health is an instance of an integer type
aragorn = Soldier()
# aragorn is an instance of the Soldier class type
```

Each new instance of a class is an "object".

## Example

```py
class Archer:
    health = 40
    arrows = 10

# Create several instances of the Archer class
legolas = Archer()
bard = Archer()

# Print class properties
print(legolas.health) # 40
print(bard.arrows) # 10
```

## Assignment

1. [ ] Create a class called `Wall`. It should have:
   1. [ ] A property called `armor` initialized to (initially set to) `10`
   2. [ ] A property called `height` initialized to `5`
2. [ ] Create a class called `BatteringRam`. It should have:
   1. [ ] A property called `damage` initialized to `2`
   2. [ ] A property called `length` initialized to `4`
