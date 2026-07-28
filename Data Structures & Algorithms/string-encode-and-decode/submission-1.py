class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#"
            result += string
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        reading_num = True
        string_length_str = ""
        string_length = 0
        string_index = 0
        cur_string = ""
        results = []
        for char in s:
            if reading_num:
                if char == "#":
                    string_length = int(string_length_str)
                    if string_length != 0:
                        reading_num = False
                    else:
                        results.append("")
                    string_length_str = ""
                    continue
                string_length_str += char
            else:
                cur_string += char
                string_index += 1
                if string_index == string_length:
                    results.append(cur_string)
                    cur_string = ""
                    string_index = 0
                    reading_num = True
        return results
