class Node:
    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage: str):
        self.currPage = Node(homepage)

    def visit(self, url: str) -> None:
        newPage = Node(url, None, self.currPage)
        self.currPage.next = newPage
        self.currPage = newPage

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.currPage.prev:
                return self.currPage.val
            self.currPage = self.currPage.prev
        return self.currPage.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.currPage.next:
                return self.currPage.val
            self.currPage = self.currPage.next
        return self.currPage.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
