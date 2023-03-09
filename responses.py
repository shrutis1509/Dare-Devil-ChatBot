import random

dare_list = ["Eat a raw piece of garlic.", "Do 100 squats.", "Keep three ice cubes in your mouth until they melt.", "Put 10 different available liquids into a cup and drink it", "Yell out the first word that comes to your mind.", "Eat a spoonful of mustard", "Eat a snack without using your hands.", "Try to put your whole fist in your mouth.", "Tell everyone an embarrassing story about yourself.", "Try to lick your elbow", "Tell the saddest story you know.", "Howl like a wolf for two minutes.", "Dance without music for two minutes."]

truth_list = ["When was the last time you lied?", "When was the last time you cried?", "What's your biggest fear?", "What's your biggest fantasy?", "What's something you're glad your mum doesn't know about you?", "What's the worst thing you've ever done?", "What's a secret you've never told anyone?", "Have you ever cheated in an exam?", "Have you ever broken the law?", "What's the most embarrassing thing you've ever done?", "What's your biggest insecurity?", "What's the biggest mistake you've ever made?", "What's the most disgusting thing you've ever done", "Do you have a hidden talent?"]

def get_response(message: str) -> str:
    message = message.lower()

    if message == '$hello' or message == '$hi':
        return 'Hey there!'
    
    if message == '$dare': 
        return str(random.choice(dare_list))
    
    if message == '$truth':
        return str(random.choice(truth_list))

    if message == '$help':
        return '''`This is a Truth and Dare bot.
        
Usable commands are:
    $hi or $hello - To get a hello back from the bot.
    $Dare - To get a random Dare from the bot.
    $Truth - To get a random Truth question from the bot.

    Using "?" symbol before any above mentioned command will lead the bot to send the text in your DM.`'''

    return