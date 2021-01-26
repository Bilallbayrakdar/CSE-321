import numpy as np
    
class item:
    def __init__(self, w, v):
        self.w = w # Agirlik
        self.v = v # Deger
    
    def __repr__(self):
        return "item: W: "+str(self.w) + ", V: "+str(self.v)
    
class Knapsack:
    def __init__(self, wlimit):
        self.wlimit = wlimit # Agirlik limiti
        self.items = [] # esyalar

    def addItem(self,item):
        self.items.append(item)
    
    def addItems(self,items):
        for item in items:
            self.addItem(item)

 # Knapsack problem sinifi icin cozum metodu
    def solve(self):
        n_items = len(self.items) # esya sayisi
        w2 = np.zeros([n_items+1, self.wlimit+1]) # (esya sayisi + 1) x (ağırlık limiti+1)
        for i in range(1,n_items+1): # her satir icin
            for k in range(0,self.wlimit+1): # her sutun icin
                if self.items[i-1].w < k+1: # Formulasyon
                    w2[i][k] = max(self.items[i-1].v + w2[i-1][k - self.items[i-1].w], w2[i-1][k])
                else:
                    w2[i][k] = w2[i-1][k]
        return w2 # matrisi dondur

    def reverse(self):
        w2 = self.solve()
        sol_list = []
        i=-1
        j=-1
        row_c = len(w2)
        while i != -row_c:
            if w2[i][j] == w2[i][j-1]:
                j -= 1
            elif w2[i][j] == w2[i-1][j]:
                i -= 1
            else:
                sol_list.append(self.items[i])
                j -= self.items[i].w
                i -= 1
        return sol_list

k1 = item(5,10)
k2 = item(4,4)
k3 = item(2,3)
items = [k1,k2,k3]

bag = Knapsack(10)
bag.addItems(items)

sol_list = bag.reverse()
print (sol_list)