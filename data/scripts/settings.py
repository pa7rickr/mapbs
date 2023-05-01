import bs
from datetime import datetime
date = datetime.now().strftime('%d')

enableTop5effects = True
enableTop5commands = True
enableCoinSystem = True

enableStats = True

print 'Enable Stats: ', enableStats

spamProtection=True

enableChatFilter = True

coinTexts = [
    'Welcome to Ultimate Server',
    'Use "/shop commands" to see commands available to buy.',
    'Use "/shop effects" to see effects available and their price.',
    'Use "/me" or "/stats" to see your stats in this server', 
    'Use "/buy" to buy effects that you like',
    'Use "/donate" to give some of your tickets to other players',
    'Use "/scoretocash" to convert some of your score to '+bs.getSpecialChar('ticket')+'\nCurrent Rate: 5scores = '+bs.getSpecialChar('ticket')+'1',
    'Join WhatsApp Group for further information'
]

questionDelay = 45 #60 #seconds
questionsList = {
  "Who is the owner of this server?": "pa7rick",
  "Who painted the Mona Lisa?": "leonardo davinci",
  "What is the name of the famous amphitheatre in Rome?": "colosseum",
  "Who was the first president of the United States?": "washington",
  "Who was the leader of Nazi Germany during World War II?": "hitler",
  "What is the name of the ship that carried Charles Darwin on his journey to the Galapagos Islands?": "beagle",
  "Who wrote the novel 'To Kill a Mockingbird'?": "lee",
  "What is the name of the ancient Egyptian writing system?": "hieroglyphs",
  "Who was the first female prime minister of Great Britain?": "thatcher",
  "What was the name of the family that ruled Florence during the Renaissance?": "medici",
  "Who wrote the play 'Hamlet'?": "shakespeare",
  "What was the name of the war fought between the North and the South in the United States from 1861 to 1865?": "civil war",
  "Who was the queen of Egypt who allied with Julius Caesar and Mark Antony?": "cleopatra",
  "What is the name of the French national anthem?": "marseillaise",
  "What was the name of the first successful powered airplane?": "wright flyer",
  "Who was the leader of the Soviet Union during the Cold War?": "stalin",
  "What is the name of the famous ancient Greek philosopher who was the student of Plato and the teacher of Alexander the Great?": "aristotle",
  "Who was the first person to circumnavigate the globe?": "magellan",
  "What is the name of the famous Italian city known for its canals and gondolas?": "venice",
  "Who was the leader of the Soviet Union during the Cuban Missile Crisis?": "khrushchev",
  "What is the name of the famous prehistoric monument in England consisting of standing stones?": "stonehenge",
  "Who was the author of 'The Communist Manifesto'?": "marx",
  "What is the name of the famous ballet by Tchaikovsky about a young girl's Christmas dream?": "nutcracker",
  "Who was the famous American artist known for his paintings of soup cans and other consumer goods?": "warhol",
  "What is the name of the famous Renaissance artist known for painting the ceiling of the Sistine Chapel?": "michelangelo",
  "What is the smallest country in the world?": "vatican",
  "What is the capital city of Canada?": "ottawa",
  "What is the largest planet in our solar system?": "jupiter",
  "What is the atomic symbol for gold?": "au",
  "What is the formula for water?": "h2o",
  "What is the smallest particle of an element that retains the chemical properties of that element?": "atom",
  "What is the capital city of Switzerland?": "bern",
  "What is the smallest particle of an atom?": "electron",
  "What is the unit of measure for force?": "newton",
  "What is the study of plants called?": "botany",
  "What is the process by which plants make their own food called?": "photosynthesis",
  "What is the study of the structure of the body called?": "anatomy",
  "What is the largest organ in the human body?": "skin",
  "What is the branch of mathematics concerned with the study of space and properties that remain unchanged under certain transformations?": "geometry",
  "What is the formula for calculating the area of a circle?": "pi*r^2",
  "What is the study of the relationship between matter and energy called?": "physics",
  "What is the branch of mathematics that deals with the properties of numbers and their relationships?": "arithmetic",
  "What is the branch of chemistry concerned with the study of carbon-based compounds?": "organic chemistry",
  "What is the study of the earth and its features called?": "geography",
  "What is the study of the universe and its origins called?": "cosmology",
  "What is the process by which living organisms produce energy from food called?": "respiration",
  "What is the study of the behavior and interactions of matter and energy called?": "physics",
  "What is the distance light travels in one year called?": "light-year",
  "What is the study of the properties and behavior of matter called?": "chemistry",
  "What is the study of the function of living organisms and their parts called?": "physiology", 
  "add": None,
  "subtract": None, 
  "multiply": None, 
  "divide": None
}


availableCommands = {
   '/nv': 50, 
   '/ooh': 5, 
   '/playSound': 10, 
   '/box': 30, 
   '/boxall': 60, 
   '/spaz': 50, 
   '/spazall': 100, 
   '/inv': 40, 
   '/invall': 80, 
   '/tex': 20, 
   '/texall': 40, 
   '/freeze': 600, 
   '/freezeall': 1000, 
   '/sleep': 400, 
   '/sleepall': 800, 
   '/thaw': 500, 
   '/thawall': 700, 
   '/kill': 800, 
   '/killall': 1500, 
   '/end': 100, 
   '/hug': 60, 
   '/hugall': 100, 
   '/tint': 90, 
   '/sm': 50, 
   '/fly': 50, 
   '/flyall': 100, 
   '/heal': 500, 
   '/healall': 700, 
   '/gm': 200, 
   '/custom': 250
}

availableEffects = {
   'ice': 500, 
   'sweat': 750, 
   'scorch': 500, 
   'glow': 400, 
   'distortion': 750, 
   'slime': 500, 
   'metal': 500, 
   'surrounder': 1000
}
