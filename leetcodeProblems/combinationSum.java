class combinationSum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        //define results and combinations
        List<List<Integer>> results = new ArrayList<>();
        List<Integer> combinations = new ArrayList<>();
        
        //edge cases
        if (candidates == null || candidates.length == 0){
            return results;
        }
        
        //sort the arrays
        Arrays.sort(candidates);
        
        int index_pointer = 0;
        
        //helper function to check combinations in DFS Manner
        findCombinations(results, combinations, candidates, target, index_pointer);
        
        return results;
    }
    
    private void findCombinations(List<List<Integer>> results, List<Integer> combinations, int[] candidates, int target, int index_pointer){
        
        //if the combination equals current target
        if(target == 0){
            results.add(new ArrayList<>(combinations));
        }
        
        //start from the current index pointer
        
        for(int i=index_pointer; i<candidates.length; i++){
            //if sum of the combination is greater than target
            //break the current combination and go back
            if(candidates[i] > target){
                break;
            }
            
            combinations.add(candidates[i]);
            findCombinations(results, combinations, candidates, target - candidates[i], i);
            
            //remove the last element if the combination is greater
            //than target size
            combinations.remove(combinations.size() - 1);
        }
    }
}