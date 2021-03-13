class Piece {
  constructor(side, position, dir) {
    this._side = side;
    this._position = position;
    this._img = document.createElement("img");
    this._img.src = dir;
  }

  getSide() {
    return this._side;
  }

  getPosition() {
    return this._position;
  }

  getImg() {
    return this._img;
  }

  setPosition(position) {
    this._position = position;
  }
}
