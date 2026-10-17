/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution { // no extra space
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;

        Node *curr = head;
        while (curr) {
            Node *new_node = new Node(curr->val);

            new_node->next = curr->next;
            curr->next = new_node;
            
            curr = new_node->next;
        }

        curr = head;
        while (curr) {
            if (curr->random) {
                curr->next->random = curr->random->next;
            }
            else {
                curr->next->random = nullptr;
            }

            curr = curr->next->next;
        }

        curr = head->next;
        while (curr) {
            if (curr->next) {
                curr->next = curr->next->next;
            }

            curr = curr->next;
        }

        return head->next;
    }
};

// 3 -> 7 -> 4 -> 5 -> nptr
// <----------
// ------------------->
//       --------->
//      <----------

// 3 -> 7 -> 4 -> 5 -> nptr

// 3 -> 3' -> 7 -> 7' -> 4 -> 4' -> 5 -> 5' -> nptr

// 3 -> 3' -> 7 -> 7' -> 4 -> 4' -> 5 -> 5' -> nptr
// c    --------------------------------->

// 3 -> 3' -> 7 -> 7' -> 4 -> 4' -> 5 -> 5' -> nptr
//      h

// 3' -> 7' -> 4' -> 5' -> nptr
// h





