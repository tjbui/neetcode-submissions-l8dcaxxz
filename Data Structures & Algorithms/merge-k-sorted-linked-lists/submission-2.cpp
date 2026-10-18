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

class Solution { // divide and conquer
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) {
            return nullptr;
        }

        if (lists.size() == 1) {
            return lists[0];
        }

        std::vector<ListNode*> leftLists = std::vector<ListNode*>(lists.begin(), lists.begin() + (lists.size() / 2));
        std::vector<ListNode*> rightLists = std::vector<ListNode*>(lists.begin() + (lists.size() / 2), lists.end());
        ListNode* leftHead = mergeKLists(leftLists);
        ListNode* rightHead = mergeKLists(rightLists);

        return merge2Lists(leftHead, rightHead);
    }

    ListNode *merge2Lists(ListNode* head1, ListNode* head2) {
        ListNode* dummyNode = new ListNode();

        ListNode *curr = dummyNode;
        while (head1 && head2) {
            if (head1->val < head2->val) {
                curr->next = head1;
                head1 = head1->next;
            }
            else {
                curr->next = head2;
                head2 = head2->next;
            }

            curr = curr->next;
        }

        while (head1) {
            curr->next = head1;
            curr = curr->next;
            head1 = head1->next;
        }

        while (head2) {
            curr->next = head2;
            curr = curr->next;
            head2 = head2->next;
        }

        return dummyNode->next;
    }
};

// 1 -> 2 -> 4
// 1 -> 3 -> 5
// 3 -> 6

// 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 6

// [head1, head2, head3, head4]

// [head1, head2] [head3, head4]

// [head1] [head2] [head3] [head4]

// 


