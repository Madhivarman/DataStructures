var maximalSquare = function(matrix) {
    //null case identifier
    if(matrix.length == 0){
        return 0;
    }
    
    var no_of_rows = matrix.length;
    var no_of_cols = matrix[0].length;
    var area = null;
    var dp = new Array(no_of_rows);
    
    //set the columns
    for(j=0; j < dp.length; j++){
        dp[j] = Array(no_of_cols).fill(0);
    }
    
    var maxarea=-1; //initial value
    
    //fill the first row
    for(i=0; i < no_of_cols; i++){
        dp[0][i] = parseInt(matrix[0][i])
        if(maxarea <= dp[0][i]){
            maxarea = dp[0][i]
        }
    }
    
    //fill the first column
    for(j=0; j <  no_of_rows; j++){
        dp[j][0] = parseInt(matrix[j][0])
        if(maxarea <= dp[j][0]){
            maxarea = dp[j][0]
        }
    }
    
    for(i=1; i< no_of_rows; i++){
        for(j=1; j< no_of_cols; j++){
            if(matrix[i][j] == "1"){
                dp[i][j] = Math.min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + parseInt(matrix[i][j])
                if(dp[i][j] >= maxarea){
                    maxarea = dp[i][j]
                }
            }
        }
    }
    
    return maxarea * maxarea;
    
};


//testcase 1
matrix = [["0","0","0","0","0"],["1","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]]
console.log(maximalSquare(matrix))