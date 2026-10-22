class MyHashMap {
public:
    struct ListNode {
        ListNode* next{};
        int key{};
        int val{};

        ListNode() = default;
        ListNode(int key, int val) : key(key), val(val) {}
    };
    static int constexpr numBuckets = 1000;
    std::array<ListNode*, numBuckets> buckets{};

    MyHashMap() {
        for (int i = 0; i < numBuckets; i++) {
            ListNode* sentinel = new ListNode(-1, -1);
            buckets[i] = sentinel;
        }
    }
    
    void put(int key, int value) {
        int index = key % 1000;

        ListNode* curr = buckets[index];
        ListNode* prev = nullptr;
        while (curr) {
            if (curr->key == key) {
                curr->val = value;
                return;
            }

            prev = curr;
            curr = curr->next;
        }

        ListNode* newNode = new ListNode(key, value);
        prev->next = newNode;
    }
    
    int get(int key) {
        int index = key % 1000;

        ListNode* curr = buckets[index];
        ListNode* prev = nullptr;
        while (curr) {
            if (curr->key == key) {
                return curr->val;
            }

            prev = curr;
            curr = curr->next;
        }

        return -1;
    }
    
    void remove(int key) {
        int index = key % 1000;

        ListNode* curr = buckets[index];
        ListNode* prev = nullptr;
        while (curr) {
            if (curr->key == key) {
                prev->next = curr->next;
                delete curr;
                return;
            }

            prev = curr;
            curr = curr->next;
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */