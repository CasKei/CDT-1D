#----------------------------------------------------------------------------------------
# import time ---------------------
import time
# initialising -----------------
ppl = {}
arrested = ''
# functions ----------------------
def pt(msg):
    print(msg)
    time.sleep(2)
def pt2(msg):
    print(msg)
    time.sleep(4)
def inp(lis):
    num = input('Input a valid choice\nOption: ')
    while num not in lis:
        num = input('Input a valid choice\nOption: ')
    	if num in ['exit','quit']:
        	exit()
    return num
def ans(lis):
    ans = input('Input your answer: ')
    while ans not in lis:
        ans = input('Input your answer: ')
    if ans in ['exit','quit']:
        exit()
    return ans
# scenes -----------------------
def intro():
    pt2('''This story is purely fictitious and is inspired by a real nightmare.''')
    pt('''Life in SUTD is tough.''')
    pt('''You are feeling the stress.''')
    pt('''Your panic episodes are returning, and you must remember to take your \nmedicine with you in case you have a panic attack.''')
    pt2('''Your friends have called you down to Crooked Cooks (for some reason opens 24/7 now) \nfor a drink to relieve some stress.''')
    ppl['player'] = input('\nPlease enter your name \nYou will be a female for the context of this game\nName: ')
    ppl['TP'] = input("Please enter your 1st friend's name(Male): ")
    ppl['Tres'] = input("Please enter your 2nd friend's name(Male): ")
    ppl['Rei'] = input("Please enter your 3rd friend's name(Female): ")
    ppl['KC'] = input("Please enter your 4th friend's name(Female): ")
    ppl['Ad'] = input("Please enter your 5th friend's name(Female): ")
    scene1_1()
def scene1_1():
    pt2('The time is 0115')
    pt('You meet ' + ppl['TP'] + ', ' + ppl['Tres'] + ', ' + ppl['Rei'] + ', ' + ppl['KC'] + ' and ' + ppl['Ad'])
    pt('You put your bag on the seat and head away to order some drinks.\n')
    pt2('The time is 0130')
    pt('When you come back you notice your bag has been rummaged through and moved.\n')
    pt2('1. Ask the group who moved your bag')
    pt2('2. Ignore and sit down\n')
    num = inp(['1','2'])
    if num == '1':
        pt('\n' + ppl['Ad'] + ': Eh paiseh I shifted your bag.')
        pt('I moved my bag aside and sat down')
    else:
        pt('I moved my bag aside and sat down')
    scene1_2()
def scene1_2():
    pt('The group continues to chat and talk about their miserable lives')
    pt(ppl['Tres'] + ': I was in my room doing physics homework and I\'m still stuck!')
    pt(ppl['Rei'] + ': I haven\'t started, I showered and came down to do laundry.')
    pt(ppl['TP'] + ': I was just sleeping man, I haven\'t done CDT problem set.')
    pt(ppl['KC'] + ': It\'s so late I wanna sleep soon but I shall accompany you all.')
    pt(ppl['Ad'] + ': Fifth row was so tiring I wanna die...\n')
    pt2(ppl['Ad'] + ' was frowning more often and looking weirdly at you.')
    pt2('You get paranoid.')
    pt2('She did touch my bag after all!\n')
    pt2('The group keeps chatting and drinking, being under the influence of alcohol...\n')
    scene2_1()
def scene2_1():
    pt2('The time is 0200')
    pt(ppl['Ad'] + ': I don\'t feel so good... I need to go to the toilet.')
    pt(ppl['Ad'] + ' stands up and leaves for the toilet.')
    pt2('Everyone else continues drinking and talking about how their parachute\'s impact force is too high.\n')
    
    pt2('The time is 0205')
    pt('You overthink.')
    pt('What did ' + ppl['Ad'] + ' do to your bag?')
    pt('What did she find out?\nAll that stress is piling up again.')
    pt('You breathe heavily.')
    pt2('You take your bag and ask to go to the toilet.\n')
    
    pt2('The time is 0206')
    pt('You meet ' + ppl['Ad'] + ' in the toilet.\n')
    pt2(ppl['Ad'] + ': Are you ok? What were those pills, are you sick?')
    pt('You panic. ' + ppl['Ad'] + ' thinks you are crazy. You need some pills now to recover yourself.')
    pt('You try to take your pills out but your head splits in pain.')
    pt(ppl['Ad'] + ' startes in astoundment.')
    pt(ppl['Ad'] + ': Are these drugs? Are you having withdrawal symptoms?')
    pt(ppl['Ad'] + ' tries to stop you from taking your medicine.')
    pt2('You experience severe head in your head and you collapse, losing consciousness.\n')
    pt2('')
    pt2('')
    pt2('')
    scene2_2()
def scene2_2():
    pt2('The time is 0245')
    pt2('You regain a little of your consciousness.')
    pt2('Your head is still groggy and you can\'t see clear')
    pt2(ppl['Rei'] + ' goes to the toilet and sees you on the floor.')
    pt2('She also sees ' + ppl['Ad'] + '\'s corpse sprawled on the floor, legs extending out from a cubicle.')
    pt('She screams and dashes out of the toilet, only to run into Prof Kenny Choo.')
    pt('She shakes Prof Kenny and shouts')
    pt2(ppl['Rei'] + ': There\'s a body inside!\n')
    pt('Kenny was just chilling and getting drunk on students\' tears but this was news.')
    pt2('You regain full consciousness and see the body in front of you.\n')
    pt2(ppl['Ad'] + ' is... dead?')
    pt2(f'You let out a scream, and dash out to join ' + ppl['Rei'] + ' and Kenny, equally scared and confused.\n')

    pt2('The time is 0250')
    pt2('Kenny opens door to inspect, but is also scared af and runs away, meeting Prof Paolo, \nwho just drowned himself in beer as he was witnessed by students eating pineapples on pizza.\n')
    pt('Kenny grabs Paolo and screams')
    pt('Kenny: There\'s a murder in school!')
    pt('Paolo is confused.')
    pt('Paolo: WHAT!? Who dares interrupt my misery.')
    pt2('He is angry at how we disturbed his alone thinking time. He decides to investigate the issue.')
    scene3_1()
def scene3_1():
    pt2('The time is 0800')
    pt('Paolo: We need to get to the bottom of this.')
    pt('Paolo: I must resolve this issue or my sin will never be cleared!')
    pt('Paolo: We must first gather evidence.')
    pt2('Paolo: Everyone go find some clues!\n')
    pt('You agree.')
    pt2('You are confused and shocked as to why ' + ppl['Ad'] + ' was suddenly dead in front of you in the toilet.')
    pt('Were you knocked out?')
    pt('Why did she die?')
    pt('You suddenly have a strong urge to find the truth.')
    pt2('You go to the crime scene.\n')
    pt2('1. Take your bag')
    pt2('2. Have a closer look at ' + ppl['Ad'])
    num = inp(['1','2'])
    if num == '1':
        pt('You find your bag thrown aside on the floor.')
        pt('You pick it up and check its contents.')
        pt2('Everything is intact except for the fact that your medkit and pills are not around anymore.')
    else:
        pt('You approach her corpse.')
        pt('You are creeped out.')
        pt('You notice her head is in a position where she is probably knocked out by the toilet bowl.')
        pt2('Is that the reason for her death or is there something else?\n')
    scene3_2()
def scene3_2():
    pt2('The time is 0830')
    pt('Paolo calls everyone back before you can carry on finding more clues.')
    pt('You meet back with Paolo and your friends at the Tables.')
    pt('Your friends are giving their alibis.')
    pt2('Paolo has asked everyone to tell each other where we were at what time, and what we were doing.')
    scene4_1()
def scene4_1():
    pt2('(Location Tables)')
    pt2(ppl['Tres'] + ': We were drinking together at around 1am. We talked about everything and then ' + ppl['Ad'] + ' said she needed the toilet at 2am, so she went.')
    pt('Everyone agrees. Then it was your turn.')
    pt2(ppl['player'] + ': I also needed the toilet so I followed shortly after, at around 0205.')
    pt('Friends agree with you, it is consistent with what they know.')
    pt2(ppl['KC'] + ': I went to the toilet at 0210 just to wash my hands. I saw ' + ppl['Ad'] + ' being very scared, and ' + ppl['player'] + ' was there flushing something down the toilet bowl. I left after I washed my hands.')
    pt2(ppl['Tres'] + ': At 0225 I went to the toilet. I saw Paolo eating pineapples on pizza. \nPaolo said "shit" and gets beer to drown himself. I returned at 0230.')
    pt2(ppl['TP'] + ': I went to the toilet at 0230. I heard ' + ppl['player'] + ' saying "So you are ' + ppl['player'] + '\'s friend" from the girl\'s toilet, \nas if ' + ppl['player'] + ' is not ' + ppl['player'] + '. I was scared and thought I was too drunk so I returned at 0240. I saw Prof Kenny along the way and greeted him.')
    pt2(ppl['Rei'] + ': I...went to the toilet at 0245. I saw ' + ppl['Ad'] + ' just lying there! I was so scared I ran out and saw Prof Kenny and shook him. Sorry Prof!')
    pt2('Kenny: I was just minding my business getting drunk on students\' tears and was suddenly shookt by a shookt ' + ppl['Rei'] + '! I went in to see and when I saw ' + ppl['player'] + '\'s body I was so scared I also screamed and ran out. Then I ran into you and you know the rest.')
    pt2('Paolo: Kenny met me at 0250 indeed. So only ' + ppl['KC'] + ' has seen ' + ppl['Ad'] + ' alive? At 0210? ' + ppl['Ad'] + ' was still alive then. But when ' + ppl['Rei'] + ' saw the body it was 0245. So the murder must have happened in between.')
    pt2('Paolo is reminded of ' + ppl['Tres'] + ' witnessing him commit the most grievous of sins. He falters a little but continues:')
    pt2('Anyone here could have killed ' + ppl['Ad'] + ', ' + ppl['KC'] + ' might have lied, ' + ppl['Tres'] + ' might have exposed my secrets just to throw me off, ' + ppl['TP'] + ' might have been there, and ' + ppl['Rei'] + ' might have lied. \nWe need to get to the bottom of this. I recalled buying a lie detector device from Amazon few days ago and have not tried using it. We shall use it now. ')
    scene4_2()
def scene4_2():
    pt('Paolo went away and came back with his lie detector. "Kids, say the truth or this will zap you. Answer me, did you kill ' + ppl['Ad'] + '? But first I will try it myself."')
    pt('Paolo: **puts his hand on the lie detector** \nPaolo: Did you commit the murder? \nPaolo: No.')
    pt2('DETECTOR: TRUTH')
    pt('Paolo: Cool device')

    pt(ppl['Tres'] + ' puts hand on detector and says No.')
    pt2('DETECTOR: **ZAPP**')
    pt(ppl['Tres'] + ': FUCK.')

    pt(ppl['TP'] + ' puts hand on detector and says No.')
    pt2('DETECTOR: **ZAPP**')
    pt(ppl['TP'] + ': WTHHHH')

    pt(ppl['Rei'] + ' puts hand on detector and says No.')
    pt2('DETECTOR: **ZAPP**')
    pt(ppl['Rei'] + ': OUCH')

    pt(ppl['player'] + ' puts hand on detector and says No.')
    pt2('DETECTOR: **ZAPP**')
    pt(ppl['player'] + ': NANI')

    pt(ppl['KC'] + ' puts hand on detector and says No.')
    pt2('DETECTOR: **ZAPP**')
    pt(ppl['KC'] + ': WOT')

    pt('Kenny puts hand on detector and says No.')
    pt2('DETECTOR: TRUTH')
    pt('Kenny: YAY\n')

    pt2('Paolo: Okay so the 5 of you students are real suspicious here.\n')
    scene5()
def scene5():
    pt('Paolo: How about everyone tell me why it isn\'t you and I shall deduce from there?')
    pt2('You think for a while.')
    pt2(ppl['player'] + ': How can I kill ' + ppl['Ad'] + ' when I was unconscious? I don\'t even remember what happened. If I really killed, I would have run away, why would I stay for so long till ' + ppl['Rei'] + ' finds me? It can\'t be me.')
    pt2(ppl['Tres'] + ': I spent some time outside laughing at Paolo and I didn\'t take long in the toilet. I can\'t possibly kill in such a short amount of time.')
    pt2(ppl['Rei'] + ': If I killed ' + ppl['Ad'] + ' why would I tell everyone about it? I\'m already this scared...')
    pt2(ppl['KC'] + ': I saw ' + ppl['player'] + ' flushing something down the toilet bowl. And I saw ' + ppl['Ad'] + ' and she was still alive when I left the toilet.\n')
    pt('Paolo stares at everyone with bloodshot eyes as everyone took their turn. He adjusted his spectacles.')
    pt2('And he paused his glare at {}\n'.format(ppl['KC']))
    pt2('Paolo: ' + ppl['KC'] + ', your defence statement is the most unconvincing. Are you just pushing the blame on ' + ppl['player'] + ' to defend yourself?\n')
    pt('1. Defend '+ ppl['KC'])
    pt('\t' + ppl['KC'] + ' is not this kind of person! You\'ve known her for quite a while already!')
    pt('2. Suggest we inspect the crime scene for further analysis.')
    pt('3. Do nothing')
    num = inp(['1','2','3'])
    if num == '2':
        scene6()
    elif num == '1':
        pt('Paolo: I see.')
        pt2(ppl['Rei'] + ': Sir, your device detects water on skin to determine if a person is lying or not. My hands were wet spilling water, so the detector gave a false positive for me!')
        pt(ppl['TP'] + ': I have sweaty palms')
        pt(ppl['KC'] + ': Same')
        pt(ppl['Tres'] + ': OK I don\'t have sweaty palms but I am innocent.')
        pt2('Paolo: Okay I will test you again. Did you kill {}?'.format(ppl['Ad']))
        pt(ppl['Tres'] + ': No')
        pt2('***ZAPPP***')
        pt('Paolo: {}! You are my favourite student and I am deeply dissapointed in you! HORRIBLE!'.format(ppl['Tres']))
        pt('The police are called.')
        pt('They arrive and drag {} away. He was still screaming "IT REALLY ISN\'T ME!!!"'.format(ppl['Tres']))
        arrested = ppl['Tres']
        end(arrested)
    elif num == '3':
        pt('Paolo: Call the police! I didn\'t expect it to be you! What grudge do you have against her?')
        pt('The police arrive.')
        pt2('They take {} away. She points at {} and says "NOT ITS NOT ME, ITS HER! SHE\'S THE ONE! I TOLD YOU SHE FLUSHED SOMETHING DOWN THE TOILET IT MUST BE IMPORTANT!"'.format(ppl['KC'], ppl['player']))
        arrested = ppl['KC']
        end(arrested)
def scene6():
    pt('You go back to the crime scene.')
    pt2('Your hazy memory returns a little, and you seem to have seen a person with a black jacket through the mirror while you were there.')
    pt2("You notice that there is some text on the wall beside the mirror: 'Look in my face, I am somebody; Look in my back, I am nobody.'")
    pt('You report this to Paolo.\n')
    pt('Paolo: Who has a black jacket?')
    pt2('Only you and {} have black jackets. But Paolo suspects you less because this is a clue that you reported yourself.'.format(ppl['Tres']))
    pt2('{}: After {} it was {} who went, but KC does not have a black jacket and the timing does not match.'.format(ppl['Tres'],ppl['player'],ppl['KC']))
    pt('Paolo: I see. Then it is probable that {} is the killer since he was wearing a dark blue jacket. It might have appeared black in the dim lighting.'.format(ppl['TP']))
    pt2('{}: No, I heard a girl\'s voice from the female toilet and I think it must be the killer. The killer is a female with a voice similar to {}\'s!\n'.format(ppl['TP'],ppl['player']))
    pt('1. Defend ' + ppl['TP'] + '\n' + ppl['player'] + ': ' + ppl['TP'] + ' has nothing against ' + ppl['Ad'] + '. I don\'t think he has any motives for killing her.')
    pt('2. Call out {} as the murderer.'.format(ppl['TP']))
    pt('3. Do nothing')
    num = inp(['1','2','3'])
    if num in ['2','3']:
        pt('Paolo calls the police.')
        pt('The police arrives and takes {} away.'.format(ppl['TP']))
        pt("{}: IT'S NOT ME, I'LL NEVER DO SUCH A THING!".format(ppl['TP']))
        pt('Everyone looks at him in disappointment.')
        arrested = ppl['TP']
        end(arrested)
    elif num == '1':
        pt2('Paolo: {}, you have a point.'.format(ppl['player']))
        pt('Paolo: Also, ' + ppl['KC'] + ' said that she saw both ' + ppl['player'] + ' and ' + ppl['Ad'] + ' in the toilet together.')
        pt('Paolo: It is likely that what you heard, the "So you are ' + ppl['player'] + '\'s friend", may be directed at either ' + ppl['Ad'] + ' or perhaps ' + ppl['player'] + ' herself.')
        pt2('Paolo: Things are not as simple as it seems, we need to take note of more clues too, like the quote on the wall earlier.')
        scene7_1()
def scene7_1():
    pt('You resume your inspection of the crime scene.')
    pt2('You found a post-it note attached to one of the toilet lockers.')
    pt2("It reads: '4 Grapes , 1 Apple , 7 Bananas , 7 Mangoes , 2 Pineapples , 1 Orange , 8 Pomegranates'")
    pt('This must be the clue to decipher the password to the lock of this locker')
    ans(['passion'])
    pt('You managed to unlock the locker')
    pt2('Inside the locker there was a medkit. There are plasters, sterile gauze, \nbandages, scissors, pain killer, cough medicine, a name card of a psychiatrist, paracetamol, antiseptic cream.\n')
    scene7_2()
def scene7_2():
    pt('Paolo: Ok guys, tell me what you have found.')
    pt2('You tell them you deciphered the password to a locker and found a medkit inside. It looked like a normal medkit except for the namecard.')
    pt('Kenny: I have asked the security guards to check the CCTV footage.')
    pt2('Kenny: first we have '+ ppl['Ad'] + ' at 0200, then '+ ppl['player'] + ' at 0205.\nThen we have ' + ppl['KC'] + ' at 0215, ' + ppl['Tres'] + ' at 0225,\n' + ppl['TP'] + ' at 0230 and finally ' + ppl['Rei'] + ' at 0243.')
    pt('Paolo: The murder must have happened between 0205 and 0245.')
    pt('{}: I went in the toilet at 0243, so I cannot be the killer.'.format(ppl['Rei']))
    pt2('Paolo: {} died of plood loss, look at the blood-stained toilet bowl! {} only had 2 minutes to kill so she cannot be the killer.'.format(ppl['Ad'],ppl['Rei']))
    pt('Paolo: Hmm... The medkit...\nWho would bring a medkit to the toilet lockers?')
    pt2('Paolo: People usually keep it where they live or carry it with them. A medkit appearing locked up in a public toilet locker is unlikely, unless someone is in a rush to hide it.')
    pt2('Paolo: The owner must be the killer, who tried to hide his/her belongings temporarily in the locker in order to run away before he/she is found.')
    pt2('Now, who is the owner of this medkit?\n')
    pt2('Eerie as it seems, the medkit appears to be the one you always bring with you in your bag. Why did it end up locked in the locker? And why is it missing some things?')
    pt2('What happened when you were unconscious?\n')
    pt('1. Own up that you are the owner and expose your mental condition. You have panic attacks and stress, and influenced by alcohol you don\'n know what you have done.\nYou have been trying to hide your condition from your friends for fear of being judged.\n')
    pt('2. Hide your condition as you still want to hide this from your friends. Divert everyone\'s attention to {} who can drain the blood of insects by pressing certain acupressure points. She could have drained {}\'s blook in 2 minutes!\n'.format(ppl['Rei'],ppl['Ad']))
    num = inp(['1','2'])
    if num == '1':
        pt('Paolo: Your memory loss is appaling. I take this as a confession. Call the police!')
        pt('{}: Halo Polis'.format(ppl['TP']))
        pt('Everyone: Oh dear, we didn\'t know that you\'ve been struggling with a mental health problem! School has piled up so much stress on you that you decided to kill her on a whim in order to relieve your stress.\nWe are sorry for not noticing, we are such terrible friends!')
        pt('The police arrive and take {} away.'.format(ppl['player']))
        arrested = ppl['player']
        end(arrested)
    elif num == '2':
        pt2('Paolo gets chills when he heard that {} could do that. He cannot believe it initially, but of course all Asians know kungfu right?'.format(ppl['Rei']))
        pt2('Gathering himself again, Paolo: {}, as impressive as your skill may be, you should not use it on another person! What, are you a psychopath? Does this make you happy? Does this spark joy?'.format(ppl['Rei']))
        pt('Paolo: Arrest {}!\n'.format(ppl['Rei']))
        pt('{}: Whut... But well... ok then you got me haha.'.format(ppl['Rei']))
        pt2('{}: For exposing me, {}, you will pay! HAHAHAHA! You\'ll get what I mean next time! You are...like me! I can tell! HAHAHAHAHA!'.format(ppl['Rei'],ppl['player']))
        pt('Reina gets escorted away willingly because she is curious how its like inside a police car.')
        arrested = ppl['Rei']
        end(arrested)
def end(arrested):
    pt2('{} is caught and put to justice. {} will face justice under the law for the murder of {}.\n'.format(arrested,arrested,ppl['Ad']))
    pt2('After collecting your witness accounts, the authorities suggest that all witnesses and suspects undergo a psychiatric assessment and counselling to make sure everyone is okay and can recover from the traumatic event.')
    pt('You go to your usual doctor.')
    pt2('You reveal to your doctor that your panic episodes are still recurring. That you lost consciousness during that time. You explain all that you know to the doctor.')
    pt2('Your doctor ponders for a moment.')
    pt('He reassesses your condition, making you do more tests than usual.')
    pt('He pieces together the dots from the case.')
    pt2('After you lost consciousness at 0210 and before you woke up at 0245, {} saw you flushing down something. Your pills were gone weren\'t they.'.format(ppl['KC']))
    pt2('{} also heard your voice speaking at 0230, as if you didn\'t recognise your friend, as if you were a different person.'.format(ppl['TP']))
    pt2('{}, you were conscious during this time. You don\'t recall seeing {} do you?'.format(ppl['player'],ppl['KC']))
    pt2("You were conscious, but you weren't you.")
    pt2('I suspect you have DID, that is, dissociative identity disorder.')
    pt2('You have another personality in you, {}, you are the killer.\n\n'.format(ppl['player']))
    credits()
def credits():
    pt('Congratulations on completing the game. Play again to get a different end, of if you want to get all other paths for fun.')
    pt('If you wish to restart the game, enter 1. If not, enter 2.')
    num = inp(['1','2'])
    if num == '1':
        main()
    elif num == '2':
        pt2('Thank you for playing.')
       	pt2('This game is created by CC08 Group8, as part of CDT 1D project 2020.')
        pt2('Credits: \nPeh Shu Ting: 1005359\nTresthon Quah Wee Kian: 1005649\nTeng Peng: 1005408\nCassie Chong Kenci: 1005301')
        pt('If you didn\'t see the credits, play again')
        exit()
       	
# def start -------------------
def main():
    pt('Welcome to our game. Would you like to play?')
    response = input('Y/N?')
    if response == 'Y':
        intro()
    else:
        exit()
# game start ---------------------
main()