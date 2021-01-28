class Queen extends Piece {
  constructor(side, position) {
    super(
      side,
      position,
      "./images/" + ["white", "black"][side] + "/Queen.JPG"
    );
  }

  getMoves() {
    let moves = [];

    for (let i = -7; i < 8; i++) {
      if (i !== 0) {
        if (0 <= this._position[0] + i && this._position[0] + i <= 7) {
          if (0 <= this._position[1] + i && this._position[1] + i <= 7) {
            moves.push([this._position[0] + i, this._position[1] + i]);
          }

          if (0 <= this._position[1] - i && this._position[1] - i <= 7)
            moves.push([this._position[0] + i, this._position[1] - i]);
        }

        if (0 <= this._position[0] + i && this._position[0] + i <= 7) {
          moves.push([this._position[0] + i, this._position[1]]);
        }

        if (0 <= this._position[1] + i && this._position[1] + i <= 7) {
          moves.push([this._position[0], this._position[1] + i]);
        }
      }
    }

    return moves;
  }
}
