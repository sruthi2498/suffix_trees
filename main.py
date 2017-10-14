from suffix_trees import SuffixTree
from graph import Graph

string="ababc$"


tree={}
tree=SuffixTree()

s1="what's$bred$in$the$bone$will$stick$to$the$flesh.$"
# tree.Add_To_Tree(s1,91,3)
# s2="the$servant$caught$a$severe$cold,$but$he$never$changed$his$color$or$complexion."
# tree.Add_To_Tree(s2,91,2)

# tree.Query("bred")
#tree.Query("rest")

s2="servant$severe$"
tree.Add_To_Tree(s1,91,3)
tree.Add_To_Tree(s2,91,2)

tree.Query("none")

