class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> v;
        if(n == 1){
            return {0};
        }
        int i = 1;
        while(i < n){
            v.push_back(i);
            v.push_back(-1 * i);
            i += 2;
        }
        if(n%2 != 0){
            v.push_back(0);
        }
        return v;
    } 
};
