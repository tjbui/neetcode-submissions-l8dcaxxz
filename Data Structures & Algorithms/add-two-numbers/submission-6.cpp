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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;

        ListNode *dummy = new ListNode(0);
        ListNode *curr = dummy;
        while (l1 && l2) {
            int total = l1->val + l2->val + carry;

            ListNode *new_node = new ListNode{};
            if (total > 9) {
                carry = 1;
                new_node->val = total - 10;
            }
            else {
                carry = 0;
                new_node->val = total;
            }

            curr->next = new_node;
            curr = new_node;
            l1 = l1->next;
            l2 = l2->next;
        }

        while (l1) {
            int total = carry + l1->val;

            ListNode *new_node = new ListNode{};
            if (total > 9) {
                carry = 1;
                new_node->val = total - 10;
            }
            else {
                carry = 0;
                new_node->val = total;
            }

            curr->next = new_node;
            curr = new_node;
            l1 = l1->next;
        }

        while (l2) {
            int total = carry + l2->val;

            ListNode *new_node = new ListNode{};
            if (total > 9) {
                carry = 1;
                new_node->val = total - 10;
            }
            else {
                carry = 0;
                new_node->val = total;
            }

            curr->next = new_node;
            curr = new_node;
            l2 = l2->next;
        }

        if (carry) {
            ListNode *new_node = new ListNode(1);
            curr->next = new_node;
        }

        return dummy->next;
    }
};

// 8 -> 5 -> 9
// 8 -> 7 -> 6

//   11
//   958 
// + 678
//  1636


// carry = 1
// 8 -> 5 -> 9
// c

// 8 -> 7 -> 6
// c

// 6 -> 



