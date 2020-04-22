/**
 * Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice 
 * and return the new length.Do not allocate extra space for another array, you must do 
 * this by modifying the input array in-place with O(1) extra memory.
 */

var removeDuplicates = function(num_lists){
    var hashmap = {}
    var pointer = 0;

    //iterate through the num_lists
    while(pointer < num_lists.length){

        //console.log(pointer, num_lists);

        if(hashmap[num_lists[pointer]] == 2){
            num_lists.splice(pointer, 1);
            pointer--; //decrement the pointer
        }else{
            if(num_lists[pointer] in hashmap){
                //increment the count
                hashmap[num_lists[pointer]] =  hashmap[num_lists[pointer]]+1;
            }else{
                hashmap[num_lists[pointer]] = 1 //start count
            }
        }
        pointer++;
    }

    return num_lists.length;
}


console.log(removeDuplicates([1,1,1,2,2,3]))
console.log(removeDuplicates([0,0,1,1,1,1,2,3,3]))