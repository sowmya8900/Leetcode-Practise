class Solution {
public:
    int balancedStringSplit(string s) {
        int c = 0, rc = 0, lc = 0;
        for(int i = 0; i < s.length(); i++){
            if (s[i] == 'R'){
                rc += 1;
            }
            else{
                lc += 1;
            }
            if (lc == rc){
                c += 1;
                lc = 0;
                rc = 0;
            }
        }
        return c;
    }
};
