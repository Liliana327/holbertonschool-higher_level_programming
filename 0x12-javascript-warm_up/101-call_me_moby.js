#!/usr/bin/node

exports.callMeMoby = (a, Function) => {
   let cont;
  for (cont = 0; cont < a; cont++) {
    Function();
  }
};
