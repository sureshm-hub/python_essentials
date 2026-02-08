from typing import List, Iterator, Optional

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

class NestedInteger:
    pass


class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> list[NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack: List[Iterator["NestedInteger"]] = []
        if nestedList is not None:
            self.stack.append(iter(nestedList))
        self._next: Optional[int] = None # cached next integer

    def _advance(self) -> bool:
        while self.stack:
            it = self.stack[-1]
            try:
                cur = next(it)
            except StopIteration:
                self.stack.pop()
                continue

            if cur.isInteger():
                self._next = cur.getInteger()
                return True
            else:
                self.stack.append(iter(cur.getList()))
        return False

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        ans = self._next
        self._next = None
        return ans

    def hasNext(self) -> bool:
        if self._next is not None:
            return True
        return self._advance()


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())