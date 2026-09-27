class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums: number[]): number[][] {

        const size = nums.length;

        const res: number[][] = [];
        const numbers = new Set(nums);

        function backtrack(per: number[], remain:Set<number>) {

            if (per.length === size) {
                res.push([...per])
                return
            }

            for (const num of [...remain]) {

                per.push(num)
                remain.delete(num)

                backtrack(per, remain)

                per.pop()
                remain.add(num)
            }

            return
        }

        backtrack([], numbers)
        return res
    }
}
