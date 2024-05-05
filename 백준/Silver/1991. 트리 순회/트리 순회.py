import sys
sys.setrecursionlimit(10**9)
# (루트) (왼쪽 자식) (오른쪽 자식)
def preorder_traverse(root):
    global tree
    
    if tree[root][0]=='.' and tree[root][1]=='.' : # leaf node
        return root
    elif tree[root][0]=='.' : # 오른쪽 자식만 있다면 
        return root + preorder_traverse(tree[root][1])
    elif tree[root][1]=='.' : # 왼쪽 자식만 있다면
        return root + preorder_traverse(tree[root][0])
    else : # 자식이 다 있다면
        return root + preorder_traverse(tree[root][0]) + preorder_traverse(tree[root][1])

# (왼쪽 자식) (루트) (오른쪽 자식)
def inorder_traverse(root):
    global tree
    
    if tree[root][0]=='.' and tree[root][1]=='.' : # leaf node
        return root
    elif tree[root][0]=='.' : # 오른쪽 자식만 있다면 
        return root + inorder_traverse(tree[root][1])
    elif tree[root][1]=='.' : # 왼쪽 자식만 있다면
        return inorder_traverse(tree[root][0]) + root
    else : # 자식이 다 있다면
        return inorder_traverse(tree[root][0]) + root + inorder_traverse(tree[root][1])

# (왼쪽 자식) (오른쪽 자식) (루트)
def postorder_traverse(root):
    global tree
    
    if tree[root][0]=='.' and tree[root][1]=='.' : # leaf node
        return root
    elif tree[root][0]=='.' : # 오른쪽 자식만 있다면 
        return postorder_traverse(tree[root][1]) + root
    elif tree[root][1]=='.' : # 왼쪽 자식만 있다면
        return postorder_traverse(tree[root][0]) + root   
    else : # 자식이 다 있다면
        return postorder_traverse(tree[root][0]) + postorder_traverse(tree[root][1]) + root 
    
n=int(input())
tree=dict()
for _ in range(n) :
    query=list(sys.stdin.readline().split())
    tree[query[0]] = (query[1], query[2])

print(preorder_traverse('A'))
print(inorder_traverse('A'))
print(postorder_traverse('A'))
