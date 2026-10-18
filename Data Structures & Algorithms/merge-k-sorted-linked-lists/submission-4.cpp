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

        return divideAndConquer(lists, 0, lists.size() - 1);
    }

    ListNode* divideAndConquer(vector<ListNode*>& lists, int l, int r) {
        if (l == r) {
            return lists[l];
        }

        ListNode *left = divideAndConquer(lists, l, (l + r) / 2);
        ListNode *right = divideAndConquer(lists, (l + r) / 2 + 1, r);

        return merge2Lists(left, right);
    }

    // divAndConq(0, 3)

    // [head0, head1, head2, head3]
    // divAndConq(0, 1)
    // divAndConq(2, 3)

    // [head0, head1]
    // divAndConq(0, 0)
    // divAndConq(1, 1)

    // [head2, head3]
    // divAndConq(2, 2)
    // divAndConq(3, 3)

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

// 1 -> 2 -> 4
// 1 -> 3 -> 5
// 3 -> 6

// 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 6

// [head1, head2, head3, head4]
// 0-3

// [head1, head2] [head3, head4]
//   0-1               2-3

// [head1] [head2] [head3] [head4]

//     0      1        2      3


