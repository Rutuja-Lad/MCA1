
class StackArray {
    constructor(maxcapacity) {
        this.data = Array(maxcapacity)
        this.capacity = maxcapacity
        this.currentlength = 0
        this.top = -1
    }
    isFull() {
        return this.currentlength == this.capacity;
    }
    isEmpty() {
        return this.currentlength == 0;
    }
    push(data) {
        if (this.isFull()) {
            return "overflow";
        } else {
            this.top = this.top + 1;
            this.data[this.top] = data;
            this.currentlength++;
        }
        return data
    }
    pop() {
        if (this.isEmpty()) {
            return "underflow";
        }
        else {
            let temp = this.data[this.top]
            this.data[this.top] = temp.next;
            this.top = this.top - 1;
            this.currentlength--;
            return temp;
        }
        
    }
    peek() {
        return this.data[this.top];
    }
}
const p5 = new StackArray(100);
console.log(p5);
console.log("push:");
p5.push(200);
p5.push(300);
console.log(p5);
console.log("peek:");
console.log(p5.peek());
console.log("pop:");
p5.pop();
console.log(p5);
console.log("peek:");
console.log(p5.peek());