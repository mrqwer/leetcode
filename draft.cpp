#include <iostream>
#include <vector>
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    Solution (){}
    bool containsDuplicate(vector<int>& nums) {
        vector<int> s;
        for(int i: nums){
            if (find(s.begin(), s.end(), i) != s.end()){
                return true;
            }
            s.push_back(i);
        }
        return false;
    }
};

int main(){
    Solution *sol = new Solution();
    vector<int> arr{1, 2, 3, 4};
    cout << sol->containsDuplicate(arr)<<"\n";
    return 0;
}
