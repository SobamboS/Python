import random
lst = list(range(1, 11))
print(lst)

random.shuffle(lst)
print(lst)

lst.append(20)
lst.extend([56, 43, 21, 90]) # Adds elements individually to the list
lst += [99, 59, 67, 23] # Augumented assginment is used to add a list
lst.append([34, 76, 89, 23, 41]) # Append at the end of the list
lst.insert(0, 41) # inserts number 41 at index 0
lst.insert(-1, 77)
last_item = lst.pop() # Pop removes the last elements (alters the list) and returns it
last_item_at_index_0 = lst.pop(0) # Pop removes the element at an index
lst.remove(99) # Remove the first occurrence of a particular element if it is more than one
print('Count', lst.count(77)) # Returns the number of times an element occurs

#del lst # Deletes a variable

#lst.clear() # Clears every element in the list

#lst.copy # Copies every element in the list





print(lst)

print(lst)

print(lst)

print(lst)

print(last_item)

print(lst)

print(last_item_at_index_0)

print(lst)

print(lst)

print(lst.index(3))

lst.reverse()


print(lst)


sentence = "Write a sentence and reverse it"
s_list = sentence.split()
s_list.reverse()
print(" ".join(s_list))

fruits = ['banana', 'apples', 'cucumber', 'mango', 'grape']
fruits.sort()
print(fruits)


def last_element(string):
    return string[-1]

fruits = ['banana', 'apples', 'cucumber', 'mango', 'grape']
fruits.sort(key = last_element, reverse= True)
print(fruits)



def anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(anagram('listen', 'silent'))