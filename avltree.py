def height(self):
    if self.isempty():
        return(0)
    else:
        return 1 + max(self.left.height(), self.right.height())

def update_height(self):
 self.height = 1 + max(self.left.height, self.right.height)

def slope(self):
 return self.left.height - self.right.height
   
def rebalance(self):
    if self.slope() in (-1, 0, 1):
        return
        
    elif self.slope() >= 2:
        if self.left.slope() < 0:
            self.rightrotate()
            self.right.update_height()
            self.update_height()
            
            self.right.rightrotate()
            self.right.right.update_height()
            self.right.update_height()
            self.update_height()
            
            self.leftrotate()
            self.left.update_height()
            self.update_height()
            
        else:
            self.rightrotate()
            self.update_height()
            
    elif self.slope() <= 2:
        if self.right.slope() > 0:
            self.leftrotate()
            self.left.update_height()
            self.update_height()
            
            self.left.leftrotate()
            self.left.left.update_height()
            self.left.update_height()
            
            self.rightrotate()
            self.right.update_height()
            self.update_height()
            
        else:
            self.leftrotate()
            self.update_height()

def insert(self,v):
    if self.isempty():
        self.value = v
        self.left = AVLTree()
        self.right = AVLTree()
        self.update_height()
        
    if v < self.value:
        self.left.insert(v)
        self.update_height()
        self.rebalance()
        
    if v > self.value:
        self.right.insert(v)
        self.update_height()
        self.rebalance()
