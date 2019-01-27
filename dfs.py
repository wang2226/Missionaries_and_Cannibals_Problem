class State():
    def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight, action):
        self.cannibalLeft = cannibalLeft
        self.missionaryLeft = missionaryLeft
        self.boat = boat
        self.cannibalRight = cannibalRight
        self.missionaryRight = missionaryRight
        self.action = action
        self.parent = None

    def is_goal(self):
        if self.cannibalLeft == 0 and self.missionaryLeft == 0:
            return True
        else:
            return False

    def is_valid(self):
        if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
               and self.boat == other.boat and self.cannibalRight == other.cannibalRight \
               and self.missionaryRight == other.missionaryRight

    def __hash__(self):
        return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))


def successors(cur_state):
    children = list()
    if cur_state.boat == 'left':
        # send two missionaries from left to right
        new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
                          cur_state.cannibalRight, cur_state.missionaryRight + 2,
                          "send two missionaries from left to right")
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send two cannibals from left to right
        new_state = State(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
                          cur_state.cannibalRight + 2, cur_state.missionaryRight,
                          "send two cannibals from left to right")
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send one missionary and one cannibal from left to right
        new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
                          cur_state.cannibalRight + 1, cur_state.missionaryRight + 1,
                          "send one missionary and one cannibal from left to right")
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send one missionary from left to right
        new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
                          cur_state.cannibalRight, cur_state.missionaryRight + 1,
                          "send one missionary from left to right")
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send one cannibal from left to right
        new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
                          cur_state.cannibalRight + 1, cur_state.missionaryRight,
                          "send one cannibal from left to right")
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
    else:
        # send two missionaries from right to left
        new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
                          cur_state.cannibalRight, cur_state.missionaryRight - 2,
                          "send two missionaries from right to left")
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send two cannibals from right to left
        new_state = State(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
                          cur_state.cannibalRight - 2, cur_state.missionaryRight,
                          "send two cannibals from right to left")
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send one missionary and one cannibal from right to left
        new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
                          cur_state.cannibalRight - 1, cur_state.missionaryRight - 1,
                          "send one missionary and one cannibal from right to left")
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send one missionary from right to left
        new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
                          cur_state.cannibalRight, cur_state.missionaryRight - 1,
                          "send one missionary from right to left")
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send one cannibal from right to left
        new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
                          cur_state.cannibalRight - 1, cur_state.missionaryRight,
                          "send one cannibal from right to left")
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

    return children


def depth_limited_search(node, depth):
    if node.is_goal():
        return node
    elif depth == 0:
        return None
    else:
        children = successors(node)
        for child in children:
            result = depth_limited_search(child, depth - 1)
            if result:
                return result
        return None


def iterative_deepening_depth_first_search(root, max_depth):
    for i in range(max_depth):
        return depth_limited_search(root, max_depth)


def print_solution(solution):
    path = list()
    path.append(solution)
    parent = solution.parent

    while parent:
        path.append(parent)
        parent = parent.parent

    print("initial state: <3,3,left,0,0>")
    for i in range(1, len(path)):
        state = path[len(path) - i - 1]
        print "action" + str(i) + ": " + state.action
        if i == len(path) - 1:
            print "goal state" + str(i) + ": <" + str(state.cannibalLeft) + "," + str(state.missionaryLeft) \
                  + "," + state.boat + "," + str(state.cannibalRight) + "," + \
                  str(state.missionaryRight) + ">"
        else:
            print "state" + str(i) + ": <" + str(state.cannibalLeft) + "," + str(state.missionaryLeft) \
                  + "," + state.boat + "," + str(state.cannibalRight) + "," + \
                  str(state.missionaryRight) + ">"


def main():
    initial_state = State(3, 3, 'left', 0, 0, "no action yet")
    solution = iterative_deepening_depth_first_search(initial_state, 11)
    print("Format: <cannibal left,missionary left,boat position,cannibal right,missionary right>")
    print_solution(solution)


# if called from the command line, call main()
if __name__ == "__main__":
    main()
