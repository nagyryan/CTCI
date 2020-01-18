## Problem 2 ####################################################################################################
## Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list ###########
## FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed? ############################
#################################################################################################################
class Node:
    def __init__(self, data: int):
        self.val = data
        self.next = None

    def print_all_nodes(self):
        while(self):
            if (self.next is None):
                print(f"{self.val}", end = "")
            else:
                print(f"{self.val}", end = "->")
            self = self.next
        print("")


# Have runner move k positions aheead
def solution1(head: Node, k: int) -> int:
    if head is None:
        return head
    current = head
    runner = current
    for _ in range(k):
        runner = runner.next
    while (runner.next):
        runner = runner.next
        current = current.next
    return current.val





# Tests
def main():
    # 2 -> 2 -> 5 -> 5 -> 6 -> 7 -> 9
    # 6
    test_input = [2,5,5,6,7,9]
    test_input_node_1 = Node(2)
    runner = test_input_node_1
    for x in test_input:
        runner.next = Node(x)
        runner = runner.next
    test_input_node_1.print_all_nodes()
    second_to_last_element = solution1(test_input_node_1, 2)
    third_to_last_element = solution1(test_input_node_1, 3)

    if(second_to_last_element == 6 and third_to_last_element == 5):
        print(f"Test 1 Passed!")
    else:
        print(f"Test 1 Failed!")
        
main()
