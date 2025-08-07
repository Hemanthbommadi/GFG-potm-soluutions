class Solution {
public:
    int minDifference(vector<string> &arr) {
        
        vector<int> seconds;
        int n = arr.size();
        for (auto it : arr) {
            int h = stoi(it.substr(0, 2));
            int m = stoi(it.substr(3, 2));
            int s = stoi(it.substr(6, 2));
            int sec = h * 60 * 60 + m * 60 + s;
            seconds.push_back(sec);
        }

        sort(seconds.begin(), seconds.end());
        int diff = INT_MAX;
        for (int i = 1; i < n; i++) {
            diff = min(diff, (seconds[i] - seconds[i - 1]));
        }

        int rotation = 24 * 60 * 60;
        diff = min(diff, (seconds[0] + rotation - seconds[n - 1]));
        return diff;
    }
};
