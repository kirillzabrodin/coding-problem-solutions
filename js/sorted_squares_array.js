const sortedSquares = function(nums) {
    return nums.map(x => x * x).sort(function(x, y) {return x - y})
};

console.log(sortedSquares([-4,-1,0,3,10]))