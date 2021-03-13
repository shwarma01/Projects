class Queen extends Piece {
  constructor(side, position) {
    super(side, position, "./images/" + ["white", "black"][side] + "/Queen.JPG");
  }

  getMoves(board) {
    const castle = new Castle(this._side, this._position);
    const bishop = new Bishop(this._side, this._position);

    return [...bishop.getMoves(board), ...castle.getMoves(board)];
  }
}
