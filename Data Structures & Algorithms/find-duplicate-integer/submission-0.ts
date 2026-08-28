class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findDuplicate(nums: number[]): number {
        const integer = new Set<number>();

        for (const num of nums) {
            if (integer.has(num)) {
                return num
            }
            else {
                integer.add(num)
            }
        }

        return nums[0]
    }
}
