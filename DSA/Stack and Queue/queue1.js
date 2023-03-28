
class node {
    constructor(value) {
        if (value == null || value == undefined) {
            throw new error("intialize with valid");
        }
        this.value = value;
        this.next = null
    }
}
class Queue1 {
    constructor(value) {
        const newnode = new node(value);
        this.front = newnode;
        this.rear = this.front
        this.length = 1;
    }
    enque(value) {
        const newnode = new node(value);
        if (!this.length) {
            this.front = newnode;
            this.rear = this.front;
        }
        else {
            this.rear.next = newnode;
            this.rear = newnode;
        }
        this.length++;
        return this;
    }
    deque() {
        let temp = this.front;
        if (!this.length) return undefined;
        if (this.length == 1) {
            this.front = null;
            this.rear = null;
        }
        else {
            temp = this.front;
            this.front = temp.next;
            temp.next = null;
            
        }
        this.length--;
        return this;
    }
    peek() {
        if (!this.isEmpty()) {
            return this.front.value;
        }
    }
    isEmpty() {
        return this.front === null;
    }
}
const q1 = new Queue1(100);
q1.enque(200);
q1.enque(300);
q1.enque(400);
q1.enque(500);
console.log(q1);
q1.deque();
q1.deque();
console.log(q1);
console.log(q1.peek());