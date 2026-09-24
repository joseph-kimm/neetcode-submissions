class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums: number[], target: number): number[][] {

        const res:number[][] = [];

        function backtrack(i: number, com: number[], sum: number) {

            if (sum === 0) {
                res.push(com)
                return
            }

            else if (sum < 0 || i >= nums.length) {
                return
            }

            com.push(nums[i])
            backtrack(i, [...com], sum - nums[i])

            com.pop()
            backtrack(i+1, [...com], sum)
        }

        backtrack(0,[], target)
        return res
    }
}
