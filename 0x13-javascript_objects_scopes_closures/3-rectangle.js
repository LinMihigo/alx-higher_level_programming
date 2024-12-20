class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log('X'.repeat(this.width).concat('\n').repeat(this.height).trim());
  }
}
module.exports = Rectangle;
