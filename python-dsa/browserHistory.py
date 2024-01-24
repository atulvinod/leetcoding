
class Node:
    def __init__(self, url: str, next=None, prev=None) -> None:
        self.url = url
        self.next = next;
        self.prev = prev
        
        

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next

    def back(self, steps: int) -> str:
        while(steps and self.root.prev):
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps: int) -> str:
        while(steps and self.root.next):
            self.root = self.root.next
            steps -= 1
        return self.root.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

ops = ["BrowserHistory","visit","visit","back","visit","visit","back","forward","visit","visit","visit","visit","visit","visit","forward","forward","visit","back","visit","visit","visit","visit","forward","visit","visit","visit"]

arg = [["momn.com"],["bx.com"],["bjyfmln.com"],[3],["ijtrqk.com"],["dft.com"],[10],[10],["yc.com"],["yhl.com"],["xynxvix.com"],["izfscdv.com"],["cdenhm.com"],["ocgcjz.com"],[5],[5],["gtd.com"],[9],["hfeour.com"],["ghmh.com"],["nnm.com"],["knm.com"],[4],["cbtg.com"],["acyvwod.com"],["mydr.com"]]

obj = None

for i in range(len(ops)):
    if ops[i] == "BrowserHistory":
        obj = BrowserHistory(arg[i][0])
        print('home ', arg[i][0])
    elif ops[i] == "visit":
        print('visit ',arg[i][0],"\n")
        obj.visit(arg[i][0])
    elif ops[i] == "forward":
        print('forward > ',arg[i][0] ," ",obj.forward(arg[i][0]),'\n')
    elif ops[i] == "back":
        print('back < ',arg[i][0]," ",obj.back(arg[i][0]),'\n')