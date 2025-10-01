# Dragons Fight

We've created a lot of classes in this course, now let's write some code that *uses* them. **Let's have ourselves a little dragon fight**.

## Assignment

Complete the bottom half of the `main()` function using two for-loops:

1. [ ] Iterate over all the `dragons` and `describe()` each one in order.
2. [ ] Iterate over all the `dragons` *again* and have each dragon `breathe_fire` at coordinate `x=3, y=3`. Pass in all the **other** dragons (not the one currently breathing fire) as the `units` parameter, so we can see if they get hit.

Pass in the dragons in the same order as the original list, excluding the current dragon. For example, when `Blue Dragon` breathes fire, it should check to breathe fire on the other dragons in this order:

1. Green Dragon
2. Red Dragon
3. Black Dragon

### Example Output

When you describe the dragons, your output should look like this:

```plaintext
Green Dragon is at 0/0
Red Dragon is at 2/2
Blue Dragon is at 4/3
Black Dragon is at 5/-1
```

The output of the first dragon breathing fire should look like this:

```plaintext
====================================
Green Dragon breathes fire at 3/3 with range 1
------------------------------------
Red Dragon is hit by the fire
Blue Dragon is hit by the fire
====================================
Red Dragon breathes fire at 3/3 with range 2
------------------------------------
```

## Tips

### Copying a List

To get a *new copy* of a list, use the `copy()` method. If you just do `new_list = old_list`, your new variable will just be a [reference](<https://en.wikipedia.org/wiki/Reference_(computer_science)>) to the original list... which is not what we want.

```python
nums = [4, 3, 2, 1]
nums_copy = nums.copy()
# nums_copy is [4, 3, 2, 1]
```

### Delete from a List

```python
fruits = ["apple", "banana", "cherry", "kiwi"]
del fruits[1]
# fruits is ["apple", "cherry", "kiwi"]
```
