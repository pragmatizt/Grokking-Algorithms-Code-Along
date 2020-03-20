"""
***BINARY_SEARCH FUNCTION***
The binary_search function takes a sorted array and an item.  If the 
item is in the array, the function returns its position.  You'll keep
track of what part of the array you have to search through.  At the 
beginning, this is the entire array:
"""

low = 0
high = len(list) - 1

# Each time, you check the middle element:
mid = (low + high) / 2
guess = list[mid]

## Note: mid is rounded down by Python automatically if (low + high) isn't an even #

# If the guess is too low, you update low accordingly:
if guess < item:
    low = mid + 1

# And if the guess is too high, you update high.  Here's the full code:

def binary_search(list, item):
    low = 0
    high = len(list) - 1  # low and high keep track of which part of the list you'll search in

    while low <= high:  # While you haven't narrowed it to one element
        mid = (low + high) # check middle element
        guess = list[mid]
        if guess == item:  # Found the item
            return mid
        if guess > item:  # The guess was too high
            high = mid - 1
        else:               # The guess was too low
            low = mid + 1
    return None             # The item doesn't exist.

    my_list = [1, 3, 5, 7, 9]   # Let's test it.

    print(binary_search(my_list, 3)) # => 1
    print(binary_search(my_list, -1)) # => None

"""
EXERCISES:
1. Suppose you have a osrted list of 128 names, and you're searching 
through it using binary search, what's the maximum number of steps it would take?
ANSWER: 128/2=64. 64/2=32. 32/2=16. 16/2=8. 8/2=4. 4/2=2. 2/2=1.  
Seven.
2. Suppose you double the size of the list.  What's the maximum number of steps now?
ANSWER: 256/2=128. ... so it's 7 + 1.
Eight.
"""

# ADDITIONAL NOTES ON RUNNING TIME:

"""
simple search                       ||     binary search
100 items = 100 guesses             ||     100 items = 7 guesses
==========================================================
4,000,000,000 items = 4bn guesses   ||  4,000,000,000 items = 32 guesses
==========================================================
        O(n)                        ||  O(log n)
     linear time                    || logarithmic time
"""

# BIG O NOTATION
"""
Big O notation is special notation that tells you how fast an algorithm is.
Who cares?  Turns out you'll use other people's algo's often. When you do,
it's nice to understand how fast or slow they are.  
"""

# EXAMPLE of BIG O Notation
"""
NASA - Bob has ten seconds to land a rocket on Moon.
He has a list with 1 billion elements (1,000,000,000).
A simple search of 100 elements is 100ms for Bob.
A binary search of 100 elements is 7 ms for Bob.

How long will binary search take for 1bn elements?

        SIMPLE SEARCH                   ||      BINARY SEARCH
100 elements            100 ms          ||      7 ms
10,000 elements         10 seconds      ||      14 ms
1,000,000,000 elems     11 days         ||      32 ms

Run times grow at very different speeds!

Bob thought binary search was 15 times faster than simple search. 
But it's more like 33 million times faster.
"""

# BIG O notation tells you how fast an algorithm is.
"""
Suppose you have a list size of n.  Simple search needs to check each element,
so it will take n operations. The run time in Big O notation is O(n).
Where are the seconds? There are none. Big O doesn't tell you speed in seconds.
Big O lets you compare the number of operations. It tells you hwo fast an algo grows.
"""




