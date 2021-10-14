export default function getStudentsByLocation(listStudents, city) {
  const response = listStudents.filter((index) => index.location === city);
  return response;
}
