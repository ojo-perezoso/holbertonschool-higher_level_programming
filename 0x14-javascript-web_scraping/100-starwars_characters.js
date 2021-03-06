#!/usr/bin/node
/* List all the characters from a starwars movie based on the id with axios */
const axios = require('axios').default;
const process = require('process');

if (process.argv.length >= 3) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

  axios.get(url)
    .then((response) => {
    // handle success
      const characters = response.data.characters;
      characters.forEach((charUrl) => {
        axios.get(charUrl)
          .then((charResponse) => {
            console.log(charResponse.data.name);
          })
          .catch((error) => {
            console.log(error);
          });
      });
    })
    .catch((error) => {
    // handle error
      console.log(error);
    });
}
