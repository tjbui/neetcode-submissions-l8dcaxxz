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
        std::unordered_map<Node *, Node *> origToCopy{};

        Node *curr = head;
        while (curr) {
            Node *copy = new Node(curr->val);
            origToCopy[curr] = copy;
            curr = curr->next;
        }
        origToCopy[nullptr] = nullptr;

        curr = head;
        Node *prev = nullptr;
        while (curr) {
            origToCopy[curr]->random = origToCopy[curr->random];
            origToCopy[curr]->next = origToCopy[curr->next];
            curr = curr->next;
        }

        return origToCopy[head];
    }
};

// 3 -> 7 -> 4 -> 5 -> null
// <----------
// ------------------->
//       --------->
//      <----------

// 3 -> 7 -> 4 -> 5 -> null

// map original to copy
// {3 --> 3c, 7 --> 7c, 4 --> 4c, 5 -> 5c, null --> null}

// 3c ->
// check is null in the hash map? yes: point 3c random to null
// 

// 3c -> 7c
// check is 5 in the hash map? no: 





