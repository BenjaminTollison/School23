var columns,rows;
var maze_size = 40;
var grid = [];
var current_cell;
var stack = [];


function setup() {
  createCanvas(800, 800);
  columns = floor(width/maze_size);
  rows = floor(width/maze_size);
  //frameRate(5);
  for(var row = 0; row<rows;row++){
    for (var column=0;column<columns;column++){
      var cell = new Cell(row,column);
      grid.push(cell);
    }
  }
  current_cell = grid[0];
  goal = [roundcellsize(random(0,rows*maze_size)),roundcellsize(random(0,columns*maze_size))];
  console.log(goal);
}
function roundcellsize(a){
  return Math.floor(a/maze_size)*maze_size;
}
function index(i,j){
  if(i<0||j<0||i>columns-1||j>rows-1){
    return -1;
  }
  return j+i*columns
}
function removeWalls(a,b){
  var x = a.column - b.column
  if (x==1){
    a.walls[3] = false;
    b.walls[1] = false;
  }else if (x == -1){
    a.walls[1] = false;
    b.walls[3] = false;
  }
  var y = a.row - b.row
  if (y==1){
    a.walls[0] = false;
    b.walls[2] = false;
  }else if (y == -1){
    a.walls[2] = false;
    b.walls[0] = false;
  }
}
function draw() {
  background(51);
  for(i=0;i<grid.length;i++){
    grid[i].show()
  }
  current_cell.visted = true;
  current_cell.highlight();
  if(x=goal[0],y=goal[1]){
    noStroke();
    fill(255,255,0,80);
    rect(x, y, maze_size, maze_size);
  }
  // step 1
  var next_cell = current_cell.checkNeighbors();
  if(next_cell){
    next_cell.visted = true;
  //step 2
    stack.push(current_cell);
  // step 3
    removeWalls(current_cell,next_cell);
  // step 4
    current_cell = next_cell;
  }else if(stack.length>0){
    current_cell = stack.pop();
  }
}
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
