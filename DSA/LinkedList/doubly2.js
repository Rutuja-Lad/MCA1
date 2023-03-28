// JavaScript source code
class Node {
    constructor(data) {
        this.data = data;
        this.prev = null;
        this.next = null;
    }
}
class doubly2 {
    constructor(data)
    {
        const newNode = new Node(data);
        this.head = newNode;
        this.tail = newNode;
        this.lenght = 1;
    }
    push(data)
    {
        const newNode = new Node(data);
        if (!this.length)
        {
            this.head = newNode;
            this.tail = newNode;
            this.lenght = 1;
        }
        else {
            this.tail.next = newNode;
            this.prev = this.tail;
            this.tail = newNode;
            this.lenght++;
        }

    }
    pop() {
        if (!this.length) {
            return undefined;
        }
        if (this.length == 1)
        {
            this.head = null;
            this.tail = null;
        }
 else
 {
    let temp = this.head;
    let prev = this.head;
    while (temp.next) {
        prev = temp;
        temp = temp.next;
    }
    this.tail = prev;
    this.tail.next = null;
    this.length--;
}
 }
}
const p = new doubly2(35);
console.log(p);
console.log("push:")
p.push(40);;
console.log(p);
console.log("pop:")
p.pop();
console.log(p)