const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    let students = fs.readFileSync(path).toString().split('\n');
    students = students.slice(1, students.length - 1);
    console.log(`Number of students: ${students.length}`);

    const studentData = {};
    for (const index of students) {
      const student = index.split(',');
      if (!studentData[student[3]]) {
        studentData[student[3]] = [];
      }
      studentData[student[3]].push(student[0]);
    }
    for (const value in studentData) {
      if (value) {
        console.log(`Number of students in ${value}: ${studentData[value].length}. List: ${studentData[value].join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};
