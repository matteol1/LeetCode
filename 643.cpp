#include <algorithm>
#include <iostream>
#include <stl>

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double avg = - 100000000;
        double sum = 0;
        double new_sum = 0;
        for (int i=0; i<k; i++) {sum +=nums[i];}; 
        for (int i=0; i<size(nums)-k; i++) {
            new_sum = sum + nums[i+k] - nums[i];
            if (new_sum>sum) {sum=new_sum;};
        return sum/k;
    

    }
};

int main() {
    Solution *sol = new Solution();


};