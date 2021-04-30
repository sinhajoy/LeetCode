class Solution {
public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
	
        //base case
        if(x == 1 and y == 1){
            if(bound < 2)
                return {};
            else
                return {2};  // Minimum possible value if both x and y are 1.
        }
        
        vector<int> v;
        
        int temp = 1;
        int xc = 0, yc=0;
        
        while(temp <= bound and x!=1){
            temp *= x;
            xc++;
        }
        
        temp = 1;
        while(temp <= bound and y!= 1){
            temp *= y;
            yc++;
        }
        
        set<int> s;  // Used to avoid duplicates
		
        for(int i=0; i<=xc; i++){
            for(int j=0; j<=yc; j++){
                int n = pow(x,i) + pow(y,j);
                if(n <= bound)
                    s.insert(n);
            }
        }
        
        for(auto t : s)
            v.push_back(t);
        
        return v;
    }
};