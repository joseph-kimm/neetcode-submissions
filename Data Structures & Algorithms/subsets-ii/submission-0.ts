class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsetsWithDup(nums: number[]): number[][] {
        nums.sort((a,b) => a - b)
        const n = nums.length
        const res:number[][] = []

        function backtrack(subset: number[], i:number) {

            if (i === n) {
                res.push([...subset])
                return
            }

            const val = nums[i]
            i++
            subset.push(val)
            backtrack(subset, i)

            while (i < n && nums[i] === val) {
                i++
            }

            subset.pop()
            backtrack(subset,i)
        }

        backtrack([], 0)
        return res

    }
}
