#!/usr/bin/node

//  A class Rectangle that defines a rectangle
//  The constructor takes 2 arguments w and h
//  Initializing the instance attribute width with the value of w
//  Initializing the instance attribute height with the value of h
//  Creating an empty object if  w or h is equal to 0 or not a positive integer

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
