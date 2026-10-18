class Node {
public:
    int val_;
    int key_;
    Node *prev_;
    Node *next_;

    Node() = default;

    Node(int key, int val) {
        this->key_ = key;
        this->val_ = val;
    }
};

class LRUCache {
private:
    std::unordered_map<int, Node*> keyToNode_{};
    Node* head_{};
    Node* tail_{};
    int capacity_{};
    int size_{};

public:
    LRUCache(int capacity) {
        this->capacity_ = capacity;
        this->size_ = 0;
        this->head_ = new Node();
        this->tail_ = new Node();

        this->head_->next_ = this->tail_;
        this->head_->prev_ = nullptr;
        this->tail_->prev_ = this->head_;
        this->tail_->next_ = nullptr;
    }

    // insert to hash map in caller function
    void insertHead(Node* toInsert) {
        toInsert->next_ = this->head_->next_;
        toInsert->prev_ = this->head_;
        this->head_->next_->prev_ = toInsert;
        this->head_->next_ = toInsert;
    }

    // remove from hash map and delete in caller function
    void removeNode(Node *toRemove) { 
        toRemove->prev_->next_ = toRemove->next_;
        toRemove->next_->prev_ = toRemove->prev_;
    }
    
    int get(int key) {
        if (this->keyToNode_.contains(key)) {
            Node* currNode = this->keyToNode_[key];
            removeNode(currNode);
            insertHead(currNode);
            return currNode->val_;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (this->keyToNode_.contains(key)) {
            // update val of node
            Node* currNode = this->keyToNode_[key];
            currNode->val_ = value;

            removeNode(currNode);
            insertHead(currNode);
        }
        else {
            Node* newNode = new Node(key, value);
            this->keyToNode_[key] = newNode;

            // remove from tail if full
            if (this->size_ == this->capacity_) {
                Node *toRemove = this->tail_->prev_;

                if (toRemove == this->head_) {
                    return;
                }

                removeNode(toRemove);
                this->keyToNode_.erase(toRemove->key_);
                delete toRemove;
                this->size_--;
            }

            // insert to head
            insertHead(newNode);
            this->size_++;
        }
    }
};



// capacity = 3

// put: {1 --> 10}
// get 1
// put: {1 --> 10, 2 --> 20}
// put: {1 --> 10, 2 --> 20, 3 --> 30}
// get 2
// get 1
// put: {1 --> 10, 2 --> 20, 4 --> 40}, evict key = 3
// put: {1 --> 10, 5 --> 50, 4 --> 40}, evict key = 2


// 1

// 2 <--> 1

// 3 <--> 2 <--> 1

// 2 <--> 3 <--> 1

// 1 <--> 2 <--> 3

// evict 3, put in 4
// 4 <--> 1 <--> 2

// evict 2, put in 5
// 5 <--> 4 <--> 1


// head <-> 1 <-> 2 <-> tail

// 

