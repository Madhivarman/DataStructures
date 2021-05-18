"""
  Problem Statement:
      Given a list paths of directory info, including the directory path, and all the files with contents in this directory, 
      return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.
      A group of duplicate files consists of at least two files that have the same content.
"""

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        #input format = (directory, filepath(content))
        content_map = defaultdict(list)
        #iterate through lists
        for path in paths:
            split_by = path.split(" ") #split by space
            directory = split_by[0] #directory
            ls = split_by[1:] #get list of files
            #iterate through files
            for files in ls:
				#preprocess, and get only filepath without any file content
                full_path = directory + "/" + files.split("(")[0].replace("(","")
				#get content and preprocess
                contents = files.split("(")
                contents = contents[1].replace(")","")
                #check if content present in the map
                if contents in content_map:
                    content_map[contents].append(full_path)
                else:
                    content_map[contents] = [full_path]
                    
        ans = []
		#filter out only duplicate  files are present
        for k,v in content_map.items():
            if len(v) > 1:
                ans.append(v)
        return ans
