class Node {
    constructor(data, priority) {
        this.data = data;
        this.priority = priority;
        this.next = null;
    }
}
class priorityqueue {
    constructor() {
        this.head = null;
    }
    enque(data, priority) {
        let newNode = new Node(data, priority);
        if (this.isEmpty() || newNode.priority < this.head.priority) {
            newNode.next = this.head;
            this.head = newNode;
        }
        else {
            let current = this.head;
            while (current.next != null && current.next.priority <= newNode.priority) {
                current = current.next;
            }
            newNode.next = current.next;
            current.next = newNode;
        }
    }
    deque() {
        if (this.isEmpty()) {
            return "underflow";
        }
        let temp = this.head;
        this.head = this.head.next;
        return temp.data;
    }
    peek() {
        if (this.isEmpty()) {
            return "no element in queue";
        }
        return this.head.data;
    }
    isEmpty() {
        
        return this.head == null;
    }
    printqueue() {
        let current = this.head;
        while (current != null) {
            console.log(current.data, current.priority);
            current = current.next;
        }
    }
}
let q = new priorityqueue();
q.enque("a", 20);
q.enque("b", 30);
q.enque("c", 40);
q.enque("d", 70);
q.enque("e", 10);
q.enque("f", 90);
q.printqueue();
q.peek();
q.deque();
q.printqueue();
