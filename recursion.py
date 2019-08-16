import pandas as pd 
from collections import defaultdict

graph = defaultdict(list)

stack_list, addNode = [],[]
orig_df = pd.DataFrame({'pid':[1,2,3,4,5,6,7,8,9,10,11,12,13, 14, 15,16, 17],
        'ppid':[0, 1,7,7,4,4,1,1,1,8,9,9,12, 3,4,14,1],
        'level':[1,2,3,3,4,4,2,2,2,3,3,3,4,4,4,5,2]})

minigraph = defaultdict(list)

def appendRootGraph(mgraph, sl):
    hir_graph, dictAsKeys = {}, {}
    for i in range(len(sl), 0, -1):
        ppid = orig_df[orig_df['pid'] == sl[i-1]]['ppid'].values[0]
        dictAsKeys.update({ppid:[{sl[i-1]:mgraph[sl[i-1]]}]})
    
    keys = dictAsKeys.keys()
    print(dictAsKeys)

    for i in keys:
        n = [x for x in dictAsKeys.values()]
        print(n)


def recursiveFn(df, stacklist, pn, alreadyPresent):
    stl = stacklist
    for j in df:
        if j in alreadyPresent:
            continue
        else:
            indf = orig_df[orig_df['ppid'] == j]['pid']
            if indf.shape[0] == 0:
                alreadyPresent.append(j)
                graph[pn].append(j)
            else:
                stl.append(j)
                idf = orig_df[orig_df['ppid'] == j]['pid']
                recursiveFn(idf, stl, j, alreadyPresent)
    
    graph_copy = graph.copy()
    
    return graph_copy, stl


def doLogic(sl, iteration, rn):
    for i in iteration:
        sl.append(i)
        #get the df
        subdf = orig_df[orig_df['ppid'] == i]['pid']
        if subdf.shape[0] == 0:
            graph[rn].append(i)
            addNode.append(i)
            sl = sl[:-1]
        else:
            mgraph, stl = recursiveFn(subdf, sl, i, addNode)
            subgraph = appendRootGraph(mgraph, stl)
            print("subgraph:{}".format(subgraph))
            break


rootnode = orig_df[orig_df['level'] == 1]

stack_list.append(rootnode['pid'].values[0])

i = rootnode['pid'][0]

secondlevel = orig_df[orig_df['level'] == 2]['pid']

doLogic(stack_list, secondlevel, i)
print(graph)
