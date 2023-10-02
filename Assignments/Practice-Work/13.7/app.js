// new Set([1,1,2,2,3,4])

// returns [1,2,3,4]



// [...new Set("referee")].join("")

//returns "ref"



// let m = new Map();
// m.set([1,2,3], true);
// m.set([1,2,3], false);

// m = ([1,2,3], true)
// m = ([1,2,3], false)



// hasDuplicate([1,3,2,1]) // true
// hasDuplicate([1,5,-1,4]) // false

// const hasDuplicate = arr => new Set(arr).size != arr.length;



// vowelCount('awesome') // Map { 'a' => 1, 'e' => 2, 'o' => 1 }
// vowelCount('Colt') // Map { 'o' => 1 }

function checkVowel(userInput){
    return "aeiou".includes(userInput);
}

function vowelCount(userInput){
    const   vowelMap = new Map();
    for (let letter of userInput){
        if(checkVowel(letter)){
            if (vowelMap.has(letter)){
                vowelMap.set(letter, vowelMap.get(letter) + 1);
            }
            else{
                vowelMap.set(letter, 1);
            }
        }
    }
    return vowelMap;
}