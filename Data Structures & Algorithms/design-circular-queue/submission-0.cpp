class MyCircularQueue {
public:
    struct Node {
        int val;
        Node* next;
        Node* prev;

        Node() = default;
        Node(int val) : val(val), next(nullptr) { }
    };
    int size;
    int capacity;
    Node* head;
    Node* tail;

    MyCircularQueue(int k) {
        this->head = new Node();
        this->tail = new Node();
        this->size = 0;
        this->capacity = k;

        this->head->next = this->tail;
        this->tail->prev = this->head;
    }
    
    bool enQueue(int value) {
        if (isFull()) return false;

        Node* newNode = new Node(value);

        this->tail->prev->next = newNode;
        newNode->prev = this->tail->prev;
        this->tail->prev = newNode;
        newNode->next = this->tail;
        
        size++;
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()) return false;
        
        Node* toDelete = this->head->next;
        this->head->next = toDelete->next;
        toDelete->next->prev = this->head;

        delete toDelete;
        size--;
        return true;
    }
    
    int Front() {
        if (isEmpty()) return -1;

        return this->head->next->val;
    }
    
    int Rear() {
        if (isEmpty()) return -1;

        return this->tail->prev->val;
    }
    
    bool isEmpty() {
        return (this->size == 0);
    }
    
    bool isFull() {
        return (this->size == this->capacity);
    }
};


/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */