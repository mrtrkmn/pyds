"""
I wrote a crawler that visits web pages, stores a few keywords in a database, and follows links to other web pages. I noticed that my crawler was wasting a lot of time visiting the same pages over and over, so I made a set, visited, where I'm storing URLs I've already visited. Now the crawler only visits a URL if it hasn't already been visited.
Thing is, the crawler is running on my old desktop computer in my parents' basement (where I totally don't live anymore), and it keeps running out of memory because visited is getting so huge.
How can I trim down the amount of space taken up by visited?
"""

class Trie(object):
    def __init__(self):
        self.root_node = {}

    def print_trie(self):
        import json 
        print(json.dumps(self.root_node, indent = 2))
   
    def add_word(self, word):
        current_node = self.root_node
        is_new_word = False

        # work downwards through the trie, adding nodes 
        # as needed, and keeping track of whether we add any nodes.

        for char in word: 
            if char not in current_node: 
                is_new_word = True 
                current_node[char] = {}
            current_node = current_node[char]

        # Explicitly mark the end of a word 
        # Otherwise, we might say a word is 
        # present if it is a prefix of a different
        # longer word that was added earlier

        if "End Of Word" not in current_node:
            is_new_word = True
            current_node ["End Of Word"] = {}

        return is_new_word
    # --> For answering, ternary search tree, a bloom filter are also great answers 



print("Running trie")
t = Trie()
t.add_word("google.com")
t.add_word("google.com/example")
t.add_word("google.com/test")
t.add_word("yahoo.com/terrr")
t.add_word("yahoo.com/example") 

t.print_trie()