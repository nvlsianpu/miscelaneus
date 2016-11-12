import os

test_pathes = [
'mule\\krolek',
'glue',
'glue\\def\\z2ylc',
'mule',
'mule\\orek'
]



class DirectoryListTool (list):
    def __init__(self, *args):
        list.__init__(self, *args)
    
    def find_subpathes(self,list_of_pathes):
        list_of_subpaths = []

        for i in range(0,len(list_of_pathes) - 1):
            #print('\r\n')
            for j in range (i + 1 ,len(list_of_pathes)):
                couplepath = [list_of_pathes[i],list_of_pathes[j]]
                cpath = os.path.commonpath(couplepath)
                
                if cpath == couplepath[0]:
                    list_of_subpaths.append(j)
                    
                elif cpath == couplepath[1]:
                    list_of_subpaths.append(i)
                
                #print('i = {0:#d} j = {1:#d} commonpath = {2}'.format(i,j, cpath))
                
        #print(list_of_subpaths)
        return list_of_subpaths
        

    def remove_subpathes(self,list_of_pathes = None):
        if list_of_pathes == None:
            list_of_pathes = self
        list_of_idx_subpaths = self.find_subpathes(list_of_pathes)
        list_of_idx_subpaths.sort(reverse = True)
        #print(list_of_idx_subpaths)
        
        for i in range(0, len(list_of_idx_subpaths)):
            list_of_pathes.pop(list_of_idx_subpaths[i])
        
    
# subpathes_helper = subpathes_opertion()

# print(test_pathes)
# subpathes_helper.remove_subpathes(test_pathes)
# print(test_pathes)

mouobj = DirectoryListTool(['mule\\krolek',
'glue',
'glue\\def\\z2ylc',
'mule',
'mule\\orek'])
mouobj.append('gryj\\jen\\ol')

mouobj.remove_subpathes()
print(mouobj)
