/**
 * @param {number[][]} envelopes
 * @return {number}
 */
var maxEnvelopes = function(envelopes) {
    var output = 0;
    
    //sort array
    envelopes = envelopes.sort(function(a,b) {
        return a[0] - b[0];
    });
    
    var max_envelopes = [];
    
    for(i=0; i < envelopes.length; i++){
        var bestSoFar = 1;
        var w = envelopes[i][0];
        var h = envelopes[i][1];
        
        for(j=0; j < i; j++){
            //condition
            if(w > envelopes[j][0] && h > envelopes[j][1]){
                var current = max_envelopes[j] + 1;
                if(current > bestSoFar){
                    bestSoFar = current;
                }
            }
        }
        max_envelopes.push(bestSoFar)
        
        if(bestSoFar > output){
            output = bestSoFar;
        }
    }
    
    return output;
    
};
