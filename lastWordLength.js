function lengthOfLastWord(s) {

  s = s.trim();

  const words = s.split(" ");
  // Return length of last word
  return words[words.length - 1].length;
}
console.log(lengthOfLastWord("Hello World")); // 5
console.log(lengthOfLastWord("   fly me   to   the moon  ")); // 4
console.log(lengthOfLastWord("luffy is still joyboy")); // 6
