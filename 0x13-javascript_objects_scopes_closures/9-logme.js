#!/usr/bin/node
let arsg_count = 0;
exports.logMe = function (item) {
  console.log(`${arsg_count}: ${item}`);
  arsg_count++;
};
