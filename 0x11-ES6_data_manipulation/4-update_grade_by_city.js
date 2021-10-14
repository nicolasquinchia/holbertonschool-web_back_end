export default function updateStudentGradeByCity(listStudents, city, newGrades) {
  const filter = listStudents.filter((index) => index.location === city);
  const response = filter.map((student) => {
    for (let index = 0; index < newGrades.length; index += 1) {
      if (student.id === newGrades[index].studentId) {
        student.grade = newGrades[index].grade;
      }
    }
    if (!student.grade) {
      student.grade = 'N/A';
    }
    return student;
  });
  return response;
}
