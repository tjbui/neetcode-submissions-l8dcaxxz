/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) {
            return head;
        }

        ListNode dummy = ListNode();
        dummy.next = head;
        ListNode *prevTail = &dummy;

        while (prevTail) {
            // check if at least k nodes are left
            ListNode* currTail = prevTail;
            for (int i = 0; i < k; i++) {
                if (currTail->next) {
                    currTail = currTail->next;
                }
                else {
                    return dummy.next;
                }
            }
            ListNode* nextHead = currTail->next;
            ListNode* currHead = prevTail->next;

            // attach prevTail to currTail and set currTail to the start of reversal
            ListNode* temp = prevTail->next;
            prevTail->next = currTail;
            currTail = temp;

            // reverse until before the nextHead
            ListNode* prev = nextHead;
            while (currTail != nextHead) {
                ListNode* temp = currTail->next;
                currTail->next = prev;
                prev = currTail;
                currTail = temp;
            }

            currTail = currHead;
            prevTail = currHead;
        }

        return dummy.next;
    }
};

// d -> 1 -> 2 -> 3 -> 4 -> 5 -> 6, k = 3

//    d      ->     1    ->     2     ->     3    ->     4     ->     5     ->     6
// prevtail         
// currTail

//    d      ->     1    ->     2     ->     3    ->     4     ->     5     ->     6
// prevtail                                 
//                                        currTail

// yes 3 nodes are left

//    d      ->     1    ->     2     ->     3    ->     4     ->     5     ->     6
// prevtail                               currTail
//                                                    nextHead

//     ------------------------------------->
//    d             1    ->     2     ->     3    ->     4     ->     5     ->     6
// prevtail      currTail                       
//                                                    nextHead

//     
//    d      ->     3    ->     2     ->     1    ->     4     ->     5     ->     6
// prevtail                                currTail
//                                                    nextHead
