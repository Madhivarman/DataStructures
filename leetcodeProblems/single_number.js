/**
 * Given a non-empty array of integers, every element appears twice except for one. Find that single one.
 * Note:
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
*/

var singleNumber = function(numlists){
    number = null;
    var hashmap = {};
    //iterate through the num lists
    for(i=0; i < numlists.length; i++){
        if(numlists[i] in hashmap){
            hashmap[numlists[i]] = hashmap[numlists[i]]+1;
        }else{
            hashmap[numlists[i]] = 1;
        }
    }
    return Object.keys(hashmap).find(key => hashmap[key] === 1);
}

console.log(singleNumber([2,2,1]));