export default function updateStudentGradeByCity(studentArr, city, newGrades) {
  const desiredStudents = studentArr.filter((student) => student.location === city);
  const toChangeStudent = desiredStudents.map((student) => {
    for (const studInfo of newGrades) {
      if (student.id === studInfo.studentId) {
        student.grade = studInfo.grade;
      }
    }
    if (student.grade == unidentified) {
      student.grade = 'N/A'
    }
    return student;
  });
  return toChangeStudent;
}
