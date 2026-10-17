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

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node *curr = head;
        std::unordered_map<Node *, Node *> origToNew{};

        while (curr) {
            Node *curr_copy = nullptr;
            if (origToNew.contains(curr)) {
                curr_copy = origToNew[curr];
            }
            else {
                curr_copy = new Node(curr->val);
                origToNew[curr] = curr_copy;
            }

            // if curr's next is in the hash map already, set it's next to it's mapped value
            // else, create the next and put in hash map
            if (curr->next) {
                if (origToNew.contains(curr->next)) {
                    curr_copy->next = origToNew[curr->next];
                }
                else {
                    Node *next_copy = new Node(curr->next->val);
                    origToNew[curr->next] = next_copy;
                    curr_copy->next = next_copy;
                }
            }

            // if curr's random is in the hash map already, set it's next to it's mapped value
            // else, create the random and put in hash map
            if (curr->random) {
                if (origToNew.contains(curr->random)) {
                    curr_copy->random = origToNew[curr->random];
                }
                else {
                    Node *random_copy = new Node(curr->random->val);
                    origToNew[curr->random] = random_copy;
                    curr_copy->random = random_copy;
                }
            }

            curr = curr->next;
        }

        return origToNew[head];
    }
};

// 3 -> 7 -> 4 -> 5 -> nptr
// <----------
// ------------------->
//       --------->
//      <----------

// 3 -> 7 -> 4 -> 5 -> nptr
// c

// {3 --> 3c, 7 --> 7c, nptr --> nptr }







