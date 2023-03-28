class Circularqueue {
    constructor(maxcapacity) {
      this.data = Array(maxcapacity); //array creation with maxcapacity
      this.capacity = maxcapacity; //capacity property is set to maxcapacity
      this.currentlength = 0; // crrent length is zero
      this.front = -1; //crrently not poinitng to any queue element
      this.rear = -1;
    }
    isFull() {
      return this.currentLength === this.capacity;
    }
    isEmpty() {
      return this.currentLength === 0;
    }
    enqueue(data) {
      if (!this.isFull()) {
        this.rear = (this.rear + 1) % this.capacity; //increment rear pointer by 1   
        this.data[this.rear] = data; //add data and  rear pointer index
        this.currentlength++;
        if (this.front === -1) {
          this.front = this.rear;
        }
      }
  
      return data;
    }
    dequeue() {
      if (this.isEmpty()) {
        return null;
      }
      let temp = this.data[this.front]; // store the front element that need to deleted in temp
      this.data[this.front] = null; //index of that front element will be null
      this.front = (this.front + 1) % this.capacity; //increment front by 1 to delete another element
      this.currentlength --;
      if (this.isEmpty()) {
        this.front = -1;
        this.rear = -1;
      }
      return temp;
    }
    peek() {
      if (!this.isEmpty()) {
        return this.items[this.front];
      }
      return null;
    }
  }
  
  const circular = new Circularqueue(7);
  circular.enqueue(1);
  circular.enqueue(2);
  circular.enqueue(3);
  circular.enqueue(4);
  circular.enqueue(5);
  circular.enqueue(6);
  circular.enqueue(7);
  console.log(circular);
  console.log(circular.dequeue());
  console.log(circular);
  