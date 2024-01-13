from linked_list_operations.build_linked_list import build_linked_list as build
from linked_list_operations.traverse_linked_list import traverse_linked_list as traverse

values = [1, 2, 3]
head = build(values)

result = traverse(head)
print(result)  # [1, 2, 3]
