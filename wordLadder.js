function ladderLength(beginWord, endWord, wordList) {
    const wordSet = new Set(wordList);
    if (!wordSet.has(endWord)) return 0; // endWord must exist in wordList

    let queue = [[beginWord, 1]]; // [word, level]

    while (queue.length > 0) {
        const [word, level] = queue.shift();

        if (word === endWord) return level;

        for (let i = 0; i < word.length; i++) {
            for (let c = 97; c <= 122; c++) { // a-z
                const newWord = word.slice(0, i) + String.fromCharCode(c) + word.slice(i + 1);

                if (wordSet.has(newWord)) {
                    queue.push([newWord, level + 1]);
                    wordSet.delete(newWord); // avoid revisiting
                }
            }
        }
    }
    return 0; // no valid transformation
}

// Example usage:
const beginWord = "hit";
const endWord = "cog";
const wordList = ["hot", "dot", "dog", "lot", "log", "cog"];
console.log(ladderLength(beginWord, endWord, wordList)); // Output: 5
