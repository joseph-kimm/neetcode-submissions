class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n: number): string[] {

        const res: string[] = []

        function backtrack(paren:string[], open:number, close:number) {

            if (paren.length === 2*n) {
                res.push(paren.join(''))
                return
            }

            if (open < n) {
                paren.push('(')
                backtrack(paren, open+1, close)
                paren.pop()
            }

            if (close < open) {
                paren.push(')')
                backtrack(paren, open, close+1)
                paren.pop()
            }
        }

        backtrack([], 0,0)
        return res

    }
}
