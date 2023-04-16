# Python program to  
# demonstrate queue implementation 
# using list 
  
# Initializing a queue 
names = [] 
  
# Adding elements to the queue
for x in range(10):
    name = input("Enter name: ")
    names.append(name)
    
print ("Queues are First-In First-Out (FIFO) data structures") 
print("\nInitial names. Used names.append(item) to enter elements into the queue") 
print(names) 
  
# Removing elements from the queue 
print("\nElements dequeued from queue. Used names.pop(0) to pop element in front") 
for x in range(10):
    print(names.pop(0))
  
print("\nQueue after removing elements") 
print(names) 
  
# Uncommenting print(queue.pop(0)) 
# will raise and IndexError 
# as the queue is now empty 

