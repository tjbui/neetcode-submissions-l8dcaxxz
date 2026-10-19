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
        ListNode dummy = ListNode();
        dummy.next = head;

        ListNode* prevTail = &dummy;
        while (prevTail) {
            ListNode* newCurrTail = prevTail->next;
            ListNode* curr = prevTail;

            for (int i = 0; i < k; i++) {
                curr = curr->next;
                if (curr == nullptr) return dummy.next;
            }

            ListNode* newCurrHead = curr;
            ListNode* nextHead = curr->next;

            ListNode* prev = nextHead;
            curr = newCurrTail;
            for (int i = 0; i < k; i++) {
                ListNode* temp = curr->next;
                curr->next = prev;
                prev = curr;
                curr = temp;
            }

            newCurrTail->next = nextHead;
            prevTail->next = newCurrHead;
            prevTail = newCurrTail;
        }

        return dummy.next;
    }
};

//   dummy   ->   1   ->   2   ->   3   ->   4   ->   5   ->   6, k = 3

// check if there are k nodes left
//   dummy   ->   1         ->   2   ->   3   ->   4   ->   5   ->   6
//   prevTail     newCurrTail
//   curr

// check if there are k nodes left, YES
//   dummy   ->   1         ->   2   ->   3         ->   4   ->   5   ->   6
//   prevTail     newCurrTail             
//                                        curr
//                                        newCurrHead

// reverse k nodes
//                 ------------------------------------->
//   dummy   ->   1              2   ->   3         ->   4   ->   5   ->   6
//   prevTail     newCurrTail             newCurrHead    nextHead
//                curr                                   prev                          

// reverse k nodes
//   dummy   ->   1         <-   2   ->   3         ->   4   ->   5   ->   6
//   prevTail     newCurrTail             newCurrHead    nextHead
//                prev           curr                                     

// reverse k nodes
//                 ------------------------------------->
//   dummy   ->   1         <-   2   <-   3              4   ->   5   ->   6
//   prevTail     newCurrTail             newCurrHead    nextHead
//                prev           curr  

// set newCurrTail next to nextHead
// set prevTail next to newCurrHead
// set prevTail to newCurrTail
//   dummy   ->   3         ->   2   ->   1     ->     4   ->   5   ->   6
//                                        prevTail     



