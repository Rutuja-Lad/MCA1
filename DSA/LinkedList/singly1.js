
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}
class Insert {
    constructor(data) {
        const newNode = new Node(data);
        this.head = newNode;
        this.tail = newNode;
        this.length = 1;
    }
    push(data) {
        const newNode = new Node(data);
        if (!this.length) {
            this.head = newNode;
            this.tail = newNode;
            this.length = 1;
        }
        else {
            newNode.next = this.head;
            this.head = newNode;
            this.length++;
        }
    }
    pop() {
        if (!this.length) {
            return undefined;
        }
        if (this.length == 1) {
            this.head = null;
            this.tail = null;
        }
        else {
            let temp = this.head;
            this.head = temp.next
            temp.next = null;
            this.length--;
        }
    }
}
const p = new Insert(5);
console.log(p);
p.push(10);
console.log(p);
p.push(15);
console.log(p);
p.push(20);
console.log(p);
p.pop();
console.log(p);
p.pop();
console.log(p);