class Movements:
    def __init__(self, node_copy, current_node_array, blank_space):
        self.current_node_array = current_node_array
        self.node = node_copy
        self.blank_space = blank_space

    def move(self, direction):
        if direction == "up":
            self.up()
        if direction == "down":
            self.down()
        if direction == "right":
            self.right()
        if direction == "left":
            self.left()

    # movements
    def right(self):
        self.node[self.blank_space - 1], self.node[self.blank_space] = self.current_node_array[self.blank_space], self.node[
            self.blank_space - 1]
        return "successfully moved"

    def left(self):
        self.node[self.blank_space + 1], self.node[self.blank_space] = self.current_node_array[
            self.blank_space], self.node[
            self.blank_space + 1]
        return "successfully moved"

    def up(self):
        self.node[self.blank_space - 3], self.node[self.blank_space] = self.current_node_array[
            self.blank_space], self.node[
            self.blank_space - 3]
        return "successfully moved"

    def down(self):
        self.node[self.blank_space + 3], self.node[self.blank_space] = self.current_node_array[
            self.blank_space], self.node[
            self.blank_space + 3]
        return "successfully moved"

