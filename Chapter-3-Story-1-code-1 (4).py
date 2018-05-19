friend_names=['Lisa', 'Alex', 'John', 'Piper', 'Jenny']
print(friend_names)
print(friend_names[2])
friends_ages=[15, 15, 14, 17, 15]
print("In 15 years  , %s will be %s years old" % (friend_names[0],friends_ages[0]+15))
print("In 15 years  , %s will be %s years old" % (friend_names[2],friends_ages[2]+15))
friend_names[3]='Pete' 
friends_ages[3]=14
print(friend_names)
print(friends_ages)
names_and_ages=[friend_names,friends_ages]
print(names_and_ages)
print(names_and_ages[0][1])
friend_names.append('Ben')
friend_names.append('Ken')
print(friend_names)
del friend_names[6]
del friend_names[5]
print(friend_names) 
