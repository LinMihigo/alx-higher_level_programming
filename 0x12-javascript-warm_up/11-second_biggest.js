#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
console.log(args.length < 2 ? 0 : args.sort((a, b) => b - a)[1]);
