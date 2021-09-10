export default function createIteratorObject(report) {
  let newArray = [];
  for (const idx of Object.values(report.allEmployees)) {
    newArray = [...newArray, ...idx];
  }

  return newArray;
}
