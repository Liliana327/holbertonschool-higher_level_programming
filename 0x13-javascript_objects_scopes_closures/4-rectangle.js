#!/usr/bin/node

// a class Rectangle that defines a rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let cont = 0; cont < this.height; cont++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let a = this.width;
    this.width = this.height;
    this.height = a;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
