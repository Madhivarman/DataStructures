/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
function freqCounter(strings){
    var hashmap = {};
    for(i=0; i<strings.length; i++){
        if(strings[i] in hashmap){
            hashmap[strings[i]] += 1;
        }else{
            hashmap[strings[i]] = 1;
        }
    }
    
    return hashmap
    
}
var isAnagram = function(s, t) {
    var bool_ = false;
    
    //if both are same
    if(s == t){
        return true;
    }
    // if length mismatch
    if(s.length != t.length){
        return false;
    }
    
    //hashmap
    let shashmap = freqCounter(s);
    let thashmap = freqCounter(t);
    
    for(i=0; i<s.length; i++){
        if(shashmap[s[i]]==thashmap[s[i]]){
            bool_ = true;
        }else{
            bool_ = false;
            console.log(s[i]);
            return bool_;
        }
    }
    
    return bool_;
};

console.log(isAnagram('anagram', 'nagaram'))