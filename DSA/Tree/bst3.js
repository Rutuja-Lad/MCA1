// JavaScript source code
class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }
    insert(data) {
        var newNode = new Node(data);
        if (this.root === null) {
            this.root = newNode;
        } else {
            this.insertNode(this.root, newNode);
        }
    }
    insertNode(node, newNode) {
        if (newNode.data < node.data) {
            if (node.left === null) {
                node.left = newNode;
            } else {
                this.insertNode(node.left, newNode);
            }
        } else {
            if (node.right === null) {
                node.right = newNode;
            } else {
                this.insertNode(node.right, newNode);
            }
        }
    }
    MinNode(root) {
        if (!root.left) return root.data;
        else return this.MinNode(root.left);
    }
    MaxNode(root) {
        if (!root.right) return root.data;
        else return this.MaxNode(root.right);
    }
}

const BST = new BinarySearchTree();
BST.insert(100);
BST.insert(300);
BST.insert(600);
BST.insert(10);
BST.insert(400);
BST.insert(900);
BST.insert(1000);
console.log(JSON.stringify(BST));
console.log("minimum node: ")
console.log(BST.MinNode(BST.root));
console.log("maximum node: ")
console.log(BST.MaxNode(BST.root));