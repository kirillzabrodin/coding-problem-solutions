function merge(nums1: number[], m: number, nums2: number[], n: number): number[] {
    let first_arr: number[] = nums1.slice(0, m)
    let second_arr: number[] = nums2.slice(0, n)
    let final_arr: number[] = []
    let index_one: number = 0
    let index_two: number = 0
    while (final_arr.length != (m + n)) {
        if (first_arr[index_one] >= second_arr[index_two] || first_arr[index_one] == undefined) {
            final_arr.push(second_arr[index_two])
            index_two += 1
        } else {
            final_arr.push(first_arr[index_one])
            index_one += 1
        }
    }
    return final_arr
};

console.log(merge([1,2,3,7,0,0], 4, [2,5,6], 3))