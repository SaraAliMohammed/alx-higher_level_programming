#!/usr/bin/node

const size = Number(process.argv[2]);
if (isNaN(Number(size)) || size === undefined) {
  console.log('Missing size');
}
let x = 'X';
for (let i = 0; i < size; i++) {
  x = '';
  for (let j = 0; j < size; j++) {
    x += 'X';
  }
  console.log(x);
}
