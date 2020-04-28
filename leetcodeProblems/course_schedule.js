/**
 * There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
 * Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
 * which is expressed as a pair: [0,1]
 * Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
 */

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(num_of_courses, course_lists) {
    //initial variables
    let stack = [];
    let visited = [];
    let repeated = []
    let graph = {};

    //helper function
    //in this function we will be using visited, graph
    //variables
    function topologicalSort(node){
        visited[node] = true;
        repeated[node] = true;
        
        //check if the node has children
        for(let n in graph[node]){
            if(!(visited[n])){
                if(topologicalSort(n)){
                    return true;
                }
            }
            //if the node found in repeated list
            else if(repeated[n]){
                return true;
            }
        }

        stack.push(node);
        repeated[node] = false; //update the node

        return false;

    }

    //to keep track if visited or not
    for(let r=0; r <= num_of_courses; r++){
        visited.push(false);
        repeated.push(false)
    }

    //create a nodes
    for(let r=0; r < num_of_courses; r++){
        graph[r] = {}
    }

    //create graph like structures
    //{0: {1: 1}, 1: {2: 1}, 2: {}, 3: {2: 1}}
    for(let r=0; r < course_lists.length; r++){
        let dependency = course_lists[r][1]
        let course = course_lists[r][0]
        graph[dependency][course] = 1
    }

    let hasCycle = false

    //iterate through all the nodes
    for(let r=0; r < num_of_courses; r++){
        //if the node are not visited
        if(!visited[r]){
            if(topologicalSort(r)){
                hasCycle = true;
            }
        }
    }

    return !(hasCycle);
};

//let numCourses = 4
//let prerequisites = [[1,0],[2,1], [2,3]]

let numCourses=2
let prerequisites = [[1,0],[0,1]]

console.log(canFinish(numCourses, prerequisites));