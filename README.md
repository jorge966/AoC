# AoC 2024 Day 1 Thoughts

## 1. More verbose variable names. Lets make sure we don't confuse what is going where, by having explicit variable names we should be able to keep up with the context of the problem we are working on.

For example, instead of writing `test` we can write `current_item_list2` which give us more context into what the variable we're naming is attempting to hold. This is especially helpful when we need to debug, because if we print out the value of `current_item_list2` we'll know if something is amiss, versus printing out the value of `test`, who knows what is supposed to be inside that variable.

## 2. Lets think about how we want to loop through things first.

If we want to loop through something, we should (generally) try to avoid nested loops. Is there some way we can do all the things we want to do in one loop? Can we track the indexes somehow so we don't have to loop through a list twice? 

It is important to think about **what** the loop is attempting to achieve at each step/iteration so we don't complicate our program.

For example, when we were looping through the left list and the right list, the initial approach was to use a nested for loop. That didn't do what we wanted it to, so we needed to track the actual index of where we were at in the first list, in order to compare that to the index of the second list.

In the future, could there be an even better way to approach this problem with stepping through two lists at the same time? Using `range(start, end)` might end up being more useful than keeping track of the index for a separate list?

# AoC 2024 Day 1 Part 2 Thoughts

## 1. The initial implementation we used was to use a nested for loop to go through the first list, and then iterate through the second list and keep track of how many times each element occurs in the second list.

The nested loop implementation worked, and for the 1000 strong list, we would be doing a 1000 squared iterations to loop through it. We decided that we can do a dictionary that instead keeps track of how many times each number in the second list appears. 

In doing so, we loop through the second list once (1000 times) and then we loop through the first list (1000 times) making our total number of iterations only 2 x 1000.

There is also a builtin collections class that actually does this for us: [link to Python Counter here.](https://docs.python.org/3/library/collections.html#collections.Counter)
