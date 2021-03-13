class Castle extends Piece {
  constructor(side, position) {
    super(side, position, "./images/" + ["white", "black"][side] + "/Castle.JPG");
  }

  getMoves(board) {
    let moves = [];

    for (let j = 0; j < 2; j++) {
      for (let k = -1; k < 2; k += 2) {
        for (let i = -1; i >= -7; i--) {
          if (j == 0) {
            if (!(0 <= this._position[0] + k * i && this._position[0] + k * i <= 7)) {
              break;
            }

            let element = board[this._position[1]][this._position[0] + k * i][1];

            if (element !== undefined) {
              if (element.getSide() !== this._side) {
                moves.push([this._position[0] + k * i, this._position[1]]);
              }

              break;
            } else {
              moves.push([this._position[0] + k * i, this._position[1]]);
            }
          } else {
            if (!(0 <= this._position[1] + k * i && this._position[1] + k * i <= 7)) {
              break;
            }

            let element = board[this._position[1] + k * i][this._position[0]][1];

            if (element !== undefined) {
              if (element.getSide() !== this._side) {
                moves.push([this._position[0], this._position[1] + k * i]);
              }

              break;
            } else {
              moves.push([this._position[0], this._position[1] + k * i]);
            }
          }
        }
      }
    }

    return moves;
  }
}
