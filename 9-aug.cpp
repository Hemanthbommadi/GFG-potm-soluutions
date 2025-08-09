class Solution
{
public:
    vector<int> calculateZ(string &input)
    {
        vector<int> z(input.size(), 0);
        int left = 0;
        int right = 0;
        for (int k = 1; k < (int)input.size(); k++)
        {
            if (k > right)
            {
                left = right = k;
                while (right < input.size() && input[right] == input[right - left])
                    right++;
                z[k] = right - left;
                right--;
            }
            else
            {
                int k1 = k - left;
                if (z[k1] < right - k + 1)
                {
                    z[k] = z[k1];
                }
                else
                {
                    left = k;
                    while (right < input.size() && input[right] == input[right - left])
                        right++;
                    z[k] = right - left;
                    right--;
                }
            }
        }
        return z;
    }

    int getLongestPrefix(string &s)
    {
        int n = s.size();
        vector<int> z = calculateZ(s);
        for (int i = n - 1; i >= 0; i--)
        {
            if (z[i] == n - i)
            {
                return i;
            }
        }
        return -1;
    }
};
