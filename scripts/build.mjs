import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url),{glyph}=require('./latin-glyphs.cjs'),root=path.resolve(import.meta.dirname,'..');
const chars={一:['jat1','하나'],二:['ji6','둘'],三:['saam1','셋'],四:['sei3','넷'],五:['ng5','다섯'],六:['luk6','여섯'],七:['cat1','일곱'],八:['baat3','여덟'],九:['gau2','아홉'],十:['sap6','열'],人:['jan4','사람'],大:['daai6','큰'],小:['siu2','작은'],口:['hau2','입'],日:['jat6','해 / 날'],月:['jyut6','달'],水:['seoi2','물'],火:['fo2','불'],天:['tin1','하늘'],中:['zung1','가운데'],我:['ngo5','나'],你:['nei5','너'],好:['hou2','좋다'],早:['zou2','이르다'],多:['do1','많다'],食:['sik6','먹다'],飲:['jam2','마시다'],係:['hai6','…이다'],唔:['m4','…하지 않다'],謝:['ze6','감사하다'],見:['gin3','보다 / 만나다']};
const template=await fs.readFile(path.join(root,'web/index.html'),'utf8');
await fs.rm(path.join(root,'dist'),{recursive:true,force:true});
const catalog=[];
for(const language of ['indonesian','cantonese','dutch','polish','swedish']){
 const data=JSON.parse(await fs.readFile(path.join(root,'data',language+'.json'),'utf8'));
 data.letters=[];
 for(const char of data.alphabet){data.letters.push({id:language+'-letter-'+char.codePointAt(0),text:char,meaning:chars[char]?.[1]||'소문자 '+char,reading:chars[char]?.[0]||'',topic:'letters'});if(language!=='cantonese')data.letters.push({id:language+'-letter-'+char.toUpperCase().codePointAt(0),text:char.toUpperCase(),meaning:'대문자 '+char.toUpperCase(),reading:'',topic:'letters'});}
 const glyphs=language==='cantonese'?JSON.parse(await fs.readFile(path.join(root,'assets/cantonese-strokes.json'),'utf8')):{};
 const canWrite=text=>[...text].every(char=>{if(/\s/u.test(char))return true;if(language==='cantonese')return Boolean(glyphs[char]);try{glyph(char);return true;}catch{return false;}});
 data.writingWords=data.words.filter(w=>canWrite(w.text)).slice(0,language==='indonesian'?60:40);
 if(data.writingWords.length<30)throw Error(language+': insufficient writable words');
 if(language!=='cantonese')for(const char of new Set([...data.letters.map(l=>l.text),...data.writingWords.flatMap(w=>[...w.text])]))if(!/\s/u.test(char))glyphs[char]={coordinate:'latin',medians:glyph(char).map(points=>points.filter((_,i)=>i%3===0||i===points.length-1))};
 const buildData=JSON.stringify(data),css=await fs.readFile(path.join(root,'web/styles.css')),js=await fs.readFile(path.join(root,'web/app.js')),core=await fs.readFile(path.join(root,'web/core.js'));
 for(const mode of ['writing','conversation']){
  const slug=language+(mode==='writing'?'-writing':'-beginner'),other=language+(mode==='writing'?'-beginner':'-writing'),title=data.ko+(mode==='writing'?' 쓰기':' 기본 회화');
  const out=path.join(root,'dist',slug);await fs.mkdir(out,{recursive:true});
  const values={...data,key:language,mode,title,counterpart:other,counterpartTitle:data.ko+(mode==='writing'?' 기본 회화':' 쓰기'),description:title+' · '+(mode==='writing'?'글자·낱말 따라 쓰기와 문장 입력':'상황별 표현·기초 단어·역할 대화')+' · 즐겨찾기와 간격 복습'};
  await fs.writeFile(path.join(out,'index.html'),template.replace(/\{\{(\w+)\}\}/g,(_,key)=>values[key]??''));
  for(const [name,content]of [['styles.css',css],['app.js',js],['core.js',core],['data.json',buildData],['strokes.json',JSON.stringify(mode==='writing'?glyphs:{})]])await fs.writeFile(path.join(out,name),content);
  await fs.copyFile(path.join(root,'assets',language+'.webp'),path.join(out,'hero.webp'));
  await fs.writeFile(path.join(out,'LICENSE.txt'),'Language Foundations · 33modeling\nLatin print tracing paths: 33modeling writing engine, with Polish and Swedish extensions.\nChinese character paths: hanzi-writer-data 2.0.1 / Make Me a Hanzi.\nThe original Arphic Public License follows unchanged.\n\n'+await fs.readFile(path.join(root,'assets/HANZI-WRITER-DATA-LICENSE.txt'),'utf8'));
  const version=crypto.createHash('sha256').update(js).update(core).update(css).update(template).update(buildData).update(JSON.stringify(glyphs)).update(await fs.readFile(path.join(root,'assets',language+'.webp'))).digest('hex').slice(0,14),cache='language-foundations-'+slug+'-'+version;
  await fs.writeFile(path.join(out,'sw.js'),`const CACHE=${JSON.stringify(cache)},ASSETS=['./','./index.html','./app.js','./core.js','./styles.css','./data.json','./strokes.json','./hero.webp'];\nself.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)).then(()=>self.skipWaiting())));self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('language-foundations-${slug}-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));self.addEventListener('fetch',e=>{if(e.request.method!=='GET'||new URL(e.request.url).origin!==self.location.origin||!new URL(e.request.url).pathname.startsWith(new URL('./',self.location).pathname))return;e.respondWith(fetch(e.request).then(r=>{if(r.ok&&r.type!=='opaque'){const copy=r.clone();e.waitUntil(caches.open(CACHE).then(c=>c.put(e.request,copy)).catch(()=>{}));}return r;}).catch(()=>caches.match(e.request).then(r=>r||(e.request.mode==='navigate'?caches.match('./index.html'):Response.error()))));});\n`);
  catalog.push({language,mode,slug,title,letters:data.letters.length,words:data.words.length,writingWords:data.writingWords.length,phrases:data.phrases.length,dialogues:data.dialogues.length});
 }
}
await fs.writeFile(path.join(root,'dist/catalog.json'),JSON.stringify(catalog,null,2));console.log(JSON.stringify(catalog,null,2));
