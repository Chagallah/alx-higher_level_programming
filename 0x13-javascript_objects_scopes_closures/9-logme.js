#!/usr/bin/node
let argumentnumber = 0;
exports.logMe = fuunction (item) {
    console.log(argumentnumber + ': ' + item);
    argumentnumber++;
};
