#!/usr/bin/node

//  A class Rectangle that defines a rectangle
//  The constructor takes 2 arguments w and h
//  Initializing the instance attribute width with the value of w
//  Initializing the instance attribute height with the value of h

module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};
