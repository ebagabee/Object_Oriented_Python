# Archer Practice

Let's practice some of these class and objects concepts a bit more.

## Assignment

**Complete the `Archer` class**.

1. [ ] Complete the constructor. It should take the following parameters in order and set them as instance properties:
   1. [ ] `name`
   2. [ ] `health`
   3. [ ] `num_arrows`
2. [ ] Complete the `take_hit` method. It operates on the current archer instance.
   1. [ ] Remove one health from the current archer.
   2. [ ] If the archer has no health, raise the exception: `{NAME} is dead` where `{NAME}` is the archer's name.
3. [ ] Finish the `shoot` method. It takes an `Archer` instance as its `target` input.
   1. [ ] If the shooter has no arrows left, [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions) `{NAME} can't shoot` where `{NAME}` is the shooter's name.
   2. [ ] Otherwise, remove an arrow from the shooter.
   3. [ ] Print `{1} shoots {2}` where `{1}` is the shooter's name and `{2}` is the name of the targeted archer.
   4. [ ] Call the target's `take_hit()` method.
