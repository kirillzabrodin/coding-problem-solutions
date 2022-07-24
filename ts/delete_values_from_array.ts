function removeElement(nums: number[], val: number): number {
    let length = nums.length
    for (let i = 0; i < length; i++) {
        if (nums[length - i - 1] == val) {
            nums.splice(length - i - 1, 1)
        }
    }
    // nums.forEachRight(function(part, index) {
    //     console.log(part);
    //     console.log(index);
    //     if (part == val) {
    //         nums.splice(index, 1);
    //     }
    // })
    console.log(nums);
    return nums.length;
};

console.log(removeElement([3, 2, 2, 3, 3], 3))