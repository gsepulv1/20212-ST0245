class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        # La inserción de un nuevo nodo debe agregarlo como un nodo hoja en el lugar adecuado.

        # Si no tenemos datos en el nodo asignamos el valor y regresamos. Esto se puede dar creando la raiz
        if not self.val:
            self.val = val
            return

        # Si el valor dado es menor o igual  que el valor de nuestro nodo y ya tenemos un hijo izquierdo, 
        # entonces llamamos recursivamente insert  a nuesto hijo izquierdo
        # Si todavía no tenemos un hijo izquierdo, convertimos el valor dado en nuestro nuevo hijo izquierdo
        if val <= self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
        # si no entro por el anterior es que es mayor que el  que nuestro nodo y debemos llevarlo a la derecha
        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
    # funcion recursiva para obtener el menor valor
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val
    # funcion recursiva para obtener el mayor  valor en el arbol 
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
   # funcion de borrado
    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals
nums = [14,15,4,18,3,9,7,5,20,16,17]
bst = BSTNode()
for num in nums:
    bst.insert(num)
print("preorder:")
print(bst.preorder([]))
print("#")

print("postorder:")
print(bst.postorder([]))
print("#")

print("inorder:")
print(bst.inorder([]))
print("#")
print("menor")
print(bst.get_min())

nums2 = [14,15,4,18,3,9,7,5,20,16,17,14,4,3]
bst2 = BSTNode()
for num2 in nums2:
    bst2.insert(num2)
print("preorden arbol 2:")
print(bst2.preorder([]))
print("#")

print("postorden arbol 2:")
print(bst2.postorder([]))
print("#")

print("inorden arbol 2:")
print(bst2.inorder([]))
print("#")
   
