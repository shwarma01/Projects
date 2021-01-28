class Pawn extends Piece {
  constructor(side, position) {
    super(side, position, "./images/" + ["white", "black"][side] + "/Pawn.JPG");
    this._hasMoved = false;
  }

  getMoves() {
    let moves = [];

    if (!this._hasMoved) {
      moves.push([
        this._position[0],
        this._position[1] - Math.pow(-1, this._side + 2) * 1,
      ]);
      moves.push([
        this._position[0],
        this._position[1] - Math.pow(-1, this._side + 2) * 2,
      ]);

      return moves;
    }

    for (let i = -1; i < 2; i++) {
      if (0 <= this._position[0] + i <= 7) {
        moves.push([
          this._position[0] + i,
          this._position[1] - Math.pow(-1, this._side + 2),
        ]);
      }
    }

    return moves;
  }

  setHasMove() {
    this._hasMoved = true;
  }
}
