class Solution {
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     */
    combinationSum2(candidates: number[], target: number): number[][] {

        candidates.sort((a,b) => a-b)

        const res:number[][] = [];
        

        function backtrack(i:number, com: number[], sum: number) {

            if (sum === 0) {
                res.push(com)
                return
            }

            else if (sum < 0 || i >= candidates.length) {
                return
            }

            let val = candidates[i]
            i++
            com.push(val)
            backtrack(i, [...com], sum - val)

            com.pop()
            while (i < candidates.length && candidates[i] === val) {
                i++
            }
            backtrack(i, [...com], sum)
        }

        backtrack(0,[], target)
        return res

    }
}
