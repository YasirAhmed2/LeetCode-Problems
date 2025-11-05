function intToRoman(num) {
  // Define the mapping of numbers to Roman numerals
  const romanMap = [
    { value: 1000, symbol: 'M' },
    { value: 900, symbol: 'CM' },
    { value: 500, symbol: 'D' },
    { value: 400, symbol: 'CD' },
    { value: 100, symbol: 'C' },
    { value: 90, symbol: 'XC' },
    { value: 50, symbol: 'L' },
    { value: 40, symbol: 'XL' },
    { value: 10, symbol: 'X' },
    { value: 9, symbol: 'IX' },
    { value: 5, symbol: 'V' },
    { value: 4, symbol: 'IV' },
    { value: 1, symbol: 'I' }
  ];

  let result = '';

  // Loop through the mapping
  for (let i = 0; i < romanMap.length; i++) {
    // While current value can be subtracted from num
    while (num >= romanMap[i].value) {
      result += romanMap[i].symbol; // Append symbol
      num -= romanMap[i].value;     // Subtract value
    }
  }

  return result;
}

// Example:
console.log(intToRoman(3));  // Output: "MMMDCCXLIX"
