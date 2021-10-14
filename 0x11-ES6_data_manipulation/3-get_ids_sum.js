export default function getStudentIdsSum(listStudents) {
  const response = listStudents.reduce((acc, current) => acc + current.id, 0);
  return response;
}
