"""
     finding the median of two arrays with O(log(m+n)).
     Gist:
        a: [a1,a2,a3,a4,a5], b:[b1, b2,b3,b4, b5]
        find the partition point for both the array. 
        consider that the partitioning is happened at a :[[a1,a2],[a3,a4,a5]],
        b:[[b1, b2], [b3,b4,b5]]
        and if this is the test case if a2 <= b3 and b2 <= a3 then if the length of the 
        partioned array is odd then avg(max(a2, b2), min(a3, b3)) if the length
        is even then max(a2, b2)
"""