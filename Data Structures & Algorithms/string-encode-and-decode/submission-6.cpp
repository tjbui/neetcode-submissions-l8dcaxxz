class Solution {
public:

    string encode(vector<string>& strs) {
        std::vector<int> str_lengths{};

        for (auto &str : strs) {
            str_lengths.push_back(str.size());
        }

        std::string encoded_str{};
        for (auto &length : str_lengths) {
            encoded_str += std::to_string(length);
            encoded_str += ",";
        }
        encoded_str += "#";

        for (auto &str : strs) {
            encoded_str += str;
        }

        return encoded_str;
    }

    vector<string> decode(string s) {
        std::vector<int> sizes{};

        std::string curr_str{};
        int pound_pos = -1;
        for (int i = 0; i < s.size(); i ++) {
            char curr_char = s[i];

            if (curr_char == '#') {
                pound_pos = i;
                break;
            }
            if (curr_char == ',') {
                sizes.push_back(std::stoi(curr_str));
                curr_str = "";
            }
            else {
                curr_str += curr_char;
            }
        }

        if (pound_pos == 0) return std::vector<string>{};

        std::vector<string> result{};
        for (auto &size : sizes) {
            result.push_back(s.substr(pound_pos + 1, size));
            pound_pos += size;
        }

        return result;
    }
};

// Input: strs = ["Hello","World"]

// encode:
// "5,5#HelloWorld"
//     3    8

// decode:
// ["Hello", "World"]