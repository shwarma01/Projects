const arrowClassList = document.querySelector(".arrow").classList;
arrowClassList.add("arrow-top");
const arrowClassLists = ["arrow-top", "arrow-bot"];

const players = ["X", "O"];
let player = 0;

let end = false;

document.querySelectorAll(".box").forEach((box) => {
  box.addEventListener("click", () => {
    if (end) {
      checkEnd();
    } else if (box.childNodes.length === 0) {
      const createElement = document.createElement("h1");
      createElement.innerHTML = players[player % 2];
      arrowClassList.remove(arrowClassLists[player % 2]);
      arrowClassList.add(arrowClassLists[(player + 1) % 2]);
      player++;
      box.appendChild(createElement);
      checkEnd();
    }
  });
});

document.querySelector(".new-game").addEventListener("click", () => {
  arrowClassList.remove(arrowClassLists[player % 2]);
  arrowClassList.add(arrowClassLists[0]);
  player = 0;
  end = false;
  document.querySelectorAll(".box").forEach((box) => {
    if (box.childNodes.length != 0) {
      box.removeChild(box.childNodes[0]);
    }
  });
});

function checkEnd() {
  const board = [];

  document.querySelectorAll(".box").forEach((box) => {
    if (box.childNodes.length != 0) {
      board.push(box.childNodes[0].innerHTML);
    } else {
      board.push(-1);
    }
  });

  players.forEach((player) => {
    for (var i = 0; i < 3; i++) {
      if (
        board[i] === player &&
        board[i + 3] == player &&
        board[i + 6] === player
      ) {
        alert("Player " + player + " wins!");
        end = true;
      }
    }

    for (var i = 0; i < 9; i += 3) {
      if (
        board[i] === player &&
        board[i + 1] === player &&
        board[i + 2] === player
      ) {
        alert("Player " + player + " wins!");
        end = true;
      }
    }

    if (
      (board[0] === player && board[4] === player && board[8] === player) ||
      (board[6] === player && board[4] === player && board[2] === player)
    ) {
      alert("Player " + player + " wins!");
      end = true;
    }
  });
}
