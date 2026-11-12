import sys, os, re, xml.etree.ElementTree as ET
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
best={}; title=None; ns=None; revs=[]
for ev, el in ET.iterparse(src, events=("end",)):
    tag = el.tag.split('}')[-1]
    if tag == 'title': title = el.text
    elif tag == 'ns': ns = el.text
    elif tag == 'revision':
        ts = el.findtext('{*}timestamp') or ''
        tx = el.findtext('{*}text') or ''
        revs.append((ts, tx)); el.clear()
    elif tag == 'page':
        if ns in ('0','14') and title and revs:
            ts, tx = max(revs)
            if title not in best or ts > best[title][0]: best[title]=(ts,tx)
        el.clear(); title=None; ns=None; revs=[]
n=0
for t,(ts,tx) in best.items():
    if tx.lower().startswith('#redirect'): continue
    fn = re.sub(r'[^A-Za-z0-9._()-]+','_',t)[:150]+'.txt'
    open(os.path.join(out,fn),'w').write(t+'\n'+ts+'\n\n'+tx); n+=1
print(n, len(best))
