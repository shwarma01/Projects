class King extends Piece {
  constructor(side, position) {
    super(side, position, "./images/" + ["white", "black"][side] + "/King.JPG");
  }

  getMoves() {
    let moves = [];

    for (let i = -1; i < 2; i += 2) {
      if (0 <= this._position[0] + i && this._position[0] + i <= 7) {
        moves.push([this._position[0] + i, this._position[1]]);

        if (0 <= this._position[1] + i && this._position[1] + i <= 7) {
          moves.push([this._position[0] + i, this._position[1] + i]);
        }

        if (0 <= this._position[1] - i && this._position[1] - i <= 7) {
          moves.push([this._position[0] + i, this._position[1] - i]);
        }
      }

      if (0 <= this._position[1] + i && this._position[1] + i <= 7) {
        moves.push([this._position[0], this._position[1] + i]);
      }
    }

    return moves;
  }
}
