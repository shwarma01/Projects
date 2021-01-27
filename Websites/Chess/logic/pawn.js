class Pawn extends Piece {
  constructor(side, position) {
    super(side, position, "./images/" + ["white", "black"][side] + "/Pawn.JPG");
  }
}
