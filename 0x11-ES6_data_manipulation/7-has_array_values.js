export default function hasValuesFromArray(set, array) {
  const inSet = (value) => set.has(value);
  return array.every(inSet);
}
