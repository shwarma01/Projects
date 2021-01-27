class Castle extends Piece {
  constructor(side, position) {
    super(
      side,
      position,
      "./images/" + ["white", "black"][side] + "/Castle.JPG"
    );
  }
}
