class node:
    def __init__(self,dt):
        self.left=None
        self.right=None
        self.data=dt

rt=node(50)
rt.left=(node(35))
rt.right=node(60)
rt.left.left=node(30)
rt.left.right=node(40)
rt.right.left=node(55)
rt.right.right=node(65)

def preorder(p):
    if(p):
        print(p.data)
        pretorder(p.left)
        preorder(p.right)

preorder(rt)

