class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.size() == 0 || intervals.size() == 1) {
            return intervals;
        }

        std::sort(intervals.begin(), intervals.end());

        std::vector<std::vector<int>> mergedIntervals{};
        std::vector<int> prevInterval = intervals[0];
        for (int i = 1; i < intervals.size(); i++) {
            int currStart = intervals[i][0];
            int currEnd = intervals[i][1];

            int prevStart = prevInterval[0];
            int prevEnd = prevInterval[1];

            if (currStart > prevEnd) {
                mergedIntervals.push_back(prevInterval);
                prevInterval = intervals[i];

                if (i == intervals.size() - 1) {
                    mergedIntervals.push_back(intervals[i]);
                }
                continue;
            }

            prevInterval[1] = std::max(currEnd, prevEnd);
            if (i == intervals.size() - 1) {
                mergedIntervals.push_back(prevInterval);
            }
        }

        return mergedIntervals;
    }
};

// [1, 3], [1, 5], [6, 7]
// [1, 5], [6, 7]

// [1, 3], [1, 5], [6, 7]
// curr
// [1, 3]

// [1, 3], [1, 5], [6, 7]
//          curr
// [1, 5]

// [1, 3], [1, 5], [6, 7]
//                 curr
// [6, 7]