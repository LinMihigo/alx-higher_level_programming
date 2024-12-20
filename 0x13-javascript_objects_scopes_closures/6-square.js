const Square = require('./5-square');

class SquareWithCharPrint extends Square {
  charPrint (c = 'X') {
    console.log(c.repeat(this.width).concat('\n').repeat(this.height).trim());
  }
}
module.exports = SquareWithCharPrint;
