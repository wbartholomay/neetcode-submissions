class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word))
            result += "#"
            result += word
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []
        reading_number = True
        current_word_length_str = ""
        current_word_length = 0
        current_word = ""
        for char in s:
            if reading_number:
                if char == "#":
                    current_word_length = int(current_word_length_str)
                    print(f"Current word length: {current_word_length}")
                    reading_number = False
                    if current_word_length == 0:
                        result.append("")
                        reading_number = True
                else:
                    current_word_length_str += char
                continue
            current_word += char
            if len(current_word) == current_word_length:
                result.append(current_word)
                current_word = ""
                current_word_length_str = ""
                reading_number = True
        return result
            
