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
    first_letter = key[0]
    first_letter_finder = ord(first_letter)
    index = first_letter_finder % self.size

    return index
  



  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    #hashes key
    box = self.arr[self.hash_func(key)]
    new_value = (key, value)
    index = box.head

    if index == None:
      box.append(new_value)

    elif index.data[0] == key:
      index.data = (key, index.data[1] + value)
      index = index.next

    else:
      box.append(new_value






  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  def print_key_values(self):
    for lst in self.arr:
      box = lst.head

      if box == None:
        pass

      else:
        for i in range(lst.length()):
           print(f'{box.data[0]}: {box.data[1]}')
           box = box.next



