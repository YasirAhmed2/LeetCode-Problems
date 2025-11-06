function groupAnagrams(strs) {
  const map = new Map();

  for (let str of strs) {
    // Sort each string alphabetically to use as a key
    const key = str.split('').sort().join('');
    // If key not in map, initialize with empty array
    if (!map.has(key)) {
      map.set(key, []);
    }
    // Push current string to the corresponding group
    map.get(key).push(str);
  }

  // Return all groups as an array
  return Array.from(map.values());
}

// Example usage
const strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
console.log(groupAnagrams(strs));
