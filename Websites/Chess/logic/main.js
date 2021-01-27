// Event listener to start a new game
document.querySelector(".new-game").addEventListener("click", () => {
  board.forEach((row) => {
    row.forEach((col) => {
      if (col.children.length === 1) {
        col.removeChild(col.children[0]);
      }

      if (col.classList.length != 1) {
        col.classList.remove(clickOnPiece);
        col.classList.remove(validMoveSpace);
        pieceChosen = false;
      }
    });
  });

  pieces = newGame();
});

// List to figure out whose turn it is
const players = ["white", "black"];

// CSS styling for when player clicks on a piece and the spaces that piece can move to
const clickOnPiece = "click-on-piece";
const validMoveSpace = "valid-move-space";

// Variables which will be used for logic
let turn = 0;
let pieceChosen = false; // Making sure that user cannot more than one piece at a time
// Getting all board elements from DOM
const board = [];
const rows = document.querySelector(".board").children;
for (let i = 0; i < rows.length; i++) {
  board.push([]);
  for (let j = 0; j < rows[i].children.length; j++) {
    board[i].push(rows[i].children[j]);
  }
}

// Arrow would start at the top left of its grid so this will put it to point to "white"
const changeArrowPosition = function (turn) {
  document
    .querySelector(".arrow")
    .classList.add(["arrow-top", "arrow-bottom"][turn]);
};
changeArrowPosition(turn);

// Function that wil get a new set of pieces in their starting positions
const newGame = function () {
  let pieces = [];

  for (let i = 0; i < 8; i += 7) {
    pieces.push(new Castle(0, [i - 0, 7]));
    pieces.push(new Castle(1, [i - 0, 0]));

    pieces.push(new Bishop(0, [Math.abs(i - 1), 7]));
    pieces.push(new Bishop(1, [Math.abs(i - 1), 0]));

    pieces.push(new Rook(0, [Math.abs(i - 2), 7]));
    pieces.push(new Rook(1, [Math.abs(i - 2), 0]));
  }

  pieces.push(new King(0, [3, 7]));
  pieces.push(new King(1, [3, 0]));

  pieces.push(new Queen(0, [4, 7]));
  pieces.push(new Queen(1, [4, 0]));

  for (let i = 0; i < 8; i++) {
    pieces.push(new Pawn(0, [i, 6]));
    pieces.push(new Pawn(1, [i, 1]));
  }

  pieces.forEach((piece) => {
    board[piece.getPosition()[1]][piece.getPosition()[0]].appendChild(
      piece.getImg()
    );
  });

  return pieces;
};

// Variable to hold all the pieces
let pieces = newGame();

board.forEach((row) => {
  row.forEach((col) => {
    if (col.children.length === 1) {
      col.addEventListener("click", () => {
        if (col.classList.length != 1) {
          col.classList.remove(clickOnPiece);
          pieceChosen = false;
        } else if (!pieceChosen) {
          col.classList.add(clickOnPiece);
          pieceChosen = true;
        }
      });
    }
  });
});
