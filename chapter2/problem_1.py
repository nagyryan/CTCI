## Problem 1 ############################################################################
## Remove Dups: Write code to remove duplicates from an unsorted linked listl ###########
## FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed? ####
#########################################################################################

class Node:
    def __init__(self, data: int):
        self.val = data
        self.next = None

    def print_all_nodes(self):
        while(self):
            print(f"{self.val}", end = "->")
            self = self.next
        print("")

# With temporary buffer
# Assumptions: First value is always going to be unique
# Time: O(n) -> since we are iterating over entire linked list
# Space: O(n) -> memory increases linearly with input linked list
def solution1(head: Node) -> Node:
    if head is None:
        return head
    seen_data = {}
    prev = None
    current = head
    while current:
        if current.val not in seen_data:
            seen_data[current.val] = 1
            prev = current
            current = current.next
        else:
            prev.next = current.next
            current = prev.next
    print(seen_data)
    return head

# In place modification
# Time: O(n^2) -> iterating over linked list for every element
# Space: O(1) -> no additional memory needed since deletion is done in place
def solution2(head: Node) -> Node:
    if (head is None):
        return head
    current = head
    while current.next is not None:
        runner = current
        while runner.next is not None:
            if (runner.next.val == current.val):
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head

# Tests
def main():
    # 2 -> 2 -> 5 -> 5
    # 2 -> 5
    test_input_node_1 = Node(2)
    test_input_node_1.next = Node(2)
    test_input_node_1.next.next = Node(5)
    test_input_node_1.next.next.next = Node(5)
    test_input_node_1.print_all_nodes()
    test_output_node_1 = solution1(test_input_node_1)
    test_output_node_1.print_all_nodes()

    test_output_node_2 = solution2(test_input_node_1)
    test_output_node_2.print_all_nodes()
    if(test_output_node_1.val == 2 and test_output_node_1.next.val == 5 and test_output_node_1.next.next == None):
        print(f"Test 1 Passed!")
    else:
        print(f"Test 1 Failed!")
    if(test_output_node_2.val == 2 and test_output_node_2.next.val == 5 and test_output_node_2.next.next == None):
        print(f"Test 1 Passed!")
    else:
        print(f"Test 1 Failed!")
        
main()