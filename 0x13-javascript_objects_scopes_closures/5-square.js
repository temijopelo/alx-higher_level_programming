#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extend Rectangle {
  constructor (size) {
  super(size, size);
  }
}
module.exports = Square;
