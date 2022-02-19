class Solution {
public:
    double average(vector<int>& salary) {
        double sum = 0;
        double avg = 0;
        int min = salary[0];
        int max = salary[0];
        for(int i = 0; i < salary.size(); i++){
            sum += salary[i];
        
            if(salary[i] <= min){
                min = salary[i];
            }
            if(salary[i] >= max){
                max = salary[i];
            }
        }
        
        return((sum-min-max)/(salary.size()-2));
        
    }
};
