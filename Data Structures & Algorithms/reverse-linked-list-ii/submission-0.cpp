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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode dummy = ListNode();
        dummy.next = head;
        int nodesSeen = 1;
        // nodesSeen = 1
        // d -> 1 -> 2 -> 3 -> 4 -> 5
        // p    c

        // nodesSeen = 2
        // d -> 1 -> 2 -> 3 -> 4 -> 5
        //      p    c
        ListNode* curr = head;
        ListNode* prev = &dummy;
        while (curr && nodesSeen < left) {
            prev = curr;
            curr = curr->next;
            nodesSeen++;
        }

        // tailBeforeReversedNodes = 1
        // reversedTail = 2
        ListNode* tailBeforeReversedNodes = prev;
        ListNode* reversedTail = curr;
        prev = curr;
        curr = curr->next;
        nodesSeen++;

        // nodesSeen = 3
        // d -> 1 -> 2 <- 3 -> 4 -> 5
        //           p    c
        // tailBeforeReversedNodes = 1
        // reversedTail = 2

        // nodesSeen = 4
        // d -> 1 -> 2 <- 3 <- 4 -> 5
        //                p    c
        // tailBeforeReversedNodes = 1
        // reversedTail = 2
        
        while (curr && nodesSeen <= right) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
            nodesSeen++;
        }

        // nodesSeen = 5
        // d -> 1 -> 2 <- 3 <- 4 -> 5
        //                     p    c
        // tailBeforeReversedNodes = 1
        // reversedTail = 2

        tailBeforeReversedNodes->next = prev;
        reversedTail->next = curr;

        return dummy.next;
    }
};

// 1 -> 2 -> 3 -> 4 -> 5, left = 2, right = 4









// 1-> 4 -> ... -> 2 -> 5