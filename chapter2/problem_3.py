## Problem 3 ############################################################################
## Delete Middle Node: Delete any Node in a linked list that is not n or n-1 ############
#########################################################################################

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


def solution1(target_node: Node) -> bool:
    if(target_node is None):
        return False
    next_node = target_node.next
    target_node.val = next_node.val
    target_node.next = next_node.next
    return True



def main():
    # 1->2->3->4->5->6->7->8->9->10
    # 1->2->3->4->5->7->8->9->10
    test_input = [2,3,4,5,6,7,8,9,10]
    test_input_node_1 = Node(1)
    test_runner = test_input_node_1
    test_target_node_1 = None
    for x in test_input:
        test_runner.next = Node(x)
        if(x == 6):
            test_target_node_1 = test_runner.next
        test_runner = test_runner.next
    print(f"Test Input Node:", end=" ")
    test_input_node_1.print_all_nodes()
    solution1(test_target_node_1)
    print(f"Test Output Node:", end=" ")
    test_input_node_1.print_all_nodes()
    runner = test_input_node_1
    while(runner.next):
        if(runner.val == 6):
            print(f"Test Failed!")
            return
        runner = runner.next
    print(f"Test Passed!")
main()