class Cell {
  constructor(column, row) {
    this.column = column;
    this.row = row;
    this.walls = [true, true, true, true]; //top right bottom left
    this.visted = false;
    this.highlight = function () {
      var x = this.column * maze_size;
      var y = this.row * maze_size;
      noStroke();
      fill(0, 0, 255, 100);
      rect(x, y, maze_size, maze_size);
    };
    this.checkNeighbors = function () {
      var neighbors = [];
      var top = grid[index(column, row - 1)];
      var right = grid[index(column + 1, row)];
      var bottom = grid[index(column, row + 1)];
      var left = grid[index(column - 1, row)];
      if (top && !top.visted) {
        neighbors.push(top);
      }
      if (right && !right.visted) {
        neighbors.push(right);
      }
      if (bottom && !bottom.visted) {
        neighbors.push(bottom);
      }
      if (left && !left.visted) {
        neighbors.push(left);
      }
      if (neighbors.length > 0) {
        var random_neighbor = floor(random(0, neighbors.length));
        return neighbors[random_neighbor];
      } else {
        return undefined;
      }
    };
    this.show = function () {
      var x = this.column * maze_size;
      var y = this.row * maze_size;
      stroke(255);
      if (this.walls[0]) {
        line(x, y, x + maze_size, y);
      }
      if (this.walls[1]) {
        line(x + maze_size, y, x + maze_size, y + maze_size);
      }
      if (this.walls[2]) {
        line(x + maze_size, y + maze_size, x, y + maze_size);
      }
      if (this.walls[3]) {
        line(x, y + maze_size, x, y);
      }
      if (this.visted) {
        noStroke();
        fill(255, 0, 255, 100);
        rect(x, y, maze_size, maze_size);
      }
    };
  }
}
