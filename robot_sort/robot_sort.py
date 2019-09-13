class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Notes
        # Robot must check if it can_move_right and then move_right
        # Robot must check if it can_move_left and then move_left
        # Robot can compare current item with the one in front and return values depending using compare_item
            # return 1 if held item is greater
            # return -1 if held item is less
            # return 0 if equal
            # If either is None, return None
        # Robot can swap_item - swap its current with the item in front of it
        # If it tries to pick up an item while already holding one, it will swap the items instead.
        # Robot's lights can turn on and off

        # Implentation Plan
        # I will try to implement a bubble sort since this looks very similar
        # The game plan is to move move the biggest number to the far right with each walkthrough
        # As we walk through the list rightward and in reverse, bigger items should automatically move to the right as well
         # How to end the sorting:
                # To stop the robot from performing more sorts, we would wrap the robot's processes within the "while-loop" of the lights
                # If a swap happened within a round, continue sorting
                # If there are no swaps, it means everything is already sorted and we end
                # Since we can't do loops, we can use the lights as the indicator to keep sorting.
        # The robot would do the following as part of its process:
            # For Moving rightward <if able>
                # Pick up the first number
                # Compare the picked-up number with the one to the right using self.compare_item**
                    # Check the response
                        # if 1 or "greater", perform self.swap_item
                            # Put the number the robot is holding down which should be the smaller of the two
                            # Check if self.can_move_right, if true then self.move_right
                            # Pick up the next number in the sequence
                            # Return to self.compare_item**
                        # if -1 or "lesser", no swaps
                            # movement same as 1 but no swaps
                        # if 0, perform same as -1, no swaps
                            # movement same as 1 but no swaps
                        # if None
                            # We've reach the end, check if we can_move_right, if false then
                            # Check if can_move_left and start moving leftward
            # Moving leftward <if able>
                # The robot's journey backwards is similar.
                # Pick up the current number, compare_item, check the response, and move accordingly until can_move_left is false.
                # At this point, it's the first number in sequence and we start the process again.
           

        # Pick up first number
        self.swap_item
        # Lights on
        self.set_light_on()

        # While lights on, keep sorting
        while self.light_is_on() == True:
            # Reset the lights so we can redo the while when we make a swap
            self.set_light_off() 

            # Start of List with initial number and can move right
            while self.can_move_right == True:
                if self.compare_item() == 1: # Current is bigger so swap and then move right
                    self.swap_item()
                    self.move_right()
                    self.set_light_on() # Keep the loop going from the beginning
                elif self.compare_item() == -1 or self.compare_item() == 0: # Current is smaller or equal
                    self.move_right()

            # End of the List and can move left; since robot looks at the one in front
            # This should be the same as the previous but movement is opposite
            while self.can_move_left == True:
                 if self.compare_item() == 1:
                    self.swap_item()
                    self.move_left()
                    self.set_light_on()
                elif self.compare_item() == -1 or self.compare_item() == 0 :
                    self.move_left()
                
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)