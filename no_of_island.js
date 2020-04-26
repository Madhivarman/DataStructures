/**
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
 * You may assume all four edges of the grid are all surrounded by water.
 */

var numberOfIslands = function(island){
    let area = 0;

    for(let row=0; row < island.length; row++){
        for(let col=0; col < island[0].length; col++){
            if(island[row][col] != 1){
                continue;
            }else{
                //update the area
                area++;
                dfs(island, row, col)
            }
        }
    }
    return area;
}

function dfs(island, row, col){
    const directions = [[-1, 0],[1,0],[0, -1],[0, 1]] //up, down, left, right
    if(island[row][col] != 1){
        return;
    }

    //change the cell into seen
    island[row][col] = 2;

    //iterate through the directions
    for(let dir=0; dir < directions.length; dir++){
        //get the next pointer
        let next_row = row + directions[dir][0]
        let next_col = col + directions[dir][1]

        //condition to check
        if(0 <= next_row && next_row < island.length && 0 <= next_col && next_col < island[0].length && island[next_row][next_col] == 1){
            dfs(island,next_row, next_col)
        }
    }
}


let island = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
let island2 = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]

console.log(numberOfIslands(island))
console.log(numberOfIslands(island2))
