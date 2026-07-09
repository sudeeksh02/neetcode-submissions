class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> ans;
        priority_queue<pair<int,pair<int,int>>,vector<pair<int,pair<int,int>>>,
        greater<pair<int,pair<int,int>>>> pq;

        for (auto p:points){
            int x=p[0];
            int y=p[1];
            int dist= (x*x)+(y*y);
            pq.push({dist,{x,y}});
        }

        for (int i=0;i<k;i++){
            auto p=pq.top().second;
            ans.push_back({p.first,p.second});
            pq.pop();
        }

    return ans;}
};
