#!/usr/bin/node
// A script that prints all characters of a Star Wars movie
// Display characters name in the same order of the list  characters in the film response

const request = require('request');
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function printCharacters (characters, idx) {
  request(characters[idx], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        printCharacters(characters, idx + 1);
      }
    }
  });
}

request(filmUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const chars = JSON.parse(body).characters;
    printCharacters(chars, 0);
  }
});
