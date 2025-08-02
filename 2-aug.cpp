
class Solution
{
public:
    int longestSubarray(vector<int> &arr, int k)
    {
        map<int, int> mp;
        int sum = 0;
        int n = arr.size();
        int ans = 0;

        for (int i = 0; i < n; i++)
        {
            int it = arr[i];

            if (it > k)
            {
                sum++;
            }
            else
            {
                sum--;
            }

            if (sum > 0)
            {
                ans = i + 1;
            }
            else
            {
                if (mp.find(sum - 1) != mp.end())
                {
                    ans = max(ans, i - mp[sum - 1]);
                }
            }

            if (mp.find(sum) == mp.end())
            {
                mp[sum] = i;
            }
        }

        return ans;
    }
};
