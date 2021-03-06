#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#

# @lc code=start
class Node(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None

class LRUCache(object):
    # THIS IS HARD TAT, copy from Garvit
    # still CANT pass case 14

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.mapping = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.mapping:
            node = self.mapping[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        if key in self.mapping:
            self.remove(self.mapping[key])
            
        node = Node(key, value)
        if len(self.mapping) >= self.capacity:
            next_head = self.head.next
            self.remove(next_head)
            del self.mapping[next_head.key]
            
        self.add(node)
        self.mapping[key] = node
        
    def add(self, node):
        tail = self.tail.prev
        tail.next = node
        self.tail.prev = node
        node.prev = tail
        node.next = self.tail
        
    def remove(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

