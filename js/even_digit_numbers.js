const findNumbers = function(nums) {
    let count = 0
    for (let i in nums) {
        if (nums[i].toString().length % 2 == 0) {
            count += 1
        }
    }
    return count
};

console.log(findNumbers([12,345,2,6,7896]))