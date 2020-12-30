import os
import random
import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = Bot(command_prefix='>')

hangman_full = (f'```\n________\n'
                f'|/    _|_\n'
                r"|    |x x|"
                f'\n'
                r'|    /[Y]\ '
                f'\n'
                r'|     / \ '
                f'\n'
                f'|_____```')

hangman0 = (f'```\n________\n'
            f'|/    \n'
            r"|    "
            f'\n'
            r'|      '
            f'\n'
            r'|      '
            f'\n'
            f'|_____```')

hangman1 = (f'```\n________\n'
            f'|/    _|_\n'
            r"|    |'-'|"
            f'\n'
            r'|      '
            f'\n'
            r'|      '
            f'\n'
            f'|_____```')

hangman2 = (f'```\n________\n'
            f'|/    _|_\n'
            r"|    |'-'|"
            f'\n'
            r'|     [Y] '
            f'\n'
            r'|       '
            f'\n'
            f'|_____```')

hangman3 = (f'```\n________\n'
            f'|/    _|_\n'
            r"|    |'-'|"
            f'\n'
            r'|    /[Y] '
            f'\n'
            r'|       '
            f'\n'
            f'|_____```')

hangman4 = (f'```\n________\n'
            f'|/    _|_\n'
            r"|    |'-'|"
            f'\n'
            r'|    /[Y]\ '
            f'\n'
            r'|       '
            f'\n'
            f'|_____```')

hangman5 = (f'```\n________\n'
            f'|/    _|_\n'
            r"|    |'-'|"
            f'\n'
            r'|    /[Y]\ '
            f'\n'
            r'|     /'
            f'\n'
            f'|_____```')


@bot.command(name='hm start', help='Starts a game of hangman.')
async def hangman_start():
    vocab = [('Abdicate', 'to step down from a position of power'),
             ('Abridge', 'to shorten, condense or lessen in length'), ('Absolve', 'to forgive or free from blame'),
             ('Abysmal', 'extremely wretched, bottomless'), ('Acquiesce', 'to comply passively, to give in'),
             ('Advocate', 'to support, or be in favor of'), ('Aesthetic', 'concerned with or appreciative of beauty'),
             ('Affinity', 'sympathy, attraction, kinship'), ('Agenda', 'program, things to be done'),
             ('Aggrandize', 'to make great'), ('Allusion', 'an indirect reference'),
             ('Altruistic', 'unselfish concern with the welfare of others'),
             ('Amnesty', 'an official pardon for a group of people who violate a law'),
             ('Animosity', 'ill will, active dislike'), ('Anomalous', 'irregular, abnormal, unusual'),
             ('Arduous', 'difficult to do, laborious'), ('Augment', 'to increase or enlarge'),
             ('Austere', 'stern in manner or appearance, strict in morals'),
             ('Aversion', 'strong or fixed dislike, a feeling of repugnance'),
             ('Banal', 'commonplace, trite, unoriginal'),
             ('Baroque', 'extravagantly ornate, flamboyant, characterized by bold ornamentation'),
             ('Begrudge', 'to envy another’s possessions, to concede reluctantly'),
             ('Benediction', 'a blessing, a good wish'), ('Benign', 'gentle, not harmful, kind'),
             ('Blanch', 'to turn pale'), ('Blithe', 'happily, lighthearted, joyful'),
             ('Botch', 'to bungle, to foul up'), ('Bracing', 'invigorating, to prepare'),
             ('Broach', 'to open up a subject for discussion'), ('Buffoon', 'clown or fool'),
             ('Bulwark', 'something used as a defense, a strong protection'),
             ('Cache', 'a hiding place, something hidden in a secret place'), ('Callous', 'unfeeling and insensitive'),
             ('Candor', 'truthfulness, great honesty, frankness'), ('Capitulate', 'to surrender, to stop resisting'),
             ('Catharsis', 'an emotional purification, an emotional release'), ('Caustic', 'biting in humor'),
             ('Censure', 'the act of blaming or condemning'), ('Chastise', 'to criticize severely'),
             ('Chronic', 'constant, lasting a long time'), ('Circumspect', 'careful, thought through'),
             ('Clemency', 'disposition towards mercy, mildness'), ('Clique', 'an exclusive group'),
             ('Coalesce', 'to come together as one, to fuse  or unite'),
             ('Coherent', 'making sense, organize and logical'),
             ('Colloquial', 'conversational, used in informal speech'), ('Compatible', 'able to get along well'),
             ('Convey', 'to transport, to conduct, to communicate'),
             ('Conviction', 'determination, a state of being convinced'), ('Copious', 'abundant, lavish'),
             ('Corroborate', 'to support with evidence'), ('Craven', 'cowardly'), ('Criterion', 'standard for judging'),
             ('Cursory', 'brief, without much attention to detail'), ('Dearth', 'a shortage'),
             ('Deference', 'respect, courtesy'), ('Deft', 'skillful'),
             ('Delineate', 'to describe or picture in words, to detail'),
             ('Delude', 'to deceive, to have false illusion'), ('Depravity', 'moral corruption'),
             ('Depreciate', 'to lessen in value, to belittle'), ('Desecrate', 'to treat with disrespect'),
             ('Destitute', 'very poor, totally lacking'), ('Diatribe', 'a denunciation, a biting speech'),
             ('Didactic', 'instructive, intended to educate'), ('Diffuse', 'wordy, not concentrated, to spread widely'),
             ('Digress', 'to stray from the main subject'), ('Discerning', 'keenly perceptive, shrewd'),
             ('Discount', 'to deduct, to disregard'),
             ('Diva', 'an opera singer, prima donna, a tempermental, conceited person'),
             ('Docile', 'easily tought, submissive'),
             ('Dogmatic', 'arrogantly assertive, positive about unproven ideas'),
             ('Dormant', 'as though asleep, not actively growing'), ('Dupe', 'to deceive, to trick'),
             ('Eccentric', 'nonconventional, a little kooky'), ('Eclectic', 'drawn from many sources'),
             ('Efface', 'to erase, to rub away the features, to obscure'), ('Egocentric', 'self-involved, selfish'),
             ('Egregious', 'extremely bad, flagrant'), ('Elucidate', 'to make clear'),
             ('Embellish', 'to add to, to exaggerate, garnish, ornament'),
             ('Emigrate', 'to move to a new country, to move to a new place'),
             ('Emissary', 'a messenger or representative, an agent'), ('Emulate', 'to imitate, to strive to equal'),
             ('Engaging', 'charming, interesting'), ('Enigma', 'a puzzle, a baffling situation, something obscure'),
             ('Enshroud', 'to cover, to enclose with a dark cover'), ('Esoteric', 'understood by only a few'),
             ('Eulogize', 'to speak in praise of someone, to pay written or spoken tribute'),
             ('Exacerbate', 'to make worse or more severe'),
             ('Exacting', 'greatly demanding, requiring close attention'), ('Exalt', 'to raise high, to glorify'),
             ('Exorbitant', 'extravagant, exceeding what is usual'),
             ('Expedite', 'to make faster or easier, to carry out promptly'),
             ('Explicit', 'clearly stated, precisely shown'), ('Expunge', 'to erase, to strike out'),
             ('Extol', 'to praise highly'), ('Facade', 'the principal front of a building, a false appearance'),
             ('Faction', 'a group, or part of large group, united on an issue'),
             ('Fallacy', 'false idea, mistaken belief, an implausible argument'),
             ('Fawning', 'to show excessive affection, to be overly flattering in return for favor'),
             ('Feign', 'to pretend, give a false impression, to invent falsely'),
             ('Fidelity', 'a state of being faithful, loyal'),
             ('Finesse', 'delicacy of workmanship, subtlety, skillful maneuvering'),
             ('Fledgling', 'a young bird learning to fly, a beginner, a novice'),
             ('Flourish', 'to grow strong, to grow abundantly, to thrive or prosper'),
             ('Fluke', 'a chance event, a coincidence, a stroke of luck'), ('Fodder', 'raw material for a given end'),
             ('Foray', 'an initial venture, to raid in search of plunder'),
             ('Forfeit', 'to give up something as a penalty for some error or crime'),
             ('Fortuitous', 'happening by chance, lucky fortunate'), ('Furtive', 'secret, done by stealth, sly'),
             ('Futile', 'useless, hopeless, without effect'),
             ('Galvanize', 'to arouse suddenly, to stimulate, spur to action'),
             ('Gamut', 'the full range of something'), ('Garner', 'to gather and store away, to acquire by effort'),
             ('Genteel', 'refined, polite, aristocratic'),
             ('Gratuitous', 'freely given, unnecessary, uncalled for, unwarranted'), ('Gravity', 'seriousness'),
             ('Grimace', 'to make an ugly disapproving facial expression'),
             ('Grovel', 'to beg persistently, to degrade oneself'), ('Guile', 'cunning duplicity, purposeful deceit'),
             ('Guise', 'an external appearance'), ('Gullible', 'easily deceived'),
             ('Harbinger', 'a precursor, an indication, one that foreshadows what is coming'),
             ('Herald', 'to give notice of, to hail or greet'),
             ('Heresy', 'any belief that is strongly opposed to established beliefs, or practice'),
             ('Hiatus', 'a break or interruption from work or any other established routine'),
             ('Homage', 'reverence, respect, an expression of high regard'),
             ('Homogeneous', 'similar, of the same kind, uniform in nature'),
             ('Hubris', 'excessive pride, arrogance, exaggerated self-confidence'),
             ('Hyperbole', 'extravagant exaggeration used as a figure of speech'),
             ('Immaterial', 'insignificant, unimportant'),
             ('Imminent', 'about to occur, hanging threatening over one’s head'),
             ('Immutable', 'something that is unchangeable, permanent'), ('Imperious', 'commanding, lordly, arrogant'),
             ('Impotent', 'lacking power, helpless, unable to perform sexual intercourse'),
             ('Incessant', 'unceasing, never ending, flowing without interruption'),
             ('Incipient', 'beginning to be, in an early stage'),
             ('Incontrovertible', 'not disputable, not open to question'),
             ('Indigenous', 'native, produced or living in a particular area'), ('Indigent', 'poverty stricken, needy'),
             ('Inept', 'clumsy, awkward, incompetent'),
             ('Infamy', 'an evil reputation borne of a criminal act, a reputation for evildeeds'),
             ('Inhibit', 'to keep from free activity or expression, to restrain or even forbid'),
             ('Insidious', 'sly, treacherous, having a gradual effect'), ('Insipid', 'lacking taste, dull, bland'),
             ('Intrepid', 'fearless, having fortitude and endurance'),
             ('Irreverent', 'disrespectful, gently or humorously mocking'),
             ('Jargon', 'a specialized vocabulary of a group, an obscure language'), ('Jaunt', 'a short pleasure trip'),
             ('Jeopardy', 'exposure to danger, peril'), ('Judicious', 'wise, showing judgment, cautious'),
             ('Junction', 'a place of meeting or joining, a linkup'), ('Juxtapose', 'to place side by side'),
             ('Karma', 'a good or bad emanation of force from someone or something'),
             ('Laconic', 'brief in speech, using very few words'), ('Lament', 'to mourn, to express regret'),
             ('Latent', 'present but not visible or apparent, dormant, potential'),
             ('Laud', 'to praise, to applaud, to extol'), ('Legacy', 'something handed down from the past, a bequest'),
             ('Levity', 'lack of seriousness, frivolity'),
             ('Liaison', 'connection between different groups, a close bond'),
             ('Listless', 'a lack of energy, spiritless'), ('Lucid', 'clear, easily understood'),
             ('Luminous', 'glowing, bright, emitting light'), ('Magnanimous', 'noble in spirit, generous, giving'),
             ('Malaise', 'a feeling of depression, uneasiness, of being unwell'),
             ('Manifest', 'to make evident by showing'),
             ('Marshal', 'to gather together something for a purpose, to arrange in order'),
             ('Martyr', 'one who suffers for a cause, a person who sacrifices for a principle'),
             ('Maverick', 'a person who breaks away from the crowd, a non conformist'),
             ('Meander', 'to wander aimlessly'),
             ('Mercenary', 'a person who serves only for money, motivated by greed'),
             ('Moot', 'of no matter or consequence, not important'),
             ('Morose', 'gloomy, bad tempered, a sullen disposition'),
             ('Myriad', 'an immense indefinite number, multitude'), ('Negligent', 'careless, remiss'),
             ('Nemesis', 'a powerful river, a usually unconquerable opponent'),
             ('Nomadic', 'without a permanent home, constantly wandering'), ('Nominal', 'insignificant, trifling'),
             ('Novel', 'new, original'), ('Nuance', 'a subtle distinction, a slight difference in definition'),
             ('Nullify', 'to repeal, cancel, render void'), ('Obliterate', 'to blot out leaving no traces, to destroy'),
             ('Obscure', 'unclear, vague partially hidden, hard to understand'),
             ('Obviate', 'to make unnecessary, to avert, to preclude'), ('Odious', 'hateful, evil, vile'),
             ('Odyssey', 'a long difficult journey marked by changes in fortune'),
             ('Ogle', 'to stare at in a disrespectful way'),
             ('Oligarchy', 'a government in which the power is in the hand of only a few'),
             ('Opaque', 'difficult to see through, unclear, dark'),
             ('Opportunist', 'a person who takes advantage of opportunity with no regard for principle'),
             ('Osmosis', 'gradual or subtle absorption, an unconscious process of absorption'),
             ('Oust', 'to eject, to banish, to expel'), ('Overture', 'an opening move, a preliminary offer'),
             ('Palatable', 'pleasant to the taste, agreeable in feeling'),
             ('Paltry', 'a tiny or insignificant amount, meager, scant'), ('Pariah', 'an outcast'),
             ('Partition', 'a dividing wall, a division'), ('Paucity', 'scarcity, smallness in number or amount'),
             ('Pedantic', 'boringly, scholarly, academic in mode'),
             ('Penchant', 'a strong like for something, a predilection'),
             ('Permeate', 'to spread or seep through, to penetrate, to pervade'),
             ('Peruse', 'to study, to read over leisurely'),
             ('Philanthropy', 'good will towards all people, love of mankind, and act of generosity'),
             ('Pious', 'reverent, devout, dutiful, may at times be marked by hypocrisy'),
             ('Pique', 'to hurt or rile the feelings of someone, irritate'),
             ('Pivotal', 'crucial, something around which things turn'),
             ('Placate', 'to soothe, to appease with concessions'), ('Plausible', 'believable'),
             ('Poignant', 'emotionally moving'), ('Polemic', 'a powerful argument to defend a thesis'),
             ('Precept', 'a rule or principle to guide conduct'),
             ('Preclude', 'to make impossible, to shut out, to bar'),
             ('Pretentious', 'showy, self-important, make unjustifiable claims to excellence'),
             ('Prolific', 'marked by abundant production or offspring'),
             ('Prosaic', 'dull, unimaginative, lacking excitement'),
             ('Provincial', 'limited in outlook, narrow in ideas'), ('Prudent', 'careful, cautious'),
             ('Quaint', 'pleasantly old-fashioned, picturesque'), ('Quell', 'to put an end to, to squelch, to calm'),
             ('Quintessential', 'the most perfect example of'), ('Quixotic', 'foolishly impractical and idealistic'),
             ('Raucous', 'boisterous, harsh sounding, noisy and disorderly'),
             ('Rebuff', 'to snub, to refuse in a blunt or rude way'), ('Rebuke', 'to criticize or reprimand sharply'),
             ('Reciprocal', 'mutual, shared, interchangeable'),
             ('Relegate', 'to dismiss to a less prominent position, to banish'),
             ('Relic', 'an object associated with a saint, something that remains from the past'),
             ('Replenish', 'to refill, to supply once more'), ('Reprehensible', 'deserving of blame'),
             ('Reprove', 'to gently criticize'), ('Rescind', 'to cancel, to repeal'),
             ('Resilient', 'an ability to recover from, or adjust easily'),
             ('Respite', 'an interval of rest, a temporary delay'), ('Resplendent', 'brilliant, gloriously bright'),
             ('Robust', 'strong and healthy, vigorous'), ('Rustic', 'primitive, rural, lacking city comforts'),
             ('Saccharine', 'excessively sweet'), ('Sardonic', 'disdainful, scornfully mocking'),
             ('Scanty', 'minimal, hardly sufficient'),
             ('Scintillate', 'to sparkle, to gleam, to be animated or brilliant'),
             ('Servile', 'submissive, behaving like a slave'), ('Sloth', 'sluggish, laziness, indolence'),
             ('Spurious', 'false, fake, not genuine'), ('Stagnate', 'to lie inactive, to stay in one place'),
             ('Static', 'stationary, not changing or moving'), ('Steadfast', 'loyal, faithful'),
             ('Stoic', 'showing indifference to pain, apathetic'), ('Stratagem', 'a trick or deceptive scheme'),
             ('Strident', 'loud, harsh, grating'), ('Stymie', 'to get in the way of, to hinder, to block'),
             ('Succinct', 'concise, clearly expressed with a few words'), ('Surfeit', 'abundance, excessive amount'),
             ('Surmise', 'a thought or idea based on scanty evidence'), ('Table', 'to remove from consideration'),
             ('Tedious', 'boring, tiresome'), ('Teem', 'to swarm, to be inundated, to become full to overflowing'),
             ('Temperance', 'habitual moderation, the avoidance of excess'),
             ('Tenet', 'a principle, doctrine or belief held as so by a group'),
             ('Tentative', 'uncertain, temporary not fully worked out'), ('Tenuous', 'flimsy'),
             ('Tepid', 'lukewarm, unenthusiastic, halfhearted'), ('Terse', 'concise, brief, free of extra word'),
             ('Theology', 'the study of god or religion'),
             ('Thwart', 'to prevent from being accomplished, to frustrate, to hinder'),
             ('Tirade', 'a long and angry speech'), ('Tonic', 'a refreshing drink, something that invigorates'),
             ('Tortuous', 'winding, twisting, full of curves'), ('Tout', 'to brag publicly, to praise highly'),
             ('Transfix', 'to cause to stand motionless with awe or other intense emotion'),
             ('Travesty', 'a parody, an imitation that makes crude fun of something'),
             ('Trite', 'unoriginal, overused, clichéd, commonplace'), ('Trivial', 'unimportant, insignificant'),
             ('Tryst', 'a secret meeting of lovers'), ('Tumult', 'noisy commotion, uproar'),
             ('Turpitude', 'shameful wickedness, evil, depravity'),
             ('Undermine', 'to weaken the support of, to injure in a slow or sneaky way'),
             ('Unilateral', 'on one side alone'), ('Urbane', 'suave, sophisticated, polished'),
             ('Usurp', 'to size wrongfully'), ('Vapid', 'tasteless, dull'),
             ('Vehement', 'intense, forceful marked by strong feeling'), ('Verbose', 'wordy'),
             ('Vestige', 'the remains of something that no longer exists'),
             ('Viable', 'workable, capable of living and growing, able to succeed'),
             ('Vilify', 'to defame, to slander, to blacken the character of'),
             ('Virulent', 'extremely poisonous, malignant, full of hate'), ('Vivacious', 'lively, spirited'),
             ('Volatile', 'explosive, tend to burn quickly'),
             ('Wanton', 'immoral, lewd, deliberate maliciousness, having no regards for others'),
             ('Waver', 'to be indecisive or inconstant, to fluctuate in opinion'),
             ('Winsome', 'charming, sweetly engaging'), ('Wistful', 'yearning, sad longing, a gentle desire'),
             ('Zealot', 'a person with great enthusiasm for and commitment to a cause'),
             ('Zenith', 'the highest point'), ('Abeyance', 'a temporary suspension of activity'),
             ('Abrogate', 'to repeal, to set aside, to nullify'), ('Abscond', 'to leave quickly and secretively'),
             ('Abstinence', 'voluntarily refraining from eating certain foods or drink'),
             ('Abstruse', 'hard to understand or grasp'), ('Accolade', 'award or honor, high praise'),
             ('Accouterments', 'personal clothing, accessories, or equipment'),
             ('Acquit', 'to find not guilty, to conduct oneself'),
             ('Adjure', 'to command or urge solemnly and earnestly'),
             ('Adumbrate', 'to suggest partly, to give a hint of things to come'), ('Aegis', 'protection, patronage'),
             ('Aggrieve', 'to distress, to mistreat'), ('Akimbo', 'having one’s hands in a bent position on the hips'),
             ('Alacrity', 'cheerful readiness, liveliness or eagerness'),
             ('Alchemy', 'a process of transformation that is seemingly magical'),
             ('Ambulatory', 'able to walk or move about'), ('Ameliorate', 'to make better, to ease or improve'),
             ('Anathema', 'something or someone loathed or intensely dislike'),
             ('Ancillary', 'subsidiary, subordinate'),
             ('Anomie', 'instability caused by an erosion of value or lack of purpose'),
             ('Antipodal', 'situated on opposite side of the earth or being exactly opposite'),
             ('Apocryphal', 'false, spurious, of doubtful origin'),
             ('Apoplexy', 'a stroke resulting from loss of blood of the brain'),
             ('Apostasy', 'a judge, one who decides'), ('Ascetic', 'hermitlike, self-denial, austere'),
             ('Assiduous', 'hardworking, busy, diligent'),
             ('Assignation', 'a secret meeting, a tryst, or something assigned'),
             ('Bacchanal', 'a drunken reveler or orgy'),
             ('Bandy', 'to toss and forth, to exchange, to use in a glib way'),
             ('Bathos', 'a transition from the illustrious to the commonplace, overdone pathos'),
             ('Behemoth', 'something that is enormous, or monstrous in size and power'),
             ('Belie', 'to run counter to, to show something as false'),
             ('Besmirch', 'to stain or soil (commonly as to reputation)'), ('Bilious', 'ill-tempered, cranky, angry'),
             ('Bivouac', 'a temporary encampment'), ('Bon vivant', 'someone who enjoys luxurious living'),
             ('Bowdlerize', 'to censor prudishly'), ('Brook', 'to tolerate, to put up with something'),
             ('Bumptious', 'pushy, conceited, noisily self-assertive'),
             ('Byzantine', 'extremely intricate or complicated in structure'),
             ('Cabal', 'a secret group of conspirators, a clique'),
             ('Cachet', 'a mark of distinction, a quality that “says” prestige'),
             ('Calumny', 'slander, deliberate false statements'), ('Capricious', 'whimsical, fanciful, impulsive'),
             ('Castigate', 'to punish, chastise, criticize severely'),
             ('Cataclysm', 'a violent upheaval, an earthquake, a flood'),
             ('Cavil', 'to quibble, to raise trivial objections'), ('Chary', 'careful, cautious, wary'),
             ('Chicanery', 'deception or trickery'), ('Chimerical', 'wildly fanciful, absurd'),
             ('Circumlocution', 'wordy language, an indirect, roundabout expression'),
             ('Clout', 'influence, a forceful blow'), ('Cogitate', 'to ponder over, to mediate, to think'),
             ('Comport', 'to behave'), ('Compunction', 'remorse, feeling uneasy after having done something'),
             ('Concomitant', 'accompanying, attending, going along with'),
             ('Conflagration', 'a large, disastrous fire'), ('Contentious', 'argumentative over a point, quarrelsome'),
             ('Cortege', 'a procession, a group of attendants'),
             ('Coterie', 'an intimate group of people with a common interest'), ('Covet', 'to wish for with envy'),
             ('Debacle', 'a disaster or violent breakdown'), ('Decimate', 'to kill or destroy a large part of'),
             ('Deleterious', 'harmful'), ('Depredate', 'to prey upon, to plunder with violence if necessary'),
             ('Descry', 'to discern, to see something, to teach sight of'), ('Desiccate', 'to dry out'),
             ('Dichotomy', 'division into two often contradictory parts'),
             ('Dilettante', 'a dabbler, someone with a superficial knowledge (usually of the arts)'),
             ('Discomfit', 'to confuse, deceive'), ('Disquiet', 'to make uneasy'),
             ('Dissipate', 'to break up, to squander, to indulge excessively in sensual pleasure'),
             ('Diurnal', 'occurring during the day, happens everyday'),
             ('Doff', 'to take off (usually clothing) as a sign of greeting'),
             ('Doggerel', 'comic, sometimes crude, informal verse'),
             ('Dossier', 'a file of documents, letters and records'), ('Draconian', 'severe, exceedingly harsh'),
             ('Dulcet', 'having a nice, agreeable, melodious sound'),
             ('Effete', 'exhausted, lost vitality, over refined'), ('Elan', 'vigor, distinctive, elegant style'),
             ('Elliptical', 'oval, obscure in expression'), ('Encomium', 'a eulogy or expression of high praise'),
             ('Endemic', 'native, belonging to a specific region'), ('Enervate', 'to weaken, to sap the strength'),
             ('Ennui', 'boredom, listlessness, lack of interest'),
             ('Ensconce', 'to settle in snugly, to hide in a secure place'), ('Ersatz', 'an inferior substitute'),
             ('Erudite', 'scholarly, deeply learned, well read'), ('Espy', 'to glimpse, to descry, to catch sight of'),
             ('Ethnocentric', 'the belief in the superiority of one’s race or ethnic group'),
             ('Evanescent', 'vanishing, happening for the briefest moment'),
             ('Exemplar', 'an excellent model, a typical example'), ('Exigent', 'urgent, demands prompt action'),
             ('Extirpate', 'to rip up by the roots, to abolish, to annihilate'),
             ('Facetious', 'humorous, joking in a somewhat inappropriate or clumsy manner'), ('Fauna', 'animals'),
             ('Feckless', 'lacking responsibility, ineffective'), ('Fecund', 'fertile, productive, fruitful'),
             ('Feral', 'wild, like a wild animal, savage'), ('Fetter', 'to impede, restrain, hamper'),
             ('Flagellate', 'to whip, or to punish as if by whipping'), ('Foment', 'to stir up, to incite'),
             ('Forswear', 'retract, renounce or recant'), ('Fusillade', 'a rapid outburst, spray of gunfire'),
             ('Gainsay', 'to deny, to speak or act against'),
             ('Gamin', 'a street urchin, a slim girl with an impish charm'), ('Garrulous', 'talkative'),
             ('Gerrymander', 'to divide into election districts to gain political advantage'),
             ('Gestalt', 'a structure, whose parts cannot stand alone'),
             ('Gesticulate', 'to gesture, especially when speaking'), ('Gird', 'to invest with authority, to brace'),
             ('Halitosis', 'bad breath'), ('Hidebound', 'excessively rigid, dry and stiff, inflexible'),
             ('Histrionic', 'overly dramatic, theatrical, deliberately affected'),
             ('Hoary', 'gray or white with age, ancient, stale'), ('Homeopathy', 'a system of natural healing'),
             ('Husbandry', 'the judicious used of resources, livestock farming'),
             ('Ignominious', 'disgraceful and dishonorable'),
             ('Imbroglio', 'a difficult and confused situation, a complicated disagreement'),
             ('Impecunious', 'without money, penniless'),
             ('Impervious', 'does not allow something to pass through, impenetrable'),
             ('Impugn', 'to attack the integrity of something'),
             ('Implacable', 'not capable of being appeased or mollified'),
             ('Inchoate', 'just beginning, not organized or orderly, incomplete'), ('Iniquitous', 'evil, unjust'),
             ('Insouciant', 'nonchalant, lighthearted, unconcerned'),
             ('Interregnum', 'the period between two successive governments'),
             ('Intransigent', 'uncompromising, stubborn'), ('Inveterate', 'habitual, deeply rooted or established'),
             ('Irascible', 'hot-tempered, cranky'), ('Itinerant', 'moving from place to place'),
             ('Juggernaut', 'a massive, unstoppable object'),
             ('Junta', 'a small group that rules a country after a coup d’etat'),
             ('Largess', 'a generous giving of gifts, philanthropy'),
             ('Lassitude', 'a weariness, listlessness, a state of lethargy'),
             ('Leitmotif', 'a dominant or recurring theme or emotion'),
             ('Levee', 'an embankment designed to prevent a river from flooding'),
             ('Libation', 'a pouring of a liquid for a religious ceremony, a drink'),
             ('Libidinous', 'lustful, lascivious'), ('Lope', 'to run at steady, easy pace'),
             ('Macerate', 'to soften by soaking, to cause to waste away'),
             ('Machination', 'scheming activity foe an evil purpose'),
             ('Malapropism', 'the humorous misuse of a word that sound very much like the word intended'),
             ('Malfeasance', 'an illegal act especially by a public official'),
             ('Martinet', 'one who adheres strictly to rules'),
             ('Matriculate', 'to enroll, most particularly in college'), ('Maudlin', 'overly sentimental'),
             ('Mellifluous', 'sweetly flowing'), ('Mendacious', 'dishonest, deceitful'),
             ('Mercurial', 'emotionally unpredictable, give to rapid changes in mood'),
             ('Miasma', 'a poisonous swamp vapor, a harmful influence or atmosphere'),
             ('Milieu', 'environment, surroundings'), ('Mirthful', 'merry, gleeful'),
             ('Mordant', 'bitingly sarcastic, incisive, caustic in manner'),
             ('Moribund', 'being in a dying or decaying condition'), ('Muckrake', 'to expose political misconduct'),
             ('Munificent', 'generous'), ('Myopia', 'nearsightedness, lacking foresight'),
             ('Nabob', 'a wealthy, influential person'), ('Nascent', 'coming into existence, being born'),
             ('Neophyte', 'a beginner, a novice'),
             ('Nepotism', 'showing favoritism to friends or family, as in granting positions in jobs or politics'),
             ('Niggardly', 'stingy, small in a mean way'),
             ('Nihilism', 'the belief that there are no values or morals in the universe'),
             ('Nirvana', 'a blissful, painless state'), ('Noisome', 'harmful, unwholesome, stinking, putrid'),
             ('Nonplus', 'to bewilder, to puzzle'), ('Obdurate', 'stubborn'),
             ('Obsequious', 'fawning, subservient, servile'), ('Oeuvre', 'a work of art, the sum of an artist’s work'),
             ('Officious', 'unnecessarily helpful, meddlesome, interfering'),
             ('Omniscient', 'all knowing, infinite awareness'),
             ('Omnivorous', 'eating or absorbing everything, feeding on both animal and vegetable substances'),
             ('Onerous', 'burdensome, oppressive, troublesome'), ('Onus', 'burden, blame, obligation'),
             ('Opprobrious', 'damning, extremely critical, disgraceful'),
             ('Opus', 'a creative work, musical composition'), ('Oscillate', 'to swing back and forth'),
             ('Ossify', 'to become rigid, to be come set in one’s ways'),
             ('Palliate', 'to hide the seriousness of something with excuses or apologies'),
             ('Pallid', 'lacking color, wan'), ('Panacea', 'a remedy that cures everything'),
             ('Panegyric', 'lofty praise, eulogistic writing'), ('Paradigm', 'a model or example'),
             ('Parsimonious', 'stingy'), ('Patina', 'surface discoloration caused by age and oxidation'),
             ('Patois', 'a language used by a particular population that differs from standard speech'),
             ('Penultimate', 'next to last'), ('Penury', 'extreme poverty'),
             ('Peregrination', 'an expedition, wandering'), ('Perfidious', 'faithless, untrustworthy'),
             ('Perfunctory', 'careless, unenthusiastic, done merely as duty'),
             ('Perorate', 'to make a long, formal speech, to sum up a speech'),
             ('Perquisite', 'a privilege or perk that goes along with a job'),
             ('Perspicacious', 'shrewd, astute, showing strong powers of discernment'),
             ('Petulant', 'cranky, ill tempered, irritable, peevish'), ('Phantasm', 'an apparition, phantom'),
             ('Phlegmatic', 'calm, indifferent, not easily aroused'), ('Piquant', 'pungent, charmingly provocative'),
             ('Placebo', 'a fake medication'), ('Plebeian', 'common, vulgar, low class'),
             ('Pluralism', 'a society in which distinct group function together, but retain their identities'),
             ('Portent', 'an omen, a sign of something coming, a foreshadowing'),
             ('Pregnant', 'highly significant, overflowing, rich in significance'),
             ('Prepossess', 'to cause to be preoccupied, to influence, positively, in advance'),
             ('Prescient', 'having foresight'), ('Prevaricate', 'to deviate from the truth'),
             ('Privation', 'lack of comforts, poverty, a state of being deprived'), ('Probity', 'honesty, uprightness'),
             ('Profligate', 'corrupt, degenerate, wildly extravagant'),
             ('Propinquity', 'nearness in place or time, kinship'),
             ('Protean', 'readily assuming different shapes or characters'),
             ('Provenance', 'origin, source, proof of posting ownership'),
             ('Prowess', 'exceptional skill or strength, military valor'),
             ('Prurient', 'lascivious, have lustful thoughts or desires'), ('Puissance', 'power, strength'),
             ('Punctilious', 'meticulously attentive to detail, exacting'), ('Putrefy', 'to rot'),
             ('Quiescence', 'state of rest or inactivity'),
             ('Raffish', 'jaunty, sporty, disreputable, vulgar, characterized by a careless'),
             ('Unconventionality', 'originality, the ability to think and act independently'),
             ('Rapprochement', 'a re-establishment of good relations'),
             ('Rarefied', 'esoteric, interesting to only a few'),
             ('Recalcitrant', 'stubbornly defiant and resistant of authority'),
             ('Recidivism', 'the act of repeating an offense'),
             ('Recondite', 'hard to understand, abstruse, over one’s head'),
             ('Redoubtable', 'formidable, fearsome, deserving of respect'), ('Remuneration', 'payment, recompense'),
             ('Repartee', 'a quick, witty reply, spirited conversation'),
             ('Reprobate', 'a morally unprincipled person, a scoundrel'),
             ('Reticent', 'restrained, reluctant, uncommunicative'), ('Ribald', 'vulgar or indecent language'),
             ('Rife', 'widespread, abounding, occurring frequently'),
             ('Rout', 'to put to flight, to scatter, to cause a huge defeat'), ('Rubric', 'heading, title, category'),
             ('Ruminate', 'to muse upon'), ('Sagacious', 'wise shrewd'), ('Sallow', 'a sickly, greenish-yellow tone'),
             ('Sally', 'a rushing attack, witty repartee, a brief excursion'), ('Salubrious', 'favorable to health'),
             ('Sangfroid', 'extraordinary composure in the face of danger'),
             ('Sartorial', 'relating to dress or fashion'), ('Saturnine', 'sullen, gloomy, depressed'),
             ('Savant', 'a scholar, a very knowledgeable person'),
             ('Scofflaw', 'one who is continually breaking the law'), ('Scotch', 'to put an end to'),
             ('Secrete', 'to give off, to conceal'),
             ('Sententious', 'preachy, pompous, using wise sayings excessively'),
             ('Shibboleth', 'a distinctive word or behavior that typifies a group, a slogan'),
             ('Simper', 'to smile foolishly'), ('Sine qua non', 'something that is an essential condition of'),
             ('Sinuous', 'winding, having many curves'), ('Slatternly', 'squalid, a slovenly woman'),
             ('Somnolent', 'drowsy, sleepy'), ('Spate', 'a sudden outburst'), ('Spelunker', 'a cave explorer'),
             ('Stalwart', 'unwavering, robust, sturdily built'), ('Striated', 'marked with thin lines or grooves'),
             ('Sturm and drang', 'turmoil'), ('Sui generis', 'unique, of its own kind, in a class by itself'),
             ('Supercilious', 'arrogant, overbearing, condescending'), ('Surreptitious', 'sneaky, secret'),
             ('Sycophant', 'a flatterer, a self-serving yes-man'),
             ('Syllogism', 'a form oflogic in which major and minor premises are made and a conclusion drawn'),
             ('Sylvan', 'forestlike, wooded'),
             ('Synergy', 'the combined force of two distinct elements that is more powerful then each alone'),
             ('Temerity', 'boldness, rashness, audacity'),
             ('Temporize', 'to compromise, to draw something out in order to gain time'),
             ('Tendentious', 'advancing a point of view, biased'), ('Timorous', 'fearful, easily frightened'),
             ('Titular', 'in title only'), ('Toothsome', 'tasty, sexually attractive, luscious'),
             ('Trice', 'an moment, a short period of time'), ('Truculent', 'hostile, aggressive, savage'),
             ('Umbrage', 'displeasure or resentment, shade'), ('Undulate', 'to move smoothly in a wavelike manner'),
             ('Usury', 'lending money at a high interest rate'), ('Vacuous', 'empty, lacking intelligence'),
             ('Vagary', 'whim, an unpredictable action'), ('Vainglorious', 'boastful, pompous'),
             ('Veneer', 'façade, coating, outward appearance'), ('Venerate', 'to honor, to worship, to respect'),
             ('Veracious', 'truthful, honest'), ('Verdant', 'covered with green plants, leafy'),
             ('Vicarious', 'acting for another, sharing in an experience of another through the imagination'),
             ('Viscosity', 'a thick or sticky consistency of a liquid'),
             ('Vitriolic', 'corrosive, biting, bitterly scathing'), ('Wastrel', 'someone who wastes, a spendthrift'),
             ('Wizened', 'shriveled, withered'), ('Wont', 'custom, habit'), ('Zaftig', 'full-figured, plump'),
             ('Zeitgeist', 'the mood or spirit of the times'), ('Zephyr', 'a gentle breeze'),
             ('Ablution', 'the act of washing one’s body'), ('Abnegate', 'to deny to oneself, renounce, surrender'),
             ('Acidulous', 'sour, ill tempered'), ('Adventitious', 'accidental'),
             ('Afflatus', 'a creative impulse, divine inspiration'),
             ('Agathism', 'the belief that things ultimately lead to good'),
             ('Agnate', 'from the father’s side of the family'), ('Aleatory', 'based on chance'),
             ('Animus', 'hostile feeling'), ('Antediluvian', 'extremely old, antiquated'),
             ('Antinomy', 'a contradiction between two seemingly true statements'), ('Aphasia', 'loss of speech'),
             ('Aphorism', 'a wise saying'), ('Arable', 'suitable for the growing of crops'),
             ('Arrant', 'notoriously without moderation, downright'), ('Arriviste', 'a social climber, an upstart'),
             ('Aseptic', 'surgically clean, free of germs'), ('Atrabilious', 'inclined to melancholy'),
             ('Bailiwick', 'a particular area of expertise'), ('Banausic', 'routine, mechanical, boring'),
             ('Bellwether', 'a person who assumes a leadership role or takes initiative'),
             ('Benison', 'blessing, benediction'),
             ('Bibulous', 'highly absorbent, given to or fond of alcoholic beverages'),
             ('Bifurcated', 'forked, divided into two branches'),
             ('Boondoggle', 'a useless or valueless project or activity'),
             ('Bosky', 'wooded, covered with trees and shrubs'), ('Braggadocio', 'arrogant pretension, empty conceit'),
             ('Brummagem', 'bogus, fraudulent, cheap, showy'),
             ('Caducity', 'the frailty of old age, the quality of being perishable transitoriness'),
             ('Canard', 'a fabricated story, or sensational report, a hoax'),
             ('Celerity', 'haste, swiftness of movement'),
             ('Centrifugal', 'proceeding in action away from the center or axle'),
             ('Claque', 'an audience paid to clap, an obsequious audience'), ('Clerisy', 'the intellectual elite'),
             ('Compendium', 'a comprehensive summary'), ('Culvert', 'a sewer or drain'),
             ('Daedal', 'ingenious or complex in design'),
             ('Deciduous', 'shedding or losing leaves on a particular season, not evergreen'),
             ('Defalcate', 'to embezzle'), ('Defenestration', 'the act of throwing someone or something out a window'),
             ('Deism', 'the belief that god created the world and then left it to its own devices'),
             ('Demimonde', 'a class of kept women or women of lower social standing'), ('Denouement', 'the outcome'),
             ('Denunciation', 'open condemnation'), ('Diadem', 'a crown that indicates royalty'),
             ('Dolorous', 'sorrowful'), ('Eclat', 'a dazzling success, acclaim'),
             ('Edacious', 'having an instable appetite, great voracity'), ('Ephemeral', 'short-lived, transitory'),
             ('Epicene', 'having characteristics of both male and female'),
             ('Escarpment', 'cliff, a steep slope resulting from erosion'), ('Esculent', 'edible, suitable for eating'),
             ('Etiolate', 'pale and drawn, to make weak by stunting growth'),
             ('Euthenics', 'the science of improving the condition of humans by improving their environment'),
             ('Evanescent', 'fleeting, vanishing, transient'), ('Evince', 'to show, reveal'),
             ('Filial', 'relating to a son'), ('Forward', 'contrary, consistently disobedient'),
             ('Fustian', 'ridiculously pompous, bombastic, grandiose in delivery'),
             ('Galoot', 'a loutish oaf, a clumsy but somewhat likable person'),
             ('Gemeinschaft', 'a group with similar tastes, a group bound by similar interests and kinship'),
             ('Grig', 'a lively person'),
             ('Hegira', 'an escape to avoid danger or to get away from an unpleasant location'),
             ('Homologate', 'to confirm officially'), ('Hortative', 'giving advice or exhortation'),
             ('Imago', 'an adult stage of an insect'), ('Indeterminate', 'vague, not known in advance'),
             ('Indubitable', 'unquestionable'), ('Ineffable', 'unutterable, unspeakable'),
             ('Ineluctable', 'inescapable, not to be avoided'), ('Inquietude', 'uneasiness, restlessness'),
             ('Inured', 'to become accustomed to something undesirable'),
             ('Jejune', 'dull, lacking interest, empty of food'), ('Labile', 'unstable, adaptable, liable to change'),
             ('Lachrymose', 'tearful, mournful'), ('Lambent', 'radiant, flickering, marked by lightness'),
             ('Lissome', 'supple'), ('Luminary', 'a person of great intellectual, creative or spiritual stature'),
             ('Lupine', 'having the characteristics of a wolf'), ('Manqué', 'a failure to realize one’s aspirations'),
             ('Manumit', 'to release from slavery'),
             ('Matrix', 'something from which something else originates or takes from'),
             ('Mélange', 'a mixture of incongruous elements'), ('Mien', 'demeanor, the air bearing of a person'),
             ('Minion', 'a hanger-on, a follower, an underling'), ('Moue', 'a pout, usually playful, a little grimace'),
             ('Mugwump', 'a person or politician who can’t make up his mind, an independent'),
             ('Nefandous', 'unspeakable, unutterable'),
             ('Nimbus', 'an atmosphere that surrounds a person or thing, a rain cloud'),
             ('Obloquy', 'strong language of condemnation'),
             ('Obstreperous', 'stubbornly defiant, angry and clamorous'),
             ('Offal', 'the waste parts of a product (often as in a butchered animal), refuse, rubbish'),
             ('Opine', 'to express an opinion'), ('Pace', 'with deference to'), ('Pachyderm', 'a thick-skinned animal'),
             ('Paralogism', 'illogical reasoning of which the reason is not aware'), ('Paroxysm', 'a fit'),
             ('Parvenu',
              'an upstart who has acquired wealth and class but hasn’t been accepted by people on that level'),
             ('Pastiche', 'a piece that imitates or is made up from pieces of other works'),
             ('Percipience', 'keen perception'), ('Perdition', 'eternal damnation'),
             ('Plenary', 'complete, fully attended, not deficient in any way'), ('Pluvial', 'rainy'),
             ('Poltroon', 'a coward'),
             ('Proscenium', 'the part of the stage in front of the curtain, the wall frame for the stage'),
             ('Proselytize', 'to seek to convert someone to a religion, cause or political position'),
             ('Pulchritude', 'physical beauty'),
             ('Quiddity', 'the real nature of a thing, the essence , a hairsplitting distinction'),
             ('Quisling', 'a traitor who helps an enemy who occupies his country'),
             ('Quotidian', 'occurring every day, commonplace'),
             ('Retinue', 'a group of attendants to an elevated person'), ('Saporous', 'tasty, flavorsome'),
             ('Satrap', 'a subordinate ruler'), ('Sciolism', 'superficial knowledge'),
             ('Senescence', 'beginning of old age'),
             ('Sequacious', 'slavish, obsequious, following in logical sequence'), ('Serried', 'crowded together'),
             ('Serviette', 'a table napkin'), ('Shantung', 'a heavy nubby fabric, made of wild silk'),
             ('Supervene', 'to follow immediately after, to ensue'), ('Surcease', 'cessation'),
             ('Tatterdemalion', 'a ragged person, always in tatters'),
             ('Teleology', 'the study of design or purpose in natural phenomena'),
             ('Temerarious', 'recklessly daring, rash'), ('Tenebrous', 'dark and gloomy'),
             ('Termagant', 'a quarrelsome woman, a shrew'),
             ('Trilemma', 'a problem for which there are three possible courses of action, and none perfect'),
             ('Tumid', 'swollen, distended, a bulging shape, overblown, bombastic'),
             ('Ukase', 'an authoritative decree, official edict'),
             ('Usufruct', 'the right to use someone else’s property as long as its not damaged in the process'),
             ('Vernal', 'occurring in spring, springlike youthful'),
             ('Vitiate', 'to impair the quality of, to corrupt morally'),
             ('Vituperative', 'harshly scolding, acrimonious'),
             ('Votary', 'a person bound by vows to live a life of religious service'),
             ('Welter', 'to write, toss, wallow'), ('Winnow', 'to blow of, or away, to separate the good from the bad'),
             ('Wraith', 'a specter, ghost of a dead person'), ('Ziggurat', 'a pyramidal stepped temple tower')]

    word = random.choice(vocab)
    guess = '```'
    for i in range(0, len(word[0])):
        if word[0][i] != ' ':
            guess += '_ '
        elif word[0][i] == ' ':
            guess += ' '
        if i == len(word[0]) - 1:
            guess += '```'
    return word, guess


@bot.command()
async def hangman_check(message, word, guess):
    for letter in word[0]:
        if message == letter:
            print(word[0].index(letter))


@bot.event
async def on_ready():
    ready_message = f'{bot.user.name} is here! Type ">help" for a basic command list.'
    channel = discord.utils.get(bot.get_all_channels(), name='playfriend')
    await channel.send(ready_message)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    command = message.content.lower().strip().split()

    # Not currently functional. Should make a hangman class, add category documentation for help, pass context

    if command[0] == '>hm':
        try:
            if command[1] == 'start':
                word, guess = hangman_start()
                await message.channel.send(hangman0)
                await message.channel.send(guess)
                print(word)
                print(guess)
            elif len(command[1].strip()) == 1 & command[1].isalpha() & word is not None:
                await hangman_check(command[1].strip().lower(), word, guess)
            elif word is not None & command[1].strip().lower() == word.lower():
                print('correct')
                await message.channel.send('Congratulations! You won. The word was', word[0], 'which means', word[1], '.')
        except IndexError:
            pass

    await bot.process_commands(message)


bot.run(TOKEN)
