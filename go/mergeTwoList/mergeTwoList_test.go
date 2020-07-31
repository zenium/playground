package main

import (
	"testing"
	"fmt"
	"reflect"
)

type ListNode struct {
	Val int
	Next *ListNode
}
 
 func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    ret := &ListNode{}
    head := ret
    for l1 != nil && l2 != nil {
		if l1.Val < l2.Val{
			// fmt.Printf(">>>%v, %v\n", l1.Val, l2.Val)
			ret.Val = l1.Val
			l1 = l1.Next
		} else {
			ret.Val = l2.Val
			l2 = l2.Next
		}
		fmt.Printf(">>%v; %v; %v\n", ret, l1, l2)
		ret.Next = &ListNode{}
		ret = ret.Next
    }
    if l1 != nil {
		ret.Val = l1.Val
		ret.Next = l1.Next
    } else if l2 != nil {
		ret.Val = l2.Val
		ret.Next = l2.Next
	}
	fmt.Printf(">1>%v\n", ret)
	fmt.Printf(">2>%v\n", ret.Next)
	fmt.Printf(">3>%v\n", head)
    return head
}

func TestMerge(t *testing.T) {
	tests := []struct {
		x, y, exp *ListNode
	}{
		{x: &ListNode{
			Val: 1,
			Next: &ListNode{
				Val: 3,
				Next: &ListNode{
					Val: 5,
				},
			},
		},
		y: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 4,
				Next: &ListNode{
					Val: 5,
				},
			},
		},
		exp: &ListNode{
			Val: 1,
			Next: &ListNode{
				Val: 2,
				Next: &ListNode{
					Val: 3,
					Next: &ListNode{
						Val: 4,
						Next: &ListNode{
							Val: 5,
						},
					},
				},
			},
		},
	},
	}

	for _, test := range tests {
		got := mergeTwoLists(test.x, test.y)
		if reflect.DeepEqual(got, test.exp) {
			
		} else {
			t.Errorf("Test failed, got: %+v, want: %+v.", got, test.exp)
		}
	}
}