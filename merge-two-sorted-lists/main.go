package main

import "fmt"

type ListNode struct {
	Val int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	merged := &ListNode{}
	current := merged
	for (list1 != nil && list2 != nil) {
		if (list1.Val > list2.Val) {
			current.Next = list2
			list2 = list2.Next
		} else if (list1.Val <= list2.Val) {
			current.Next = list1
			list1 = list1.Next
		}
		current = current.Next
	}

	if (list1 != nil) {
		current.Next = list1
	} else if (list2 != nil) {
		current.Next = list2
	}
	return merged.Next
}

func printList(node *ListNode) {
	for (node != nil) {
		if node.Next == nil {
			fmt.Printf("%d\n", node.Val)
		} else {
			fmt.Printf("%d -> ", node.Val)
		}
		node = node.Next
	}
}

func main() {
	list1 := &ListNode{Val: 1}	
	list1.Next = &ListNode{Val: 2}
	list1.Next.Next = &ListNode{Val: 4}

	list2 := &ListNode{Val: 1}
	list2.Next = &ListNode{Val: 3}
	list2.Next.Next = &ListNode{Val: 4}

	fmt.Printf("List1: \n")
	printList(list1)

	fmt.Printf("List2: \n")
	printList(list2)

	fmt.Printf("Merged: \n")
	merged := mergeTwoLists(list1, list2)
	printList(merged)
}
