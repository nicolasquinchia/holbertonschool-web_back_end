export default function getListStudentIds(arrayStudents) {
  let mappedArray;
  if (Array.isArray(arrayStudents)) {
    mappedArray = arrayStudents.map((index) => index.id);
    return mappedArray;
  }
  return [];
}
