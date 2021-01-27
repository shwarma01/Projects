class King extends Piece {
  constructor(side, position) {
    super(side, position, "./images/" + ["white", "black"][side] + "/King.JPG");
  }
}
