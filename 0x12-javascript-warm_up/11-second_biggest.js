#!/usr/bin/node
const args = [];
if (process.argv.length < 4) {
  console.log(0);
}
for (let i = 2; i < process.argv.length; i++) {
  const arg = parseInt(process.argv[i]);
  args.push(arg);
}
const sorted = args.sort((a, b) => a - b);
if (sorted[sorted.length - 2]) {
  console.log(sorted[sorted.length - 2]);
}
