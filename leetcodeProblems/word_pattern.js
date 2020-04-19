/**
 * @param {string} pattern
 * @param {string} str
 * @return {boolean}
 */
var wordPattern = function(pattern, str) {
    var matched = true;
    var hashmap = {}; //to store matching key value pairs
    
    //slice the string by space
    let str_list = str.split(" ");
    let words_already_assigned = [];
    
    //if string and pattern both are same
    if((str == pattern) & (str_list.length == pattern.list)){
        return matched;
    }
    
    //check if both of the lists are same
    if(pattern.length != str_list.length){
        matched = false;
        return matched;
    }
    
    for(i=0; i < pattern.length; i++){
        if((pattern[i] in hashmap) & (hashmap[pattern[i]] == str_list[i])){
            continue;
        }else{
            if((words_already_assigned.includes(str_list[i])) || (pattern[i] in hashmap)){
                matched=false;
                return matched;
            }
            hashmap[pattern[i]] = str_list[i];
            words_already_assigned.push(str_list[i]);
        }
    }
    
    return matched;
};

console.log(wordPattern("abba", "dog dog dog dog"))