process.stdin.setEncoding('utf8');
process.stdin.resume();

console.log('Welcome to Holberton School, what is your name?');
process.stdin.on('readable', () => {
  const nameValue = process.stdin.read();
  if (nameValue !== null) {
    process.stdout.write(`Your name is: ${nameValue}`);
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
