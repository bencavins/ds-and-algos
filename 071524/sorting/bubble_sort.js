// Time Complexity: O(n^2)
// Space Complexity: O(1)

function bubbleSort(array) {
    while (true) {
        let swap = false  // flag to determine if a swap was performed
        for (let i = 0; i < array.length - 1; i++) {
            console.log(i, array[i], array[i+1])
    
            // check if pair is out of order
            if (array[i] > array[i+1]) {
                // swap pair
                const tmp = array[i+1]
                array[i+1] = array[i]
                array[i] = tmp
                swap = true
            }
        }
        console.log(array)
        
        // check if a swap was performed
        if (!swap) {
            // break out of while loop
            break
        }
    }
}

bubbleSort([2, 5, 3, 4, 1, 6,3,5,3,8,3])