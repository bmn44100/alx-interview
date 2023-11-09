#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/${id}';

request(url, async function (error, response, body) {
    if (error) {
        console.log(error);
    }

    const characters = JSON.parse(body).characters;

    for (const character of characters) {
        await new Promise(function (resolve, reject) {
            request(character, function (error, response, body) {
                if (error) {
                    console.log(error);
                }
                console.log(JSON.parse(body).name);
                resolve();
            });
        });
    }
});