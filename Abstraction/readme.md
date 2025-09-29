# Abstraction

Abstraction helps us handle complexity by hiding unnecessary details.

... which sounds just like encapsulation, *right*? To be honest, the ideas are so similar that it's almost not worth worrying about the difference..._almost_.

## Abstraction vs. Encapsulation

- Abstraction is about *creating a simple interface for complex behavior.* It focuses on what's exposed (public).
- Encapsulation is about *hiding internal state.* It focuses on tucking away the implementation details (private).

Abstraction is more about reducing complexity, encapsulation is more about maintaining the integrity of system internals.

In my personal opinion, it's a bit of a distinction without a difference... but "abstraction" is a more broadly used term, and in my view at least, it's also a more general term for "making something easier to use by adding a layer on top".

## Are We Encapsulating or Abstracting?

Both. We are almost always doing both. Here's an example of using the `random` library to generate a random number:

```py
import random

attack_damage = random.randrange(5)
```

[Generating random numbers](https://blog.boot.dev/cryptography/what-is-entropy-in-cryptography/) is a *really hard* problem. The operating system uses the physical hardware of the computer to create a [seed](https://en.wikipedia.org/wiki/Random_seed) for the randomness. However, the developers of the `random` library have *abstracted* that complexity away and *encapsulated* it within the simple `randrange` function. We just say "I want a random number from 0 to 4" and the library does it.

When writing libraries for other developers to use, getting the abstractions right is *critical* because changing them later can be disastrous. Imagine if the maintainers of the `random` module changed the input parameters to the `randrange` function! It would break code used by thousands of applications around the world.

## Assignment

We don't want our coworkers at Age of Dragons Studios™ to have to worry about how `Human`s move. We'll abstract that away from them by encapsulating the private `__pos_x`, `__pos_y`, and `__speed` variables behind some simple methods.

**Complete the following methods in the `Human` class:**

1. [ ] `move_right()`: Adds the human's speed to its x position.
2. [ ] `move_left()`: Subtracts the human's speed from its x position.
3. [ ] `move_up()`: Adds the human's speed to its y position.
4. [ ] `move_down()`: Subtracts the human's speed from its y position.
5. [ ] `get_position()`: Returns the x position and y position as a [tuple](https://docs.python.org/3/library/stdtypes.html#tuples).
