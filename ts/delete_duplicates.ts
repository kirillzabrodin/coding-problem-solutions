function removeDuplicates(nums: number[]): number {
    let previous: any = undefined
    for (let index = 0; index < nums.length; index++) {
        if (nums[index] == previous) {
            nums.splice(index, 1)
            index--
        }
        previous = nums[index]
    }
    return nums.length
};

console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))