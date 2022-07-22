let findMaxConsecutiveOnes = function(nums) {
    let maximum = 0
    let current = 0
    for (let variable of nums) {
        if (variable == 1) {
            current += 1
        } else {
            if (current > maximum) {
                maximum = current
            }
            current = 0
        }
    }
    return Math.max(maximum, current)
};

console.log(findMaxConsecutiveOnes([1,1,0,1,1,1]))