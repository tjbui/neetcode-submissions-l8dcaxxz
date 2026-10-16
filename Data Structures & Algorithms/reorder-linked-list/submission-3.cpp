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
    void reorderList(ListNode* head) {
        if (!head) {
            return;
        }

        ListNode *slow = head;
        ListNode *fast = head->next;
        
        // Get middle
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reverse second half
        ListNode *curr = slow->next;
        slow->next = NULL;
        ListNode *prev = NULL;
        while (curr) {
            ListNode *temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        // Merge
        ListNode *p1 = head;
        ListNode *p2 = prev;
        while (p1 && p2) {
            ListNode *temp1 = p1->next;
            ListNode *temp2 = p2->next;

            p1->next = p2;
            p2->next = temp1;
            p1 = temp1;
            p2 = temp2;
        }
        
        return;
    }
};

// [0, 1, 2, 3, 4, 5, 6]

// [0, 6, 1, 5, 2, 4, 3]

// [0, 1, 2, 3, 4, 5, 6]

// [0, 1, 2, 3, 4, 5, 6]
//  s  f


// [0, 1, 2, 3, 4, 5, 6]
//     s     f

// [0, 1, 2, 3, 4, 5, 6]
//        s        f

// [0, 1, 2, 3, 4, 5, 6]
//           s           f

// 0 -> 1 -> 2 -> 3
//      p1

// 6 -> 5 -> 4
//      p2

// 0 --> 6 --> 1
// 

// p1->next = p2
// p2->next = p1->next
// p1 = temp1
// p2 = temp2

