from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)



  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):

     return [LinkedList() for i in range(size)]


  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    #first letter of the key "lower" will always lowercase letters
    first_letter = key[0].lower()

    distance_from_a = ord(first_letter) - ord('a')
    #mods so we can be in range
    index = distance_from_a % self.size
    return index
  



  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    #hashes key
    box = self.arr[self.hash_func(key)]
    # this is used to assign key and value pairs to a tuple
    new_pair = (key,value)
    # This checks if thier are any key and value pair duplicates
    dup_pair_checker = box.find(key)
    # if duplicate key and value pair exist, append it, then replace the old pair
    if dup_pair_checker == None:
      box.append(new_pair)

    else:
      if dup_pair_checker == key:
        dup_pair_checker = (key, dup_pair_checker + 1)






  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    for lst in self.arr:
      pass



