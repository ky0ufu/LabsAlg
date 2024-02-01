class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class PersistentStack:
    def __init__(self):
        self.versions = {}
        self.current_version = 0
        
    def push(self, value, version):
        if version not in self.versions:
            self.versions[version] = None
        
        new_node = StackNode(value)
        new_node.next = self.versions[version] 
        self.versions[version] = new_node 
    
    def pop(self, version):
        if version not in self.versions or self.versions[version] is None:
            return None

        popped_value = self.versions[version].value
        self.versions[version] = self.versions[version].next
        return popped_value
    
    def print_stack(self, version):
        if version not in self.versions or self.versions[version] is None:
            print("Stack is empty.")
            return
        current_node = self.versions[version]
        values = []
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
        
        print("Stack version", version, ":", "->".join(values))


stack = PersistentStack()
stack.push(1, 1)
stack.push(2, 1)
stack.push(3, 2)
stack.push(4, 2)
stack.print_stack(2)

popped_value = stack.pop(2)
print("Poped value", popped_value)