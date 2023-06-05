/*
Matrix Equallity

Write a function that takes two input matrices 
and returns true if they are equal false otherwise.
*/
function areMatricesEqual(m1, m2) {

}


// Test Case 1
const matrix1 = [
    [1, 2],
    [3, 4]
  ];
  const matrix2 = [
    [1, 2],
    [3, 4]
  ];
  console.log(
    `Test Case 1: ${areMatricesEqual(matrix1, matrix2)}. Expected output: true`
  );
  
  // Test Case 2
  const matrix3 = [
    [1, 2],
    [3, 4]
  ];
  const matrix4 = [
    [1, 2],
    [5, 6]
  ];
  console.log(
    `Test Case 2: ${areMatricesEqual(matrix3, matrix4)}. Expected output: false`
  );
  
  // Test Case 3
  const matrix5 = [
    [1, 2],
    [3, 4]
  ];
  const matrix6 = [
    [1, 2, 3],
    [3, 4, 5]
  ];
  console.log(
    `Test Case 3: ${areMatricesEqual(matrix5, matrix6)}. Expected output: false`
  );
  
  // Test Case 4
  const matrix7 = [
    [1, 2],
    [3, 4],
    [5, 6]
  ];
  const matrix8 = [
    [1, 2],
    [3, 4],
    [5, 6]
  ];
  console.log(
    `Test Case 4: ${areMatricesEqual(matrix7, matrix8)}. Expected output: true`
  );
  
  // Test Case 5
  const matrix9 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ];
  const matrix10 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
  ];
  console.log(
    `Test Case 5: ${areMatricesEqual(matrix9, matrix10)}. Expected output: false`
  );
  