# Python code for the above approach

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:

	# Program to reverse the linked list
	# using stack
	def reverseLLUsingStack(self, head):

		stack, temp = [], head

		while temp:
			stack.append(temp)
			temp = temp.next

		head = temp = stack.pop()

		# Untill stack is not
		# empty
		while len(stack) > 0:
			elem = stack.pop()
			temp.next = elem
			temp = elem

		elem.next = None
		return head

# Driver Code
if __name__ == "__main__":
	head = ListNode(20, ListNode(52, ListNode(23,
						ListNode(14, ListNode(5)))))
	obj = Solution()
	head = obj.reverseLLUsingStack(head)
	while head:
		print(head.val, end=' ')
		head = head.next
