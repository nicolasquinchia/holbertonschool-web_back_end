export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  for (const newItem of map) {
    if (newItem[1] === 1) {
      map.set(newItem[0], 100);
    }
  }
  return map;
}
