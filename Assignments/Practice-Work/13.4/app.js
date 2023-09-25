function filterOutOdds() {
    var nums = Array.prototype.slice.call(arguments);
    return nums.filter(function(num) {
      return num % 2 === 0
    });
  }

  const filterOutOdds = (...args) => args.filter(nums => nums % 2 === 0);

  const findMin = (...args) => Math.min(args)

  const mergeObjects = (obj1, obj2) => ({...obj1, ...obj2})

  const doubleAndReturnArgs = (arr, ...args) => [...arr, args.map(num => num *2)]

  /** remove a random element in the items array
and return a new array without that item. */

const removeRandom = items => {
    randomIndex = Math.random() *items.length - 1;
    items.pop(randomIndex);
    let newArray = (...items) => newArray;
    return newArray;
}

/** Return a new array with every item in array1 and array2. */

// function extend(array1, array2) {

// }

const extend = (array1, array2) => [...array1, ...array2];

/** Return a new object with all the keys and values
from obj and a new key/value pair */

// function addKeyVal(obj, key, val) {

// }

const addKeyVal = (obj, key, val) => {
    return {...obj, [key]: val}
};


/** Return a new object with a key removed. */

// function removeKey(obj, key) {

// }
const removeKey = (obj, key) => {
    let newObj = {...obj}
    delete newObj[key]
    return newArray;
}


/** Combine two objects and return a new object. */

// function combine(obj1, obj2) {

// }

const combine = (obj1, obj2) => {
    ({...obj1, ...obj2});
}

/** Return a new object with a modified key and value. */

// function update(obj, key, val) {

// }

const update = (obj, key, val) => {
    ({...obj, [key]: val})
}



