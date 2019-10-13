class Node():
  def __init__(self, val):
      self.data = val
      self.left = None
      self.right = None

def invertTree(root):
  if root == None:
      return
  else:
      #traverse till it reaches the leaf
      invertTree(root.left)
      invertTree(root.right)
      
      #once subtrees are swapped just
      temp = root.left
      root.left = root.right
      root.right = temp
  
  return root

def printPreOrder(root):
  if root:
    print(root.data, end=',')
    printPreOrder(root.left)
    printPreOrder(root.right)
  
if __name__ == '__main__':
  
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    
    sol = invertTree(root)
    printPreOrder(sol)
