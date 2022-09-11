from linked_list import linked_list
from node import node

class snake:

    def __init__(self):
        self.rows, self.cols = (10, 10)
        self.grid = []
        self.food = (3, 3)

        for row in range(self.rows):
            r = []
            for col in range(self.cols):
                r.append(' ')
            self.grid.append(r)

        start_node = node(5, 5, head=True)
        second_node = node(4, 5)
        trail_node = node(3, 5, trailing_node=True)

        start_node.setNext(second_node)
        second_node.setPrev(start_node)
        second_node.setNext(trail_node)
        trail_node.setPrev(second_node)

        self.snake = linked_list(start_node)
        self.updateGrid()


    def updateGrid(self):
        # clear whole grid
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col] = ' '

        # draw food position to grid
        self.grid[self.food[0]][self.food[1]] = '*'

        # for each node in the snake, draw to grid
        node = self.snake.getHead()

        self.grid[node.getY()][node.getX()] = "#"

        node = node.getNext()

        while(node != None):
            if(node.isTrailing()):
                self.grid[node.getY()][node.getX()] = "-"
            else:
                self.grid[node.getY()][node.getX()] = "#"

            node = node.getNext()


    def printGrid(self):
        print('###')
        for row in self.grid:
            print(row)

    
    def move(self, direction):
        """
            Moves the snake in a direction and returns True if game continues
            and False if game over.

            Args: 'up', 'down', 'left', 'right'
            Returns: True if successful and False otherwise
        """

        # Check if next move will be food :-)
        # Update snake positions
        self.updateSnakePosition(direction, self.isNextMoveFood(direction))

        # Check if all positions are valid
        if(self.isTheSnakeDead(direction)):
            print('GAME OVER')
        
        else:
            # Update grid
            self.updateGrid()


    def isTheSnakeDead(self, direction):
        """
            Returns True if the snake has died. 
            This may be because it has gone into a wall (wallphobia) or
            it has eaten itself (cannabalism). 

            Returns False if the snake is to live another day (or frame).
        """

        if(direction == 'up'):
            new_position = (self.snake.getHead().getX(), self.snake.getHead().getY() - 1)
        elif(direction == 'down'):
            new_position = (self.snake.getHead().getX(), self.snake.getHead().getY() + 1)
        elif(direction == 'left'):
            new_position = (self.snake.getHead().getX() - 1, self.snake.getHead().getY())
        elif(direction == 'right'):
            new_position = (self.snake.getHead().getX() + 1, self.snake.getHead().getY())

        # Wall check
        if(new_position[0] > 9 or new_position[0] < 0 or new_position[1] > 9 or new_position[1] < 0):
            return True

        # Own-body check
        current_node = self.snake.getHead()

        while(current_node != None):
            if(new_position[0] == current_node.getX() and new_position[1] == current_node.getY()):
                return True
            
            current_node = current_node.getNext()

        return False


    def isNextMoveFood(self, direction):
        """
            Returns True if the next move results in FOOD else False.
            If out of bounds, it also returns False.
        """

        # If position of head + next move is on a food, then awe!
        if(direction == 'up'):
            new_position = (self.snake.getHead().getX(), self.snake.getHead().getY() - 1)
        elif(direction == 'down'):
            new_position = (self.snake.getHead().getX(), self.snake.getHead().getY() + 1)
        elif(direction == 'left'):
            new_position = (self.snake.getHead().getX() - 1, self.snake.getHead().getY())
        elif(direction == 'right'):
            new_position = (self.snake.getHead().getX() + 1, self.snake.getHead().getY())
        
        if(new_position == self.food):
            self.createNewFoodPosition()
            return True

        return False

    
    def createNewFoodPosition(self):
        # destroy old food by making a new food position (that doesnt lie on the snake)
        pass

    
    def updateSnakePosition(self, direction, will_be_growing):
        """
            Updates each position of the snake depending on new move.
            If it will be growing after the move, then the tail stays put,
            and the snake will GROW!
            :-O
        """

        current_node = self.snake.getTail()

        if(will_be_growing):

            print('will be growing!')

            new_node_position = (current_node.getPrev().getX(), current_node.getPrev().getY())

            if(direction == 'up'):
                while(current_node != self.snake.getHead()):
                    # move prev node into next node's position, unless its the trail.
                    if(not current_node.isTrailing()):
                        current_node.setX(current_node.getPrev().getX())
                        current_node.setY(current_node.getPrev().getY())

                    current_node = current_node.getPrev()

                # move the head
                headNode = self.snake.getHead()
                headNode.setY(headNode.getY() - 1)

                # add the new node between the trail (gettail) and snake tail.
                trail_node = self.snake.getTail()
                snake_tail = trail_node.getPrev()
                new_node = node(new_node_position[0], new_node_position[1])

                trail_node.setPrev(new_node)
                snake_tail.setNext(new_node)

                new_node.setNext(trail_node)
                new_node.setPrev(snake_tail)

            if(direction == 'down'):
                while(current_node != self.snake.getHead()):
                    # move prev node into next node's position, unless its the trail.
                    if(not current_node.isTrailing()):
                        current_node.setX(current_node.getPrev().getX())
                        current_node.setY(current_node.getPrev().getY())

                    current_node = current_node.getPrev()

                # move the head
                headNode = self.snake.getHead()
                headNode.setY(headNode.getY() + 1)

                # add the new node between the trail (gettail) and snake tail.
                trail_node = self.snake.getTail()
                snake_tail = trail_node.getPrev()
                new_node = node(new_node_position[0], new_node_position[1])

                trail_node.setPrev(new_node)
                snake_tail.setNext(new_node)

                new_node.setNext(trail_node)
                new_node.setPrev(snake_tail)

            if(direction == 'left'):
                while(current_node != self.snake.getHead()):
                    # move prev node into next node's position, unless its the trail.
                    if(not current_node.isTrailing()):
                        current_node.setX(current_node.getPrev().getX())
                        current_node.setY(current_node.getPrev().getY())

                    current_node = current_node.getPrev()

                # move the head
                headNode = self.snake.getHead()
                headNode.setX(headNode.getX() - 1)

                # add the new node between the trail (gettail) and snake tail.
                trail_node = self.snake.getTail()
                snake_tail = trail_node.getPrev()
                new_node = node(new_node_position[0], new_node_position[1])

                trail_node.setPrev(new_node)
                snake_tail.setNext(new_node)

                new_node.setNext(trail_node)
                new_node.setPrev(snake_tail)

            if(direction == 'right'):
                while(current_node != self.snake.getHead()):
                    # move prev node into next node's position, unless its the trail.
                    if(not current_node.isTrailing()):
                        current_node.setX(current_node.getPrev().getX())
                        current_node.setY(current_node.getPrev().getY())

                    current_node = current_node.getPrev()

                # move the head
                headNode = self.snake.getHead()
                headNode.setX(headNode.getX() + 1)

                # add the new node between the trail (gettail) and snake tail.
                trail_node = self.snake.getTail()
                snake_tail = trail_node.getPrev()
                new_node = node(new_node_position[0], new_node_position[1])

                trail_node.setPrev(new_node)
                snake_tail.setNext(new_node)

                new_node.setNext(trail_node)
                new_node.setPrev(snake_tail)

        else:

            if(direction == 'up'):
                current_node = self.snake.getTail()

                while(current_node != self.snake.getHead()):
                    # move node into previous node's position
                    current_node.setX(current_node.getPrev().getX())
                    current_node.setY(current_node.getPrev().getY())

                    current_node = current_node.getPrev()

                # finally, move head to new position
                headNode = self.snake.getHead()
                headNode.setY(headNode.getY() - 1)

            elif(direction == 'down'):
                current_node = self.snake.getTail()

                while(current_node != self.snake.getHead()):
                    # move prev current_node into next current_node's position
                    current_node.setX(current_node.getPrev().getX())
                    current_node.setY(current_node.getPrev().getY())

                    current_node = current_node.getPrev()

                # finally, move head to new position
                headNode = self.snake.getHead()
                headNode.setY(headNode.getY() + 1)

            elif(direction == 'left'):
                current_node = self.snake.getTail()

                while(current_node != self.snake.getHead()):
                    # move prev current_node into next current_node's position
                    current_node.setX(current_node.getPrev().getX())
                    current_node.setY(current_node.getPrev().getY())

                    current_node = current_node.getPrev()

                # finally, move head to new position
                headNode = self.snake.getHead()
                headNode.setX(headNode.getX() - 1)

            elif(direction == 'right'):
                current_node = self.snake.getTail()

                while(current_node != self.snake.getHead()):
                    # move prev current_node into next current_node's position
                    current_node.setX(current_node.getPrev().getX())
                    current_node.setY(current_node.getPrev().getY())

                    current_node = current_node.getPrev()

                # finally, move head to new position
                headNode = self.snake.getHead()
                headNode.setX(headNode.getX() + 1)



if __name__ == "__main__":

    s = snake()

    s.printGrid()

    s.move('up')

    s.printGrid()

    s.move('up')

    s.printGrid()

    s.move('left')

    s.printGrid()

    s.move('left')
    
    s.printGrid()

    s.move('left')

    s.printGrid()

    s.move('left')

    s.printGrid()

    s.move('left')

    s.printGrid()

    s.move('left')

    s.printGrid()
