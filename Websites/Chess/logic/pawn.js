class Pawn extends Piece {
  constructor(side, position) {
    super(side, position, "./images/" + ["white", "black"][side] + "/Pawn.JPG");
    this._hasMoved = false;
  }

  getMoves(board) {
    let moves = [];

    if (!this._hasMoved) {
      if (board[this._position[1] - Math.pow(-1, this._side + 2)][this._position[0]][1] === undefined) {
        moves.push([this._position[0], this._position[1] - Math.pow(-1, this._side + 2) * 1]);
      }

      if (board[this._position[1] - Math.pow(-1, this._side + 2) * 2][this._position[0]][1] === undefined) {
        moves.push([this._position[0], this._position[1] - Math.pow(-1, this._side + 2) * 2]);
      }

      return moves;
    }

    if (0 <= this._position[1] - Math.pow(-1, this._side + 2) && this._position[1] - Math.pow(-1, this._side + 2) <= 7) {
      if (board[this._position[1] - Math.pow(-1, this._side + 2)][this._position[0]][1] === undefined) {
        moves.push([this._position[0], this._position[1] - Math.pow(-1, this._side + 2)]);
      }
    }

    for (let i = -1; i < 2; i += 2) {
      if (0 <= this._position[0] + i && this._position[0] + i <= 7) {
        if (board[this._position[1] - Math.pow(-1, this._side + 2)][this._position[0] + i][1] !== undefined) {
          if (board[this._position[1] - Math.pow(-1, this._side + 2)][this._position[0] + i][1].getSide() !== this._side) {
            moves.push([this._position[0] + i, this._position[1] - Math.pow(-1, this._side + 2)]);
          }
        }
      }
    }

    return moves;
  }

  setHasMove() {
    this._hasMoved = true;
  }
}
