#!/usr/bin/node

const number = Number(process.argv[2]);
if (!number) {
  console.log('Missing number of occurrences');
} else if (number) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
