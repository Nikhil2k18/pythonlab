import random
print('\t---------------------------')
print('\t\tMad Libs Generator')
print('\t---------------------------')
print('\t\t\tBY:NIKHIL SHARMA-1118\n\t\t\tRISHABH SINGLA-1128')
print('\t\t\t\nmenu\n1.randomly predefined lists \t2.input from user\n')

def funcpre():
    random_name=['Sam','Jhon','Karan','Shubham','Shreya','Nidhi','Pari']
    your_name = ['Nikhil','Rishabh']
    place = ['park','mall','cafe','club']
    adjective =['amazing','beautiful','wonderful','marvellous']
    adjs = ['Chatty','brave',"Crazy", "Nice", "Lovely", "Gross"]
    verbs = ['beat','drawn','drove',"met", "proposed to", "robbed", "pushed"]
    prepositions = ['beneath','under',"above the", "near the", "around the", "behind", "beside"]
    print(random.choice(adjs) + " " + random.choice(random_name) + " " + (random.choice(verbs))+ " " + random.choice(your_name) + " " + (random.choice(prepositions))+ " " + random.choice(adjective)+ " " + random.choice(place ))

def funcuser():
    print('-------------------------------------------------------------------------')
    print('*--(exclamation)..! they said ..(adverb). as they jumped into their..(noun)..\n and flew off with their..(adjective).(plural noun)..--*\n')
    print('-------------------------------------------------------------------------')
    print('enter examples for each for given above')
    print('---------------------------------------')
    ex=input('enter eg for exclamation: ')
    ad=input('enter eg for adverb: ')
    no=input('enter eg for noun: ')
    adj=input('enter eg for adjective: ')
    plnon=input('enter eg for plural noun: ')
    print(ex+' ! they said '+ad+' as they jumped into their '+no+' and flew off with their'+adj+' '+plnon)

choice=int(input('enter your choice and 0 to exit '))    

if(choice==1):
    while True:
        funcpre();
        c=input('\nwant to regenerate yes or no \n')
        if not(c=='yes'):
            break
if(choice==2):
    while True:
        funcuser();
        c=input('\nwant to regenerate yes or no \n')
        if not(c=='yes'):
            break






