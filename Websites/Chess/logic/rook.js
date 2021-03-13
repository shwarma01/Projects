class Rook extends Piece {
  constructor(side, position) {
    super(side, position, "./images/" + ["white", "black"][side] + "/Rook.JPG");
  }

  getMoves(board) {
    let moves = [];

    for (let i = -2; i <= 2; i += 4) {
      for (let j = -1; j <= 1; j += 2) {
        if (0 <= this._position[0] + i && this._position[0] + i <= 7) {
          if (0 <= this._position[1] + j && this._position[1] + j <= 7) {
            moves.push([this._position[0] + i, this._position[1] + j]);
          }
        }

        if (0 <= this._position[1] + i && this._position[1] + i <= 7) {
          if (0 <= this._position[0] + j && this._position[0] + j <= 7) {
            moves.push([this._position[0] + j, this._position[1] + i]);
          }
        }
      }
    }

    for (let i = moves.length - 1; i >= 0; i--) {
      if (board[moves[i][1]][moves[i][0]][1] !== undefined) {
        if (board[moves[i][1]][moves[i][0]][1].getSide() === this._side) {
          moves.splice(i, 1);
        }
      }
    }

    return moves;
  }
}
