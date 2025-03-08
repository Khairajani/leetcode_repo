class Solution:
    def solve_for_generate_parenthesis(self,closing_bracket_count,opening_bracked_count,intermediate_string,result):
        if opening_bracked_count==0 and closing_bracket_count==0:
            result.append(intermediate_string)
            return
        
        # We can select opening bracket anytime
        # But, we can select closing bracket only if the remaining count of closing bracket is greater than opening ones
        if closing_bracket_count>opening_bracked_count:
            #either go with opening (if count!=0)
            if opening_bracked_count>0:
                self.solve_for_generate_parenthesis(closing_bracket_count,opening_bracked_count-1,intermediate_string+"(", result)

            #or go with closing
            self.solve_for_generate_parenthesis(closing_bracket_count-1,opening_bracked_count,intermediate_string+")", result)

        # else, we the choice is to select opening 
        elif opening_bracked_count:
            self.solve_for_generate_parenthesis(closing_bracket_count,opening_bracked_count-1,intermediate_string+"(", result)
        return


    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        intermediate_string = ""
        self.solve_for_generate_parenthesis(n,n,intermediate_string,result)
        return result