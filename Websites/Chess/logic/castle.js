class Castle extends Piece {
  constructor(side, position) {
    super(side, position, "./images/" + ["white", "black"][side] + "/Castle.JPG");
  }

  getMoves(board) {
    let moves = [];
    let spliceOffset = 0;

    for (let j = 0; j < 2; j++) {
      spliceOffset = moves.length;
      for (let i = -7; i <= 7; i++) {
        if (i !== 0) {
          if (j === 0) {
            if (0 <= this._position[0] + i && this._position[0] + i <= 7) {
              moves.push([this._position[0] + i, this._position[1]]);

              if (board[this._position[1]][this._position[0] + i][1] !== undefined) {
                if (board[this._position[1]][this._position[0] + i][1].getSide() !== this._side) {
                  moves.splice(spliceOffset, moves.length - spliceOffset - 1);
                } else {
                  moves.splice(spliceOffset, moves.length - spliceOffset);
                }

                if (i > 0) {
                  break;
                }
              }
            }
          } else {
            if (0 <= this._position[1] + i && this._position[1] + i <= 7) {
              moves.push([this._position[0], this._position[1] + i]);

              if (board[this._position[1] + i][this._position[0]][1] !== undefined) {
                if (board[this._position[1] + i][this._position[0]][1].getSide() !== this._side) {
                  moves.splice(spliceOffset, moves.length - spliceOffset - 1);
                } else {
                  moves.splice(spliceOffset, moves.length - spliceOffset);
                }

                if (i > 0) {
                  break;
                }
              }
            }
          }
        }
      }
    }

    return moves;
  }
}
