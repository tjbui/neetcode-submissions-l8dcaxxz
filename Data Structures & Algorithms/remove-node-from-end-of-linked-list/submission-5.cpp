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
public: // approach 2: recursive
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        removeRec(head, &n);

        if (n == 0) {
            ListNode *temp = head;
            head = head->next;
            delete temp;
        }

        return head;
    }

    ListNode *removeRec(ListNode *head, int *iptr) {
        if (!head) {
            return nullptr;
        }

        removeRec(head->next, iptr);

        (*iptr)--;

        if (*iptr == -1) {
            head->next = head->next->next;
        }


        return head;
    }
};

// p1 -> p2 -> p3 -> p4, n = 2


// removeNthFromEnd(p1, ptr)
// removeNthFromEnd(p2, ptr)
// removeNthFromEnd(p3, ptr)
// removeNthFromEnd(p4, ptr)
// removeNthFromEnd(nullptr, ptr)

// removeNthFromEnd(p4, 2) --> n = 1
// removeNthFromEnd(p3, 2) --> n = 0

 
// p1 -> p2 -> p3
// 

