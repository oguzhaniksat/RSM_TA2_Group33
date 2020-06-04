import json
import time

f = open('../../gen/data-preparation/temp/Fortniteastronomicalevent.json','r', encoding='utf-8')

con = f.readlines()
#Creating 3 output file for the seperation
outfile = open('../../gen/data-preparation/temp/parsed-data-eventbef.csv', 'w', encoding = 'utf-8')
outfile2= open('../../gen/data-preparation/temp/parsed-data-event.csv', 'w', encoding = 'utf-8')
outfile3= open('../../gen/data-preparation/temp/parsed-data-eventaf.csv', 'w', encoding = 'utf-8')

outfile.write('id\tcreated_at\ttext\n')
outfile2.write('id\tcreated_at\ttext\n')
outfile3.write('id\tcreated_at\ttext\n')

cnt=0

for line in con:
    if (len(line)<=5): continue

    obj = json.loads(line.replace('\n',''))
    time = obj.get("created_at")
    text = obj.get('text')
    text = text.replace('\t', '').replace('\n', '')
    #Determing hours and minutes for dividing
    hour = time[11:13]
    minute = time [14:16]
    # Deleting username of the people who got reply(names of people who have been mentioned) in tweet
    if "@" in text:
        if ":" in text:
            try:
                a=text.index("@")
                a_sub=text[a:]
                b=a_sub.index(" ")
                text = text[:a]+text[a+b+1:]
            except:
                continue

    #Trying translate or pass
    counter=0
    lang = obj.get("lang")
    if lang != "en":
        #print (text)
        if counter % 2 == 0:
            try:
                a = TextBlob(text)
                text = a.translate(to= "en")
                time.sleep(1)
            except:
                text=text
        else:
            continue
        counter +=1



    #Sepeareting 3 pieces (first 15min,event[14.00-14.22],last 20min)
    if int(hour) == 13 and int(minute)>45:
        outfile.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text+'\n')
    else:
        if int(minute) < 22:
            outfile2.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text+'\n')
        if int(hour) ==14 and int(minute)>=22:
            outfile3.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text+'\n')

    #If limit needed, activate
    #cnt+=1
    #if cnt >40:
    #    break

print('done.')
