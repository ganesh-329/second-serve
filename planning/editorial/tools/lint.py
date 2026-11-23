import sys,re
t=open(sys.argv[1]).read()
body=t.split('**Continuity')[0]
pats={
'dash':r'[—–]|--',
'tic':r'for a (moment|second|while|long time|beat)|said nothing|didn\'t say anything|didn\'t look at|without looking|without turning|very quietly|\bfiled\b|[Ss]omething in his chest|That was all|for a long (second|moment)',
'banned':r'\b(delve|crucial|seamless|robust|vibrant|testament|highlight|leverage|showcase|enhance|tapestry|intricate|pivotal|realm|nuanced|meticulous|underscore|navigate|foster|embark|resonate)\w*',
'negpar':r"\bnot (just |only )?\w+[,.] (but )?\w|, not \w+|wasn't \w+\. (It|He|She) was|didn't \w+[^.]{0,40}, (he|she|it) \w+ed|[Nn]ot because",
'spelled':r'\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|thirty|hundred|first|second|third|fourth|fifth|once more)\b',
'feeladv':r'\b\w+(ly)\b',
}
for k,p in pats.items():
    for m in re.finditer(p,body):
        s=body.rfind('\n',0,m.start())+1; e=body.find('\n',m.end())
        line=body[s:e]
        if k=='feeladv':
            w=m.group(0).lower()
            if w not in ('angrily','sadly','happily','miserably','warmly','delightedly','nervously','anxiously','proudly','gently','softly','tiredly','kindly','coldly','sheepishly','grimly','cheerfully','pleasantly','bitterly','eagerly','fondly','shyly','sternly','smugly','gratefully','helplessly','wearily','glumly','flatly'): continue
        print(f'[{k}] {m.group(0)!r}: ...{line[max(0,m.start()-s-60):m.end()-s+60]}...')
print('words(prose):',len(re.findall(r"\b[\w'-]+\b",body)))
