// JavaScript source code
class Node {
    constructor(data) {
        this.left = null;
        this.data = data;
        this.right = null;
    }
}
class bst {
    constructor() {
        this.root = null;
    }
    insert(data) {
        const newnode = new Node(data);
        if (this.root == null) {
            this.root = newnode;
        }
        else {
            this.insertnewnode(this.root, newnode);
        }
    }
    insertnewnode(root, newnode) {
        if (newnode.data < root.data) {
            if (root.left == null) {
                root.left = newnode;
            }
            else {
                this.insertnewnode(root.left, newnode);
            }
        }
        else if (newnode.data > root.data) {
            
            if (root.right == null) {
                root.right = newnode;
            }
            else {
                this.insertnewnode(root.right, newnode);
            }
        }
    }
    search(root, data) {
        if (!root) {
            return false;
        }
        if (root.data === data) {
            return true;
        } else if (data < root.data) {
            return this.search(root.left, data);
        } else {
            return this.search(root.right, data);
        }
    }

}
let ob = new bst();
ob.insert(100);
ob.insert(50);
ob.insert(150);
ob.insert(200);
ob.insert(500);
console.log(JSON.stringify(ob));
console.log(ob.search(200));