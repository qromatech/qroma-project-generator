import { createInterface } from "readline";

console.log('Hello world2!')

const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Please enter a project ID: ", (projectId: string) => {
  console.log(`You entered projectId: ${projectId}`);
  rl.close();
});
