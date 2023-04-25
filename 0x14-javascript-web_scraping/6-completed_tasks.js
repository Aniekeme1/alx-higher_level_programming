#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const arguments = process.argv;
let url = arguments[2];
let request = require('request');
request(url, function (error, response, body) {
	if (error) {
	console.log('error:', error);
	} else {
		let todos = JSON.parse(body);
		let dashboard = {};
		for (let i = 0; i < todos.length; i++) {
			let isCompleted = (todos[i]['completed']);
			let userId = todos[i]['userId'].toString();
			if (isCompleted) {
				if (dashboard[userId]) {
				dashboard[userId]++;
				} else {
					dashboard[userId] = 1;
				}
			}
		}
	
	console.log(dashboard);
	}
});
