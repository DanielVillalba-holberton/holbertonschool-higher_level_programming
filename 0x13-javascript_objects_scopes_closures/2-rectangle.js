#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w = null, h = null) {
    if (h < 1 || w < 1) {
      return null;
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
