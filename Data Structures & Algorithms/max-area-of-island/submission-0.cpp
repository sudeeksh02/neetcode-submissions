class Solution {
public:
   int dir[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
   int area=0,temp=0;
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int row=grid.size(),col=grid[0].size();
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if (grid[i][j]){dfs(grid,i,j);if(area<temp){area=temp;}temp=0;}
            }
        }return area;
    }
    
    void dfs(vector<vector<int>>& grid, int r,int c){
        if(r<0 || c<0|| r>=grid.size() ||c>=grid[0].size() || grid[r][c]==0) return;
        
        grid[r][c]=0;
        temp++;
        for(int i=0;i<4;i++){
            dfs(grid,r+dir[i][0],c+dir[i][1]);
        }
    }
};