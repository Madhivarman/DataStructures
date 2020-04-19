/**
 * Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
 * The number of elements initialized in nums1 and nums2 are m and n respectively.
 * You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
 */

var mergeSortArray =  function(nums1, m, nums2, n){
    var first = m -1;
    var second = n - 1;

    for(let i=m+n-1; i >=0; i--){
        //if we completed traversing through the nums2
        //array then break
        if(second < 0){
            break
        }

        if(nums2[second] > nums1[first]){
            nums1[i] = nums2[second]
            second--;
        }else{
            nums1[i] = nums1[first];
            first--;
        }
    }
    //return nums1
    return nums1
}

console.log(mergeSortArray([1,2,3,0,0,0], 3, [2,5,6], 3))