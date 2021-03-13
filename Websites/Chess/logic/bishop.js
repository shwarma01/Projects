class Bishop extends Piece {
  constructor(side, position) {
    super(side, position, "./images/" + ["white", "black"][side] + "/Bishop.JPG");
  }

  getMoves(board) {
    let moves = [];

    for (let j = -1; j < 2; j += 2) {
      for (let k = -1; k < 2; k += 2) {
        for (let i = -1; i >= -7; i--) {
          if (0 <= this._position[0] + k * i && this._position[0] + k * i <= 7) {
            if (0 <= this._position[1] + j * k * i && this._position[1] + j * k * i <= 7) {
              let element = board[this._position[1] + j * k * i][this._position[0] + k * i][1];

              if (element !== undefined) {
                if (element.getSide() !== this._side) {
                  moves.push([this._position[0] + k * i, this._position[1] + j * k * i]);
                }

                break;
              } else {
                moves.push([this._position[0] + k * i, this._position[1] + j * k * i]);
              }
            } else {
              break;
            }
          } else {
            break;
          }
        }
      }
    }

    return moves;
  }
}
