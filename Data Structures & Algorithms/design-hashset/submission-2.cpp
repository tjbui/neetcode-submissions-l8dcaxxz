class MyHashSet {
public:
    struct ListNode {
        ListNode* next{};
        int val{};

        ListNode() = default;
        ListNode(int val) : val(val) {}
    };
    static constexpr int numBuckets = 1000;
    std::array<ListNode*, numBuckets> buckets{};

    MyHashSet() {
        for (int i = 0; i < numBuckets; i++) {
            ListNode* newNode = new ListNode(-1);

            buckets[i] = newNode;
        }
    }
    
    void add(int key) {
        int index = key % 1000;

        ListNode* head = buckets[index];
        ListNode* curr = head;
        ListNode* prev = nullptr;
        while (curr) {
            if (curr->val == key) {
                return;
            }

            prev = curr;
            curr = curr->next;
        }

        ListNode* newNode = new ListNode(key);
        prev->next = newNode;
    }
    
    void remove(int key) {
        int index = key % 1000;

        ListNode* head = buckets[index];
        ListNode* curr = head;
        ListNode* prev = nullptr;
        while (curr) {
            if (curr->val == key) {
                prev->next = curr->next;
                delete curr;
                return;
            }
            
            prev = curr;
            curr = curr->next;
        }
    }
    
    bool contains(int key) {
        int index = key % 1000;

        ListNode* head = buckets[index];
        ListNode* curr = head;
        ListNode* prev = nullptr;
        while (curr) {
            if (curr->val == key) {
                return true;
            }

            prev = curr;
            curr = curr->next;
        }

        return false;
    }
};

// add(10)

// [ ,  ,  , ,  ,  ,] 



/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */