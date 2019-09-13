#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is O(n) because it is n^3/n^2 for the loop/body.


b) This is O(n^2) because it has a while loop O(n) inside the for loop (n). Lines in between are O(1) and since they are slow moving compared to n^2, they are omitted.


c) This is O(n) because the recursion loops as many times as the number bunnies you input.

## Exercise II
# Building

where n = 22
|22|21|20|19|18|17|16|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|
---egg break zone---^ Possible F location

The plan would be to throw the eggs at the halfway point of the building at floor 11 and see if the eggs would break. If the egg doesn't break, you can ignore every floor below that.

|22|21|20|19|18|17|16|15|14|13|12| Remaining Floors

We can do this again with the remaining floors. The midway would be (22-12)/2 which is five so we move up to floor 17 and drop the egg. If it breaks (let's say it does since I designated 16 as the break point), then we can ignore 17 and everything above because we know everything after would break the egg as well since this info is given to us.

|16|15|14|13|12| Remaining Floors

We keep doing this method until there's only one culprit remaining which we know is f. The next ones to go would be 14-, and finally 15 would go, and 16 remains!

This method would be related to a binary search so the runtime complexity would be 0(log(n)) since we are removing half the floors each time.





