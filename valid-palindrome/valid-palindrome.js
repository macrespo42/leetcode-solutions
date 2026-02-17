function isPalindrome(s) {
  const text = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i].match(/^[a-z0-9]+$/i)) {
      text.push(s[i].toLowerCase());
    }
  }
  let left = 0;
  let right = text.length - 1;
  while (left < text.length) {
    if (text[left] !== text[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
}
