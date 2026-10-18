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

class Solution { // divide and conquer iterative
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) {
            return nullptr;
        }

        while (lists.size() > 1) {
            std::vector<ListNode*> mergedLists{};

            for (int i = 0; i < lists.size(); i += 2) {
                ListNode* firstHead = lists[i];

                ListNode* secondHead = nullptr;
                if (i + 1 < lists.size()) {
                    secondHead = lists[i + 1];
                }

                mergedLists.push_back(merge2Lists(firstHead, secondHead));
            }

            lists = mergedLists;
        }

        return lists[0];
    }

    ListNode* merge2Lists(ListNode* head1, ListNode* head2) {
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

// [head0, head1, head2, head3, head4, head5, head6, head7]

// merge 0, 1. merge 2, 3. merge 4, 5. merge 6, 7
// [head0, head1] [head2, head3] [head4, head5] [head6, head7]
// [head0, head1, head2, head3]


