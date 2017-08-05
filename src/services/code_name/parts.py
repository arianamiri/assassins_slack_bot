#todo put this in s3 not source code

adjectives = (
    'abandoned', 'able', 'absolute', 'academic', 'acceptable', 'acclaimed', 'accomplished', 'accurate', 'aching', 'acidic', 'acrobatic', 'active', 'actual', 'adept', 'admirable', 'admired', 'adolescent', 'adorable', 'adored', 'advanced', 'adventurous', 'affectionate', 'afraid', 'aged', 'aggravating', 'aggressive', 'agile', 'agitated', 'agonizing', 'agreeable', 'ajar', 'alarmed', 'alarming', 'alert', 'alienated', 'alive', 'all', 'altruistic', 'amazing', 'ambitious', 'ample', 'amused', 'amusing', 'anchored', 'ancient', 'angelic', 'angry', 'anguished', 'animated', 'annual', 'another', 'antique', 'anxious', 'any', 'apprehensive', 'appropriate', 'apt', 'arctic', 'arid', 'aromatic', 'artful', 'artistic', 'ashamed', 'assured', 'astonishing', 'athletic', 'atomic', 'attached', 'attentive', 'attractive', 'austere', 'authentic', 'authorized', 'automatic', 'avaricious', 'average', 'aware', 'awesome', 'awful', 'awkward',

    'back', 'bad', 'baggy', 'bare', 'barren', 'basic', 'basking', 'bearded', 'beautiful', 'beguiling', 'belated', 'beloved', 'beneficial', 'best', 'better', 'bewitched', 'big', 'big hearted', 'biodegradable', 'bite sized', 'bitter', 'black', 'bland', 'blank', 'blaring', 'bleak', 'blind', 'blissful', 'blond', 'blue', 'blushing', 'bogus', 'boiling', 'bold', 'bony', 'boring', 'bossy', 'both', 'bouncy', 'bountiful', 'bowed', 'brave', 'breakable', 'brief', 'bright', 'brilliant', 'brisk', 'broken', 'bronze', 'brown', 'bruised', 'bubbly', 'bulky', 'bumpy', 'buoyant', 'burdensome', 'burly', 'bustling', 'busy', 'buttery', 'buzzing',

    'calculating', 'calm', 'candid', 'canine', 'capital', 'carefree', 'careful', 'careless', 'caring', 'cautious', 'cavernous', 'celebrated', 'charming', 'cheap', 'cheerful', 'cheery', 'chief', 'chilly', 'chubby', 'circular', 'classic', 'clean', 'clear', 'clever', 'close', 'closed', 'clouded', 'cloudy', 'clueless', 'clumsy', 'cluttered', 'coarse', 'cold', 'colorful', 'colorless', 'colossal', 'comfortable', 'common', 'compassionate', 'competent', 'complete', 'complex', 'complicated', 'composed', 'concerned', 'concrete', 'confused', 'conscious', 'considerate', 'constant', 'content', 'conventional', 'cooked', 'cool', 'cooperative', 'coordinated', 'corny', 'corrupt', 'costly', 'courageous', 'courteous', 'crafty', 'crazy', 'creamy', 'creative', 'creepy', 'criminal', 'crisp', 'critical', 'crooked', 'crowded', 'cruel', 'crushing', 'cuddly', 'cultivated', 'cultured', 'cumbersome', 'curly', 'curvy', 'cute', 'cylindric',

    'damaged', 'damp', 'dangerous', 'dapper', 'daring', 'dark', 'darling', 'dazzling', 'dead', 'deadly', 'deafening', 'dear', 'dearest', 'decent', 'decimal', 'decisive', 'deep', 'defenseless', 'defensive', 'defiant', 'deficient', 'definite', 'definitive', 'delayed', 'delectable', 'delicious', 'delightful', 'delirious', 'demanding', 'dense', 'dental', 'dependable', 'dependent', 'descriptive', 'deserted', 'detailed', 'determined', 'devoted', 'different', 'difficult', 'digital', 'diligent', 'dim', 'dimpled', 'dimwitted', 'direct', 'dirty', 'disastrous', 'discrete', 'disfigured', 'disguised', 'disgusting', 'dishonest', 'disloyal', 'dismal', 'distant', 'distinct', 'distorted', 'dizzy', 'dopey', 'doting', 'double', 'downright', 'drab', 'drafty', 'dramatic', 'dreary', 'droopy', 'dry', 'dual', 'dull', 'dusky', 'dutiful', 'dynamic', 'dynamo',

    'eager', 'early', 'earnest', 'easy', 'ecstatic', 'edible', 'educated', 'elaborate', 'elastic', 'elated', 'elderly', 'electric', 'elegant', 'elementary', 'elliptical', 'embarrassed', 'embellished', 'eminent', 'emotional', 'empty', 'enchanted', 'enchanting', 'energetic', 'enlightened', 'enormous', 'enraged', 'entire', 'envious', 'equal', 'equatorial', 'essential', 'esteemed', 'ethical', 'euphoric', 'even', 'evergreen', 'everlasting', 'every', 'evil', 'exalted', 'excellent', 'excitable', 'excited', 'exciting', 'exemplary', 'exhausted', 'exotic', 'expensive', 'experienced', 'expert', 'extraneous', 'extroverted',

    'fabulous', 'failing', 'faint', 'fair', 'faithful', 'fake', 'false', 'familiar', 'famous', 'fancy', 'fantastic', 'far', 'fast', 'fat', 'fatal', 'fatherly', 'favorable', 'favorite', 'fearful', 'fearless', 'feisty', 'feline', 'female', 'feminine', 'few', 'fickle', 'filthy', 'fine', 'finished', 'firm', 'first', 'firsthand', 'fitting', 'fixed', 'flaky', 'flamboyant', 'flashy', 'flat', 'flawed', 'flawless', 'flickering', 'flimsy', 'flippant', 'flowery', 'fluffy', 'fluid', 'flustered', 'focused', 'fond', 'foolhardy', 'foolish', 'forceful', 'forked', 'formal', 'forsaken', 'forthright', 'fortunate', 'fragrant', 'frail', 'frank', 'frayed', 'free', 'frequent', 'fresh', 'friendly', 'frightened', 'frightening', 'frigid', 'frilly', 'frivolous', 'frizzy', 'front', 'frosty', 'frozen', 'frugal', 'fruitful', 'full', 'fumbling', 'functional', 'funny', 'fussy', 'fuzzy',

    'gargantuan', 'gaseous', 'general', 'generous', 'gentle', 'genuine', 'giant', 'giddy', 'gifted', 'gigantic', 'giving', 'glamorous', 'glaring', 'glass', 'gleaming', 'gleeful', 'glistening', 'glittering', 'gloomy', 'glorious', 'glossy', 'glowing', 'glum', 'golden', 'good', 'gorgeous', 'graceful', 'gracious', 'grand', 'grandiose', 'granular', 'grateful', 'grave', 'gray', 'great', 'greedy', 'green', 'gregarious', 'grim', 'grimy', 'gripping', 'grizzled', 'gross', 'grotesque', 'grouchy', 'grounded', 'growing', 'growling', 'grown', 'grubby', 'gruesome', 'grumpy', 'guilty', 'gullible', 'gummy',

    'hairy', 'half', 'handmade', 'handsome', 'handy', 'happy', 'hard', 'harmful', 'harmless', 'harmonious', 'harsh', 'hasty', 'hateful', 'haunting', 'healthy', 'heartfelt', 'hearty', 'heavenly', 'heavy', 'hefty', 'helpful', 'helpless', 'hidden', 'hideous', 'high', 'hilarious', 'hoarse', 'hollow', 'homely', 'honest', 'honorable', 'honored', 'hopeful', 'horrible', 'hospitable', 'hot', 'huge', 'humble', 'humiliating', 'humming', 'humongous', 'hungry', 'hurtful', 'husky',

    'icky', 'icy', 'ideal', 'idealistic', 'identical', 'idiotic', 'idle', 'idolized', 'ignorant', 'ill', 'illegal', 'illiterate', 'illustrious', 'imaginary', 'imaginative', 'immaculate', 'immaterial', 'immediate', 'immense', 'impartial', 'impassioned', 'impeccable', 'imperfect', 'imperturbable', 'impish', 'impolite', 'important', 'impossible', 'impractical', 'impressionable', 'impressive', 'improbable', 'impure', 'inborn', 'incomparable', 'incompatible', 'incomplete', 'inconsequential', 'incredible', 'indelible', 'indolent', 'inexperienced', 'infamous', 'infantile', 'infatuated', 'inferior', 'infinite', 'informal', 'innocent', 'insecure', 'insidious', 'insignificant', 'insistent', 'instructive', 'insubstantial', 'intelligent', 'intent', 'intentional', 'interesting', 'internal', 'international', 'intrepid', 'ironclad', 'irresponsible', 'irritating', 'itchy',

    'jaded', 'jagged', 'jam packed', 'jaunty', 'jealous', 'jittery', 'joint', 'jolly', 'jovial', 'joyful', 'joyous', 'jubilant', 'judicious', 'juicy', 'jumbo', 'jumpy', 'junior', 'juvenile',

    'kaleidoscopic', 'keen', 'key', 'kind', 'kindhearted', 'kindly', 'klutzy', 'knobby', 'knotty', 'knowing', 'knowledgeable', 'kooky', 'kosher',

    'lame', 'lanky', 'large', 'last', 'lasting', 'late', 'lavish', 'lawful', 'lazy', 'leading', 'leafy', 'lean', 'left', 'legal', 'legitimate', 'light', 'lighthearted', 'likable', 'likely', 'limited', 'limp', 'limping', 'linear', 'lined', 'liquid', 'little', 'live', 'lively', 'livid', 'loathsome', 'lone', 'lonely', 'long', 'long term', 'loose', 'lopsided', 'lost', 'loud', 'lovable', 'lovely', 'loving', 'low', 'loyal', 'lucky', 'lumbering', 'luminous', 'lumpy', 'lustrous', 'luxurious',

    'mad', 'magnificent', 'majestic', 'major', 'male', 'mammoth', 'married', 'marvelous', 'masculine', 'masked', 'massive', 'mature', 'meager', 'mealy', 'mean', 'measly', 'meaty', 'medical', 'mediocre', 'medium', 'meek', 'mellow', 'melodic', 'memorable', 'menacing', 'merry', 'messy', 'metallic', 'mild', 'milky', 'mindless', 'miniature', 'minor', 'minty', 'miserable', 'miserly', 'misguided', 'misty', 'mixed', 'modern', 'modest', 'moist', 'monstrous', 'monthly', 'monumental', 'moral', 'mortified', 'motherly', 'motionless', 'mountainous', 'muddy', 'muffled', 'multicolored', 'mundane', 'murky', 'mushy', 'musty', 'muted', 'mysterious',

    'naive', 'narrow', 'nasty', 'natural', 'naughty', 'nautical', 'near', 'neat', 'necessary', 'needy', 'negative', 'neglected', 'negligible', 'neighboring', 'nervous', 'new', 'next', 'nice', 'nifty', 'nimble', 'nippy', 'nocturnal', 'noisy', 'nonstop', 'normal', 'notable', 'noted', 'noteworthy', 'novel', 'noxious', 'numb', 'nutritious', 'nutty',

    'obedient', 'obese', 'oblong', 'obvious', 'occasional', 'odd', 'oddball', 'offbeat', 'offensive', 'official', 'oily', 'old', 'old fashioned', 'only', 'open', 'optimal', 'optimistic', 'opulent', 'orange', 'orderly', 'ordinary', 'organic', 'original', 'ornate', 'ornery', 'other', 'our', 'outgoing', 'outlandish', 'outlying', 'outrageous', 'outstanding', 'oval', 'overcooked', 'overdue', 'overjoyed', 'overlooked',

    'palatable', 'pale', 'paltry', 'parallel', 'parched', 'partial', 'passionate', 'past', 'pastel', 'peaceful', 'peppery', 'perfect', 'perfumed', 'periodic', 'perky', 'personal', 'pertinent', 'pesky', 'pessimistic', 'petty', 'phony', 'physical', 'piercing', 'pink', 'pitiful', 'plain', 'plaintive', 'plastic', 'playful', 'pleasant', 'pleased', 'pleasing', 'plump', 'plush', 'pointed', 'pointless', 'poised', 'poison', 'polished', 'polite', 'political', 'poor', 'popular', 'portly', 'posh', 'positive', 'possible', 'potable', 'powerful', 'powerless', 'practical', 'precious', 'present', 'prestigious', 'pretty', 'previous', 'pricey', 'prickly', 'primary', 'prime', 'pristine', 'private', 'prize', 'probable', 'productive', 'profitable', 'profuse', 'proper', 'proud', 'prudent', 'punctual', 'pungent', 'puny', 'pure', 'purple', 'pushy', 'putrid', 'puzzled', 'puzzling',

    'quaint', 'qualified', 'quarrelsome', 'quarterly', 'queasy', 'querulous', 'questionable', 'quick', 'quick witted', 'quiet', 'quintessential', 'quirky', 'quixotic', 'quizzical',

    'radiant', 'radiated', 'ragged', 'rapid', 'rare', 'rash', 'raw', 'ready', 'real', 'realistic', 'reasonable', 'recent', 'reckless', 'rectangular', 'red', 'reflecting', 'regal', 'regular', 'reliable', 'relieved', 'remarkable', 'remorseful', 'remote', 'repentant', 'repulsive', 'required', 'respectful', 'responsible', 'revolving', 'rewarding', 'rich', 'right', 'rigid', 'ringed', 'ripe', 'roasted', 'robust', 'rosy', 'rotating', 'rotten', 'rough', 'round', 'rowdy', 'royal', 'rubbery', 'ruddy', 'rude', 'rundown', 'runny', 'rural', 'rusty',

    'sad', 'safe', 'salty', 'same', 'sandy', 'sane', 'sarcastic', 'sardonic', 'satisfied', 'scaly', 'scarce', 'scared', 'scary', 'scented', 'scholarly', 'scientific', 'scornful', 'scratchy', 'scrawny', 'second', 'second hand', 'secondary', 'secret', 'self assured', 'self reliant', 'selfish', 'sentimental', 'separate', 'serene', 'serious', 'serpentine', 'several', 'severe', 'shabby', 'shadowy', 'shady', 'shallow', 'shameful', 'shameless', 'sharp', 'shimmering', 'shiny', 'shocked', 'shocking', 'shoddy', 'short', 'showy', 'shrill', 'shy', 'sick', 'silent', 'silky', 'silly', 'silver', 'similar', 'simple', 'simplistic', 'sinful', 'single', 'sizzling', 'skeletal', 'skinny', 'sleepy', 'slight', 'slim', 'slimy', 'slippery', 'slow', 'slushy', 'small', 'smart', 'smoggy', 'smooth', 'smug', 'snappy', 'snarling', 'sneaky', 'sniveling', 'snoopy', 'sociable', 'soft', 'soggy', 'solid', 'somber', 'some', 'sophisticated', 'sore', 'sorrowful', 'soulful', 'soupy', 'sour', 'sparkling', 'sparse', 'specific', 'spectacled', 'spectacular', 'speedy', 'spherical', 'spicy', 'spiffy', 'spirited', 'spiteful', 'splendid', 'spotless', 'spotted', 'spry', 'square', 'squeaky', 'squiggly', 'stable', 'staid', 'stained', 'stale', 'standard', 'starchy', 'stark', 'starry', 'steel', 'steep', 'sticky', 'stiff', 'stimulating', 'stingy', 'stormy', 'straight', 'strange', 'strict', 'strident', 'striking', 'striped', 'strong', 'studious', 'stunning', 'stupendous', 'stupid', 'sturdy', 'stylish', 'subdued', 'submissive', 'substantial', 'subtle', 'suburban', 'sudden', 'sugary', 'sunny', 'super', 'superb', 'superficial', 'superior', 'supportive', 'surprised', 'suspicious', 'svelte', 'sweaty', 'sweet', 'sweltering', 'swift', 'sympathetic',

    'talkative', 'tall', 'tame', 'tan', 'tangible', 'tart', 'tasty', 'tattered', 'taut', 'tedious', 'teeming', 'tempting', 'tender', 'tense', 'tepid', 'terrible', 'terrific', 'testy', 'thankful', 'thick', 'thin', 'third', 'thirsty', 'thorny', 'thorough', 'thoughtful', 'threadbare', 'thrifty', 'thunderous', 'tidy', 'tight', 'timely', 'tinted', 'tiny', 'tired', 'torn', 'total', 'tough', 'tragic', 'trained', 'traumatic', 'treasured', 'tremendous', 'triangular', 'tricky', 'trifling', 'trim', 'trivial', 'troubled', 'true', 'trusting', 'trustworthy', 'trusty', 'truthful', 'tubby', 'turbulent', 'twin',

    'ugly', 'ultimate', 'unacceptable', 'unaware', 'uncomfortable', 'uncommon', 'unconscious', 'understated', 'unequaled', 'uneven', 'unfinished', 'unfit', 'unfolded', 'unfortunate', 'unhappy', 'unhealthy', 'uniform', 'unimportant', 'unique', 'united', 'unkempt', 'unknown', 'unlawful', 'unlined', 'unlucky', 'unnatural', 'unpleasant', 'unrealistic', 'unripe', 'unruly', 'unselfish', 'unsightly', 'unsteady', 'unsung', 'untidy', 'untimely', 'untried', 'untrue', 'unused', 'unusual', 'unwelcome', 'unwieldy', 'unwilling', 'unwitting', 'unwritten', 'upbeat', 'upright', 'upset', 'urban', 'usable', 'used', 'useful', 'useless', 'utilized', 'utter',

    'vacant', 'vague', 'vain', 'valid', 'valuable', 'vapid', 'variable', 'vast', 'velvety', 'venerated', 'vengeful', 'verifiable', 'vibrant', 'vicious', 'victorious', 'vigilant', 'vigorous', 'villainous', 'violent', 'violet', 'virtual', 'virtuous', 'visible', 'vital', 'vivacious', 'vivid', 'voluminous',

    'warlike', 'warm', 'warmhearted', 'warped', 'wary', 'wasteful', 'watchful', 'waterlogged', 'watery', 'wavy', 'weak', 'wealthy', 'weary', 'webbed', 'wee', 'weekly', 'weepy', 'weighty', 'weird', 'welcome', 'well groomed', 'well off', 'well to do', 'well worn', 'wet', 'which', 'whimsical', 'whirlwind', 'whispered', 'white', 'whole', 'whopping', 'wicked', 'wide', 'wide eyed', 'wiggly', 'wild', 'willing', 'wilted', 'winding', 'windy', 'winged', 'wiry', 'wise', 'witty', 'wobbly', 'woeful', 'wonderful', 'wooden', 'woozy', 'wordy', 'worldly', 'worn', 'worried', 'worrisome', 'worse', 'worst', 'worthless', 'worthwhile', 'worthy', 'wrathful', 'wretched', 'writhing', 'wrong', 'wry',

    'yawning', 'yearly', 'yellow', 'yellowish', 'young', 'youthful', 'yummy',

    'zany', 'zealous', 'zesty', 'zigzag'
)


animals = (
    'aardvark', 'abyssinian', 'affenpinscher', 'airedale', 'akbash', 'akita', 'albatross', 'alligator', 'alpine', 'angel', 'angelfish', 'angora', 'ant', 'anteater', 'antelope', 'appenzeller', 'armadillo', 'avocet', 'axolotl',

    'baboon', 'bactrian', 'badger', 'balinese', 'bandicoot', 'bandit', 'barb', 'barn owl', 'barnacle', 'barracuda', 'bat', 'beagle', 'bear', 'beaver', 'bee-eater', 'beetle', 'binturong', 'bird', 'birman', 'bison', 'bloodhound', 'bluetick', 'boar', 'bobcat', 'bombay', 'bongo', 'bonobo', 'booby', 'boxer', 'budgerigar', 'buffalo', 'bull', 'bulldog', 'bullfrog', 'bumblebee', 'burmese', 'butterfly', 'buzzard',

    'caiman', 'camel', 'canaan', 'capuchin', 'capybara', 'caracal', 'carolina', 'cassowary', 'cat', 'caterpillar', 'catfish', 'cavalier', 'cavalry', 'centipede', 'chameleon', 'chamois', 'cheetah', 'chicken', 'chihuahua', 'chimpanzee', 'chin', 'chinchilla', 'chinook', 'chipmunk', 'chow', 'cichlid', 'civet', 'clam', 'clawed frog', 'clownfish', 'clumber', 'coati', 'cockroach', 'collie', 'coral', 'corgi', 'cottontop', 'cougar', 'cow', 'coyote', 'crab', 'crane', 'crocodile', 'cucumber', 'cuscus', 'cuttlefish',

    'dachsbracke', 'dachshund', 'dalmatian', 'darwin', 'deer', 'desert', 'devil', 'dhole', 'dingo', 'discus', 'dodo', 'dog', 'dogfish', 'dolphin', 'donkey', 'dormouse', 'dragon', 'dragonfly', 'drever', 'duck', 'dugong', 'dunker', 'dutchess',

    'eagle', 'earwig', 'echidna', 'eel', 'elephant', 'eleuth', 'elf', 'emperor', 'emu',

    'falcon', 'fennec', 'ferret', 'fish', 'flamingo', 'flounder', 'fly', 'forest', 'fossa', 'fousek', 'fowl', 'fox', 'foxhound', 'frigatebird', 'frise', 'frog', 'gar', 'gecko', 'gerbil', 'gharial', 'gibbon', 'gila', 'giraffe', 'glow-worm', 'goat', 'goose', 'gopher', 'gorilla', 'grasshopper', 'greyhound', 'grizzly', 'grouse', 'guppy',

    'hammerhead', 'hamster', 'hare', 'harrier', 'havanese', 'hedgehog', 'hercules', 'hermit', 'heron', 'highlander', 'himalayan', 'hippopotamus', 'honeybee', 'hornet', 'horse', 'hound', 'howler', 'human', 'hummingbird', 'husky', 'hyena', 'hyrax',

    'ibis', 'iguana', 'impala', 'indri', 'insect',

    'jackal', 'jaguar', 'javanese', 'jellyfish',

    'kakapo', 'kangaroo', 'kingfisher', 'kiwi', 'koala', 'komodo dragon', 'kudu',

    'labradoodle', 'ladybird', 'lemming', 'lemur', 'leopard', 'liger', 'lion', 'lionfish', 'lizard', 'llama', 'lobster', 'loon', 'lynx',

    'macaque', 'macaw', 'magpie', 'malamute', 'maltese', 'mammoth', 'manatee', 'mandrill', 'mantaray', 'mantis', 'mariner', 'markhor', 'marmoset', 'marsh', 'mastiff', 'mau', 'mayfly', 'meerkat', 'millipede', 'minke whale', 'mist', 'mole', 'molly', 'mongoose', 'mongrel', 'monitor', 'monkey', 'monster', 'moorhen', 'moose', 'moth', 'mountain', 'mouse', 'mule',

    'neanderthal', 'newfoundland', 'newt', 'nightingale', 'numbat',

    'ocelot', 'octopus', 'okapi', 'olm', 'opossum', 'orangutan', 'orca', 'oriole', 'ostrich', 'otter', 'owl', 'oyster',

    'pademelon', 'panda', 'panther', 'parrot', 'peacock', 'peccary', 'pekingese', 'pelican', 'penguin', 'persian', 'pheasant', 'pig', 'pika', 'pike', 'pinscher', 'piranha', 'platypus', 'pointer', 'poodle', 'porcupine', 'possum', 'prawn', 'puffer', 'puffin', 'pug', 'puma', 'pygmy',

    'quail', 'quetzal', 'quokka', 'quoll',

    'rabbit', 'raccoon', 'ragdoll', 'rat', 'rattlesnake', 'redwolf', 'reindeer', 'retriever', 'rhinoceros', 'robin', 'rocket', 'rockhopper', 'rottweiler',

    'sabre-tooth', 'saint', 'salamander', 'sand', 'saola', 'schnauzer', 'scorpion', 'sea lion', 'seadragon', 'seahorse', 'seal', 'serval', 'shark', 'sheep', 'sheepdog', 'shepherd', 'shrew', 'shrimp', 'siamese', 'siberian', 'skater', 'skunk', 'sloth', 'slug', 'snail', 'snake', 'snap', 'snowshoe', 'sparrow', 'spider', 'sponge', 'spoonbill', 'squid', 'squirrel', 'stag', 'starfish', 'stingray', 'stoat', 'sun', 'swan',

    'tamarin', 'tang', 'tapir', 'tarantula', 'tarsier', 'termite', 'terrier', 'tetra', 'thorn', 'tiger', 'toad', 'tortoise', 'toucan', 'tree toad', 'tropicbird', 'tuatara', 'turkey', 'turtle',

    'uakari', 'uguisu', 'umbrellabird', 'urchin',

    'vampire', 'vervet monkey', 'vole', 'vulture',

    'wallaby', 'walrus', 'warthog', 'wasp', 'weasel', 'whale', 'whippet', 'widow', 'wildebeest', 'wolf', 'wolfhound', 'wolverine', 'wombat', 'woodlouse', 'woodpecker', 'worm', 'wrasse', 'x-ray', 'yak', 'zebra', 'zebu', 'zonkey', 'zorse'
)
