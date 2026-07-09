class Solution {
public:
    int lastStoneWeight(vector<int>& nums) {
         priority_queue<int> pq;

    int length=(nums.size());
    for(int i=0;i<length;i++){
        pq.push(nums[i]);
    }
    int top,bottom;
    while(pq.size()>1){
        top=pq.top();
        pq.pop();
        bottom=pq.top();
        pq.pop();
        if(bottom<top){
            pq.push(top-bottom);

        }
    }
    if(pq.empty()){
        return 0;
    }
   else{ return pq.top();}
    
    }
};