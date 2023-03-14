#!/usr/bin/node

const arg = process.argv[2];

if (/^\d+$/.test(arg)) {
  const size = parseInt(arg);

  for (let i = 0; i < size; i++) {
    let line = '';

    for (let j = 0; j < size; j++) {
      line += 'X';
    }

    console.log(line);
  }
} else {
  console.log('Missing size');
}
