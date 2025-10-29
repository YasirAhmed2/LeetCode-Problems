function rotate(nums, k) {
  k = k % nums.length; // Handle cases where k > nums.length
  const removed = nums.splice(nums.length - k); // Remove last k elements
  nums.unshift(...removed); // Add them at the start
  return nums;
}

// Example usage:
let nums = [1, 2, 3, 4, 5, 6, 7];
let k = 3;
console.log(rotate(nums, k)); // Output: [5, 6, 7, 1, 2, 3, 4]
