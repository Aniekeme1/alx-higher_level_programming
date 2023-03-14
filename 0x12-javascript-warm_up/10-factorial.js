#!/usr/bin/node

function Factorial (number) {
  const holder = Number(number);
  if (!holder) {
    return (1);
  } else if (holder === 1) {
    return (1);
  } else {
    return (Factorial(holder - 1) * holder);
  }
}

console.log(Factorial(process.argv[2]));
