// CSS styling for when player clicks on a piece and the spaces that piece can move to
const clickOnPiece = "click-on-piece";
const validMoveSpace = "valid-move-space";

// Variables which will be used for logic
let turn = 1;
let end = false;
let pieceChosen = null; // Keeping track of which piece has been chosen

// Getting all board elements from DOM
const rows = document.querySelector(".board").children;
const board = [];
for (let i = 0; i < rows.length; i++) {
  board.push([]);
  for (let j = 0; j < rows[i].children.length; j++) {
    board[board.length - 1].push([rows[i].children[j], undefined]);
  }
}

// Arrow would start at the top left of its grid so this will put it to point to "white"
const changeArrowPosition = function () {
  document.querySelector(".arrow").classList.remove(["arrow-top", "arrow-bottom"][turn]);
  ++turn;
  turn %= 2;
  document.querySelector(".arrow").classList.add(["arrow-top", "arrow-bottom"][turn]);
};
changeArrowPosition();

// Function that wil get a new set of pieces in their starting positions
const newGame = () => {
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
    board[piece.getPosition()[1]][piece.getPosition()[0]][1] = piece;
    board[piece.getPosition()[1]][piece.getPosition()[0]][0].appendChild(piece.getImg());
  });
};
newGame();

// Event listener to start a new game
document.querySelector(".new-game").addEventListener("click", () => {
  pieceChosen = null;
  end = false;
  turn = 1;
  changeArrowPosition();

  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      if (board[i][j][1] !== undefined) {
        board[i][j][0].removeChild(board[i][j][1].getImg());
        board[i][j][1] = undefined;
      }
    }
  }

  newGame();
});

// Logic for dealing with the clickOnPiece styling and stopping players from clicking multiple pieces at the same time
board.forEach((row) => {
  row.forEach((colPiecePair) => {
    let col = colPiecePair[0];
    col.addEventListener("click", () => {
      if (col.children.length === 1 && pieceChosen === null) {
        if (colPiecePair[1].getSide() === turn) {
          pieceChosen = colPiecePair;
          col.classList.add(clickOnPiece);

          pieceChosen[1].getMoves(board).forEach((position) => {
            board[position[1]][position[0]][0].classList.add(validMoveSpace);
          });
        }
      } else if (pieceChosen != null) {
        if (colPiecePair[0].classList.contains(validMoveSpace)) {
          pieceChosen[1].getMoves(board).forEach((position) => {
            board[position[1]][position[0]][0].classList.remove(validMoveSpace);
          });

          if (colPiecePair[1] !== undefined) {
            colPiecePair[0].removeChild(colPiecePair[1].getImg());

            if (colPiecePair[1].constructor.name === "King") {
              end = true;
              alert("Game has ended, " + ["White", "Black"][turn] + " has won!");
            }
          }

          colPiecePair[0].appendChild(pieceChosen[1].getImg());
          pieceChosen[1].setPosition([row.indexOf(colPiecePair), board.indexOf(row)]);

          if (pieceChosen[1].constructor.name === "Pawn") {
            pieceChosen[1].setHasMove();
          }

          colPiecePair[1] = pieceChosen[1];
          pieceChosen.splice(1, 1);
          changeArrowPosition();
        } else {
          pieceChosen[1].getMoves(board).forEach((position) => {
            board[position[1]][position[0]][0].classList.remove(validMoveSpace);
          });
        }

        pieceChosen[0].classList.remove(clickOnPiece);
        pieceChosen = null;

        if (end) {
          document.querySelector(".new-game").click();
        }
      }
    });
  });
});
