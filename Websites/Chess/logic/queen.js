class Queen extends Piece {
  constructor(side, position) {
    super(
      side,
      position,
      "./images/" + ["white", "black"][side] + "/Queen.JPG"
    );
  }
}
