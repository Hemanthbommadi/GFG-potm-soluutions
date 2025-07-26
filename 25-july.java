class Solution {
    int maxCircularSum(int[] arr) {
        int total = 0, maxSum = arr[0], curMax = 0;
        int minSum = arr[0], curMin = 0;

        for (int num : arr) {
            total += num;

            curMax = Math.max(curMax + num, num);
            maxSum = Math.max(maxSum, curMax);

            curMin = Math.min(curMin + num, num);
            minSum = Math.min(minSum, curMin);
        }

        if (maxSum < 0) return maxSum; 
        return Math.max(maxSum, total - minSum);
    }
}