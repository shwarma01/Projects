class Bishop extends Piece {
  constructor(side, position) {
    super(
      side,
      position,
      "./images/" + ["white", "black"][side] + "/Bishop.JPG"
    );
  }
}
