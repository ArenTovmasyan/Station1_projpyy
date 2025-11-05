from random import choice
def get_valid_number(question: str) -> int:
    while True:
        inp_number = input(question)
        if inp_number.strip() == "":
            print('you have forgot to enter a number')

        elif not inp_number.isnumeric():
            print("Please enter a number.")
        else:
            return int(inp_number)

def get_valid_string(question: str) -> str:
    while True:
        inp_string = input(question)
        if inp_string.strip() == "":
            print(f"Please don't leave it empty.")
        elif inp_string.isnumeric():
            print(f"Please don't enter a number.")
        else:
            return inp_string
def get_valid_time(question: str) -> str:
    while True:
        inp_time = input(question)
        if inp_time.strip() == "":
            print(f"Please don't leave it empty.")
        elif inp_time.isnumeric():
            print(f'{inp_time} is not measure of time. please enter a valid value for example(day, year, month, etc)')
        else:
            return inp_time
def story_choice(story_list: list):
    for idx, story in enumerate(story_list):
        print(f'{idx + 1}. {story}')
    chosen_story = input("Chose the number of story you chose: ")
    if chosen_story.isnumeric():
        chosen_story = int(chosen_story)
        try:
            return story_list[chosen_story - 1]
        except IndexError:
            return choice(story_list)

def story_generate():
    story_titles = ['Hospital Visit','Camping Trip','Magic Castle']
    story = story_choice(story_titles)

    questions = {
        1: {
            'Number': 'Type a number:',
            'Measure of time': 'Type a unit of time:',
            'Mode of Transportation': 'Type a mode of transportation:',
            'Adjective': 'Type an adjective:',
            'Adjective2': 'Type another adjective:',
            'Noun': 'Type a noun:',
            'Color': 'Type a color:',
            'Part of the Body': 'Type a part of the body:',
            'Verb': 'Type a verb:',
            'Number2': 'Type another number:',
            'Noun2': 'Type another noun:',
            'Noun3': 'Type a third noun:',
            'Part of the Body2': 'Type another part of the body:',
            'Verb2': 'Type a second verb:',
            'Noun4': 'Type a fourth noun:',
            'Adjective3': 'Type a third adjective:',
            'Silly Word': 'Type a silly word:',
            'Noun5': 'Type a fifth noun:'
        },
        2: {
            'Proper Noun': 'Type a person’s name:',
            'Measure of time': 'Type a unit of time:',
            'Noun': 'Type a noun:',
            'Adjective (Feeling)': 'Type an adjective (feeling):',
            'Verb': 'Type a verb:',
            'Adjective2 (Feeling)': 'Type another adjective (feeling):',
            'Animal': 'Type an animal:',
            'Verb2': 'Type a second verb:',
            'Color': 'Type a color:',
            'Verb (ending in ing)': 'Type a verb ending in -ing:',
            'Number': 'Type a number:',
            'Color (Animal)': 'Type a color:',
            'Animal2': 'Type another animal:',
            'Number (Silly Word)': 'Type a number:',
            'Silly Word': 'Type a silly word:',
            'Noun2': 'Type another noun:'
        },
        3: {
            'Proper Noun': 'Type a person’s name:',
            'Measure of time': 'Type a unit of time:',
            'Adjective': 'Type an adjective:',
            'Color': 'Type a color:',
            'Animal': 'Type an animal:',
            'Place': 'Type a place:',
            'Adjective2': 'Type another adjective:',
            'Magical Creature (Plural)': 'Type a magical creature (plural):',
            'Adjective3': 'Type a third adjective:',
            'Magical Creature (Plural2)': 'Type another magical creature (plural):',
            'Room in a House': 'Type a room in a house:',
            'Noun': 'Type a noun:',
            'Noun2': 'Type another noun:',
            'Noun (Plural)3': 'Type a plural noun:',
            'Adjective4': 'Type another adjective:',
            'Noun (Plural)4': 'Type another plural noun:',
            'Number': 'Type a number:',
            'Verb (ending in ing)': 'Type a verb ending in -ing:',
            'Adjective5': 'Type a fifth adjective:',
            'Noun5': 'Type another noun:'
        }
    }


    if story == 'Hospital Visit':
        for question in questions[1]:
            if 'number' in  questions[1][question]:
                questions[1][question] = get_valid_number(questions[1][question])
            elif 'time' in questions[1][question]:
                questions[1][question] = get_valid_time(questions[1][question])
            else:
                questions[1][question] = get_valid_string(questions[1][question])
        return f"""
it was about {questions[1]['Number']} {questions[1]['Measure of time']} ago when I arrived at the hospital in a {questions[1]['Mode of Transportation']}. 
The hospital is a/an {questions[1]['Adjective']} place, there are a lot of {questions[1]['Adjective2']} {questions[1]['Noun']} here. 
There are nurses here who have {questions[1]['Color']} {questions[1]['Part of the Body']}. 
If someone wants to come into my room I told them that they have to {questions[1]['Verb']} first. 
I’ve decorated my room with {questions[1]['Number2']} {questions[1]['Noun2']}. 
Today I talked to a doctor and they were wearing a {questions[1]['Noun3']} on their {questions[1]['Part of the Body2']}. 
I heard that all doctors {questions[1]['Verb2']} {questions[1]['Noun4']} every day for breakfast. 
The most {questions[1]['Adjective3']} thing about being in the hospital is the {questions[1]['Silly Word']} {questions[1]['Noun5']}!
"""
    elif story == 'Camping Trip':
        for question in questions[2]:
            if 'number' in questions[2][question]:
                questions[2][question] = get_valid_number(questions[2][question])
            elif 'time' in questions[2][question]:
                questions[2][question] = get_valid_time(questions[2][question])
            else:
                questions[2][question] = get_valid_string(questions[2][question])
        return f"""
This weekend I am going camping with {questions[2]['Proper Noun']}. 
I packed my lantern, sleeping bag, and {questions[2]['Noun']}. 
I am so {questions[2]['Adjective (Feeling)']} to {questions[2]['Verb']} in a tent. 
I am {questions[2]['Adjective2 (Feeling)']} we might see a(n) {questions[2]['Animal']}, I hear they’re kind of dangerous. 
While we’re camping, we are going to hike, fish, and {questions[2]['Verb2']}. 
I have heard that the {questions[2]['Color']} lake is great for {questions[2]['Verb (ending in ing)']}. 
Then we will {questions[2]['Verb (ending in ing)']} hike through the forest for {questions[2]['Number']} {questions[2]['Measure of time']}. 
If I see a {questions[2]['Color (Animal)']} {questions[2]['Animal2']} while hiking, I am going to bring it home as a pet! 
At night we will tell {questions[2]['Number (Silly Word)']} {questions[2]['Silly Word']} stories and roast {questions[2]['Noun2']} around the campfire!!
"""
    else:
        for question in questions[3]:
            if 'number' in  questions[3][question]:
                questions[3][question] = get_valid_number(questions[3][question])
            elif 'time' in questions[3][question]:
                questions[3][question] = get_valid_time(questions[3][question])
            else:
                questions[3][question] = get_valid_string(questions[3][question])
        return f"""
Dear {questions[3]['Proper Noun']}, I am writing to you from a {questions[3]['Adjective']} castle in an enchanted forest. 
I found myself here one day after going for a ride on a {questions[3]['Color']} {questions[3]['Animal']} in {questions[3]['Place']}. 
There are {questions[3]['Adjective2']} {questions[3]['Magical Creature (Plural)']} and {questions[3]['Adjective3']} {questions[3]['Magical Creature (Plural2)']} here! 
In the {questions[3]['Room in a House']} there is a pool full of {questions[3]['Noun']}. 
I fall asleep each night on a {questions[3]['Noun2']} of {questions[3]['Noun (Plural)3']} and dream of {questions[3]['Adjective4']} {questions[3]['Noun (Plural)4']}. 
It feels as though I have lived here for {questions[3]['Number']} {questions[3]['Measure of time']}. 
I hope one day you can visit, although the only way to get here now is {questions[3]['Verb (ending in ing)']} on a {questions[3]['Adjective5']} {questions[3]['Noun5']}!!
"""






print(story_generate())












