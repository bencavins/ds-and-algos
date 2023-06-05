/*
Sum of all elements

Write a function that calculates and returns 
the sum of all elements in a given 2D array.
*/
function sumOfElements(m) {
    let total = 0
    for (let i = 0; i < m.length; i++) {
        // const row = m[i]
        for (let j = 0; j < m[i].length; j++) {
            total += m[i][j]
        }
    }
    return total
}


// Test Case 1
const arr1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
console.log('Expected output: 45')
console.log(sumOfElements(arr1)); // Expected output: 45
console.log('-------------------')

// Test Case 2
const arr2 = [
  [10, 20],
  [30, 40],
  [50, 60]
];
console.log('Expected output: 210')
console.log(sumOfElements(arr2)); // Expected output: 210
console.log('-------------------')

// Test Case 3
const arr3 = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
];
console.log('Expected output: 0')
console.log(sumOfElements(arr3)); // Expected output: 0
console.log('-------------------')

// Test Case 4
const arr4 = [
  [-1, -2, -3],
  [-4, -5, -6],
  [-7, -8, -9]
];
console.log('Expected output: -45')
console.log(sumOfElements(arr4)); // Expected output: -45
console.log('-------------------')

// Test Case 5
const arr5 = [
  [1, 2],
  [3, 4],
  [5, 6],
  [7, 8]
];
console.log('Expected output: 36')
console.log(sumOfElements(arr5)); // Expected output: 36
console.log('-------------------')
