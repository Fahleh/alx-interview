#!/usr/bin/node
const request = require("request");
const BASE_URL = "https://swapi-api.hbtn.io/api";
const ARGS = process.argv;

if (ARGS.length > 2) {
  request(`${BASE_URL}/films/${ARGS[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const characterList = JSON.parse(body).characters;
    const characters = characterList.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (err, __, response) => {
            if (err) {
              reject(err);
            }
            resolve(JSON.parse(response).name);
          });
        })
    );

    Promise.all(characters)
      .then((character) => console.log(character.join("\n")))
      .catch((allErr) => console.log(allErr));
  });
}
