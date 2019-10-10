"""
  Generating N! possible strings from the given string.
  Note:
    With this below method, if same characters are repeated, then
    there will be duplicate strings. To overcome this, we can follow
    two methods
      1. Using set to check, if the generated string is already present. If
      it's already present just ignore and generate next possible string. Time
      complexity for this method is O(N!)* N. Generating N! number of possibilites 
      plus checking if the string is present in the set or not. 
      2. Using Word Counter we can solve this duplication problem by O(N!). Will be
      updating shortly
"""
def toString(List):
    return ''.join(List)

def permutation(a, l, r):
    if l == r:
        print(toString(a))
        print("\n\n")
    else:
        for i in range(l, r+1):
            print("values:i:{}, l:{}, r:{}".format(i, l, r))
            a[l], a[i] = a[i], a[l]
            permutation(a, l+1, r) #create permutation
            a[l], a[i] = a[i], a[l]

string = "abcd"
N = len(string)
asList = list(string)
