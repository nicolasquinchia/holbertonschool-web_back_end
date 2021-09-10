export default function iterateThroughObject(reportWithIterator) {
  let newEmployee = '';
  for (const name of reportWithIterator) {
    newEmployee += `${name} | `;
  }
  return newEmployee.slice(0, -3);
}
