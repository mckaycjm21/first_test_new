/** Node: node for a singly linked list. */

class Node {
    constructor(val) {
      this.val = val;
      this.next = null;
    }
  }
  
  /** LinkedList: chained together nodes. */
  
  class LinkedList {
    constructor(vals = []) {
      this.head = null;
      this.tail = null;
      this.length = 0;
  
      for (let val of vals) this.push(val);
    }
  
    /** push(val): add new value to end of list. */
  
    push(val) {
      let newNode = new Node(val)
      if (head) {
        this.tail.next = newNode
      }
      else{
        this.head = newNode
      }
      this.tail = newNode

      this.length += 1;
  
      return undefined
    }
  
    /** unshift(val): add new value to start of list. */
  
    unshift(val) {
      let newNode = new Node(val)
      currentNode = this.head
      if (currentNode) {
        newNode.next = currentNode
        this.head = newNode
      }
      else{
        this.head = newNode
        this.tail = newNode
      }
      this.length += 1;
      
      return undefined
    }
  
    /** pop(): return & remove last item. */
  
    pop() {
      if(list){
  
      }
      else{
        error message "list is empty"
      }
  
      return this.tail.val
    }
  
    /** shift(): return & remove first item. */
  
    shift() {
      if(list){
  
      }
      else{
        error message "list is empty"
      }
      return this.head.val
    }
  
    /** getAt(idx): get val at idx. */
  
    getAt(idx) {
      if(val at indx){
  
      }
      else{
        error message "point at index is invalid"
      }
      return currentValAtIndx
  
    }
  
    /** setAt(idx, val): set val at idx to val */
  
    setAt(idx, val) {
      if(val at indx){
  
      }
      else{
        error message "point at index is invalid"
      }    
      return f`{val} was set at index of {idx}`
    }
  
    /** insertAt(idx, val): add node w/val before idx. */
  
    insertAt(idx, val) {
      if(val at indx){
  
      }
      else{
        error message "point at index is invalid"
      }    
      return undefined
    }
  
    /** removeAt(idx): return & remove item at idx, */
  
    removeAt(idx) {
      if(val at indx){
  
      }
      else{
        error message "point at index is invalid"
      }    
      return valAtPosOfIdx    
    }
  
    /** average(): return an average of all values in the list */
  
    average() {
      
    }
  }
  
  module.exports = LinkedList;
  