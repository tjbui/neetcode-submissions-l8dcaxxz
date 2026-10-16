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

class Solution { // approach 3: 2 pointers
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *dummy = new ListNode(0);
        ListNode *p1 = dummy;
        ListNode *p2 = dummy;

        dummy->next = head;

        while (n > 0) {
            p2 = p2->next;
            n--;
        }

        while (p2->next) {
            p1 = p1->next;
            p2 = p2->next;
        }

        ListNode *toDelete = p1->next;
        if (toDelete) {
            p1->next = toDelete->next;
            delete toDelete;
            return dummy->next;
        }

        p1->next = nullptr;
        return dummy->next;
    }
};

// d -> 1 -> 2 -> 3 -> 4, n = 2

// d -> 1 -> 2 -> 3 -> 4
// p1
// p2

// d -> 1 -> 2 -> 3 -> 4
// p1
//      p2

// d -> 1 -> 2 -> 3 -> 4
// p1
//           p2

// d -> 1 -> 2 -> 3 -> 4
//      p1
//                p2

// d -> 1 -> 2 -> 3 -> 4
//           p1
//                     p2