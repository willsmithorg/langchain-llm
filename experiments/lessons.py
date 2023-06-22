lessons = '''
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

# solution in Python:
def solution():
    """Olivia has $23. She bought five bagels for $3 each. How much money does she have left?"""
    money_initial = 23
    bagels = 5
    bagel_cost = 3
    money_spent = bagels * bagel_cost
    money_left = money_initial - money_spent
    result = money_left
    return result





Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

# solution in Python:
def solution():
    """Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?"""
    golf_balls_initial = 58
    golf_balls_lost_tuesday = 23
    golf_balls_lost_wednesday = 2
    golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
    result = golf_balls_left
    return result





Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

# solution in Python:
def solution():
    """There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?"""
    computers_initial = 9
    computers_per_day = 5
    num_days = 4  # 4 days between monday and thursday
    computers_added = computers_per_day * num_days
    computers_total = computers_initial + computers_added
    result = computers_total
    return result





Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

# solution in Python:
def solution():
    """Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?"""
    toys_initial = 5
    mom_toys = 2
    dad_toys = 2
    total_received = mom_toys + dad_toys
    total_toys = toys_initial + total_received
    result = total_toys
    return result





Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

# solution in Python:
def solution():
    """Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?"""
    jason_lollipops_initial = 20
    jason_lollipops_after = 12
    denny_lollipops = jason_lollipops_initial - jason_lollipops_after
    result = denny_lollipops
    return result





Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

# solution in Python:
def solution():
    """Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?"""
    leah_chocolates = 32
    sister_chocolates = 42
    total_chocolates = leah_chocolates + sister_chocolates
    chocolates_eaten = 35
    chocolates_left = total_chocolates - chocolates_eaten
    result = chocolates_left
    return result





Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

# solution in Python:
def solution():
    """If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?"""
    cars_initial = 3
    cars_arrived = 2
    total_cars = cars_initial + cars_arrived
    result = total_cars
    return result





Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

# solution in Python:
def solution():
    """There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?"""
    trees_initial = 15
    trees_after = 21
    trees_added = trees_after - trees_initial
    result = trees_added
    return result



Q: On the nightstand, there is a red pencil, a purple mug, a burgundy keychain, a fuchsia teddy bear, a black plate, and a blue stress ball. What color is the stress ball?


# solution in Python:
def solution():
    # Put objects into a dictionary for quick look up
    objects = dict()
    objects['pencil'] = 'red'
    objects['mug'] = 'purple'
    objects['keychain'] = 'burgundy'
    objects['teddy bear'] = 'fuchsia'
    objects['plate'] = 'black'
    objects['stress ball'] = 'blue'
    
    # Look up the color of stress ball
    stress_ball_color = objects['stress ball']
    answer = stress_ball_color
    return answer


Q: On the table, you see a bunch of objects arranged in a row: a purple paperclip, a pink stress ball, a brown keychain, a green scrunchiephone charger, a mauve fidget spinner, and a burgundy pen. What is the color of the object directly to the right of the stress ball?

# solution in Python:
def solution():
    
    # Put objects into a list to record ordering
    objects = []
    objects += [('paperclip', 'purple')] * 1
    objects += [('stress ball', 'pink')] * 1
    objects += [('keychain', 'brown')] * 1
    objects += [('scrunchiephone charger', 'green')] * 1
    objects += [('fidget spinner', 'mauve')] * 1
    objects += [('pen', 'burgundy')] * 1
    
    # Find the index of the stress ball
    stress_ball_idx = None
    for i, object in enumerate(objects):
        if object[0] == 'stress ball':
            stress_ball_idx = i
            break
    
    # Find the directly right object
    direct_right = objects[i+1]
    
    # Check the directly right object's color
    direct_right_color = direct_right[1]
    answer = direct_right_color
    return answer
    


Q: On the nightstand, you see the following items arranged in a row: a teal plate, a burgundy keychain, a yellow scrunchiephone charger, an orange mug, a pink notebook, and a grey cup. How many non-orange items do you see to the left of the teal item?

# solution in Python:
def solution():
    # Put objects into a list to record ordering
    objects = []
    objects += [('plate', 'teal')] * 1
    objects += [('keychain', 'burgundy')] * 1
    objects += [('scrunchiephone charger', 'yellow')] * 1
    objects += [('mug', 'orange')] * 1
    objects += [('notebook', 'pink')] * 1
    objects += [('cup', 'grey')] * 1
    
    # Find the index of the teal item
    teal_idx = None
    for i, object in enumerate(objects):
        if object[1] == 'teal':
            teal_idx = i
            break
    
    # Find non-orange items to the left of the teal item
    non_orange = [object for object in objects[:i] if object[1] != 'orange']
    
    # Count number of non-orange objects
    num_non_orange = len(non_orange)
    answer = num_non_orange
    return answer



Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?

# solution in Python:
def solution():
    # If 2015 is coming in 36 hours, then today is 36 hours before.
    today = datetime(2015, 1, 1) - relativedelta(hours=36)
    # One week from today,
    one_week_from_today = today + relativedelta(weeks=1)
    # The answer formatted with %m/%d/%Y is
    result = one_week_from_today.strftime('%m/%d/%Y')
    return result
     

Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

# solution in Python:
def solution():
    # If the first day of 2019 is a Tuesday, and today is the first Monday of 2019, then today is 6 days later.
    today = datetime(2019, 1, 1) + relativedelta(days=6)
    # The answer formatted with %m/%d/%Y is
    result = today.strftime('%m/%d/%Y')
    return result



Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?

# solution in Python:
def solution():
    # If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day later.
    today = datetime(1943, 6, 1) + relativedelta(days=1)
    # 10 days ago,
    ten_days_ago = today - relativedelta(days=10)
    # The answer formatted with %m/%d/%Y is
    result = ten_days_ago.strftime('%m/%d/%Y')
    return result

Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?

# solution in Python:
def solution():
    
    # It is 4/19/1969 today.
    today = datetime(1969, 4, 19)
    # 24 hours later,
    later = today + relativedelta(hours=24)
    # The answer formatted with %m/%d/%Y is
    result = today.strftime('%m/%d/%Y')
    return result



Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?

# solution in Python:
def solution():
    
    # If Jane thought today is 3/11/2002, but today is in fact Mar 12, then today is 3/12/2002.
    today = datetime(2002, 3, 12)
    # 24 hours later,
    later = today + relativedelta(hours=24)
    # The answer formatted with %m/%d/%Y is
    result = later.strftime('%m/%d/%Y')
    return result



Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?

# solution in Python:
def solution():    
    # If Jane was born on the last day of Feburary in 2001 and today is her 16-year-old birthday, then today is 16 years later.
    today = datetime(2001, 2, 28) + relativedelta(years=16)
    # Yesterday,
    yesterday = today - relativedelta(days=1)
    # The answer formatted with %m/%d/%Y is
    result = yesterday.strftime('%m/%d/%Y')
    return result

'''