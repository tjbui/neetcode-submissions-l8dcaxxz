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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *curr = head;
        ListNode *reversedHead = nullptr;
        while (curr) {
            ListNode *temp = curr->next;
            curr->next = reversedHead;
            reversedHead = curr;
            curr = temp;
        }

        curr = reversedHead;
        ListNode *prev = nullptr;
        while (n > 1) {
            prev = curr;
            curr = curr->next;
            n--;
        }

        if (prev == nullptr) {
            reversedHead = curr->next;
        }
        else {
            prev->next = curr->next;
        }
        delete curr;

        ListNode *result = nullptr;
        curr = reversedHead;
        while (curr) {
            ListNode *temp = curr->next;
            curr->next = result;
            result = curr;
            curr = temp;
        }

        return result;
    }
};

// 1 -> 2 -> 3 -> 4, n = 2

// 1 -> 2 -> 4

// approach one: reverse the list and then go backwards n nodes

// approach two: recursion

// approach three: 