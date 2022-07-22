const duplicateZeros = function(arr) {
    let initial_length = arr.length
    for (let index = 0; index < initial_length; index++) {
        if (arr[index] === 0) {
            arr.splice(index, 0, 0)
            index++
            arr.pop()
        }
    }
    return arr
};

console.log(duplicateZeros([1,0,2,3,0,4,5,0]))