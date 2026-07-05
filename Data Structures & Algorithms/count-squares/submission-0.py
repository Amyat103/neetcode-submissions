class CountSquares:
    """
    input will be points [[1,2]]...add them into a "Plain" or DS set() dict()
    later on, add, itll give a new point
    - dont add, but calc how many squares, points can be used again if one of the point have duplicate
    - set() out of con -- remove dups
    pre process the count, dict (x,y) : count
    count() - find 4 points and return how many?
    we can use anothe rpoint to pin and check if square
    2,1 - for _ in 4 dir, if(3,1)(1,0)(3,0)(1,2) exist, then use those as pin and calcualte 
    """
    def __init__(self):
        self.pointCount = defaultdict(int)
        self.seen = []

    def add(self, point: List[int]) -> None:
        self.pointCount[tuple(point)] += 1
        self.seen.append(point)

    def count(self, point: List[int]) -> int:
        ans = 0
        px, py = point

        for x, y in self.seen:
            if (px == x and py == y) or (abs(px - x) != abs(py - y)):
                continue
            ans += self.pointCount[(x,py)] * self.pointCount[(px,y)]
        return ans