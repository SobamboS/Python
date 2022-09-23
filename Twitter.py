users = [
    {'name': 'Hadiza',
      'age': 23,
      'gender': 'Female',
      'username': 'deezah',
      'is_verified': True,
      'tweets': [
          {'content': 'PO for president', 'likes': 450, 'retweets': 253},
          {'content': 'Atiku is our man', 'likes': 4, 'retweets': 2},
      ]},

    {'name': 'Fred',
      'age' : 32 ,
      'gender': 'Male',
      'username': 'Fredo',
      'is_verified': False,
      'tweets': [
          {'content': 'Gbedu dey plenty', 'likes': 560, 'retweets': 903},
          { 'content' : 'Igbo and Shayo' , 'likes' : 489 , 'retweets' : 29 } ,
      ] } ,

    { 'name' : 'Olusola' ,
      'age' : 56 ,
      'gender' : 'Male' ,
      'username': 'Don_Millie',
      'is_verified': True,
      'tweets': [
          { 'content': 'PO for president', 'likes': 4150, 'retweets': 4253},
          {'content': 'Atiku is not my own man', 'likes': 4, 'retweets': 2},
      ]},

    {'name': 'Banke',
      'age': 23,
      'gender': 'Female',
      'username': 'Bank',
      'is_verified': False,
      'tweets': [
          {'content': 'Singer', 'likes': 4500, 'retweets': 2853},
      ]}
]

no_of_users = len(users)
usernames = {user['username'] for user in users}
female_users = [user for user in users if user['gender']== 'female']
inactive_users = [user for user in users if len(user['tweets']) == 0]
name_and_age = [{'name': user['name'], 'age': user['age']} for user in users]
print(female_users)
print(name_and_age)

print(sum(user['age']for user in users)/ len(users))
print(any(user['is_verified']for user in users))
