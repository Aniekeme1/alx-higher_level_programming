#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi.dev/api/films/${filmId}/`;
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;
    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  } else {
    console.log('Error:', error);
  }
});

