import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {DAY,normalizeAnswer,gradeReview,validateBackup,selectVoice,acceptsStroke,mergeRecords,deduplicateItems} from '../web/core.js';

test('Polish and Swedish letters retain accents and NFC equivalence in answers',()=>{
 for(const [right,wrong,locale]of [['Dzień dobry.','Dzien dobry','pl-PL'],['åtta','atta','sv-SE'],['ł','l','pl-PL'],['ż','ź','pl-PL']])assert.notEqual(normalizeAnswer(right,locale),normalizeAnswer(wrong,locale));
 assert.equal(normalizeAnswer('DZIEŃ DOBRY!','pl-PL'),normalizeAnswer('dzień dobry.','pl-PL'));assert.equal(normalizeAnswer('a\u030a','sv-SE'),'å');
});
test('review records use measured attempts and bounded intervals',()=>{
 const start=12345,first=gradeReview(null,true,start),second=gradeReview(first,true,start+1);assert.equal(first.count,1);assert.equal(first.due,start+DAY);assert.equal(second.due,start+1+3*DAY);const again=gradeReview(second,false,start+2);assert.equal(again.step,0);assert.equal(again.count,3);assert.equal(again.due,start+2+600000);
});
test('backups are scoped and validated before merging; unknown IDs never enter storage',()=>{
 const scope={language:'polish',mode:'writing',ids:new Set(['a'])},row={step:1,count:1,last:10,due:20},backup={schema:'language-foundations/v1',language:'polish',mode:'writing',favorites:['a','foreign'],progress:{a:row,foreign:row}};
 assert.deepEqual(validateBackup(backup,scope),{progress:{a:row},favorites:['a']});assert.throws(()=>validateBackup({...backup,language:'swedish'},scope));assert.throws(()=>validateBackup({...backup,mode:'conversation'},scope));assert.throws(()=>validateBackup({...backup,progress:{a:{...row,due:null}}},scope));assert.equal(mergeRecords({a:{...row,last:30}}, {a:row}).a.last,30);
});
test('Cantonese never silently uses Mandarin; other voices stay within their language',()=>{
 const voices=[{lang:'zh-CN'},{lang:'nl-NL'},{lang:'sv-SE'},{lang:'yue-HK'}];assert.equal(selectVoice(voices,'zh-HK').lang,'yue-HK');assert.equal(selectVoice([{lang:'zh-CN'},{lang:'zh-TW'}],'zh-HK'),null);assert.equal(selectVoice(voices,'nl-NL').lang,'nl-NL');assert.equal(selectVoice(voices,'pl-PL'),null);
});
test('duplicate lessons retain both topic memberships and distinct meanings',()=>{
 const original=[{id:'a',text:'dekat',meaning:'가까운',topic:'transport'},{id:'b',text:'dekat',meaning:'가까운',topic:'directions'},{id:'c',text:'morgen',meaning:'내일',topic:'time'},{id:'d',text:'morgen',meaning:'아침',topic:'time'}];
 const result=deduplicateItems(original,'id-ID');assert.equal(result.items.length,3);assert.deepEqual(result.items[0].topics,['transport','directions']);assert.deepEqual(result.aliases,{b:'a'});assert.equal(original[0].topics,undefined);
});
test('deduplicating existing lessons preserves attempts, favorites and the latest review schedule',()=>{
 const scope={language:'indonesian',mode:'conversation',ids:new Set(['first']),aliases:{duplicate:'first'}},older={step:1,count:2,last:100,due:300},latest={step:2,count:3,last:200,due:500},backup={schema:'language-foundations/v1',language:'indonesian',mode:'conversation',progress:{first:older,duplicate:latest},favorites:['duplicate','first']};
 assert.deepEqual(validateBackup(backup,scope),{progress:{first:{...latest,count:5}},favorites:['first']});assert.throws(()=>validateBackup({...backup,progress:{first:{...older,count:Number.MAX_VALUE}}},scope));assert.throws(()=>validateBackup({...backup,progress:{first:{...older,due:1e30}}},scope));
});
test('stroke validation rejects reversed, shortened and unrelated ink',()=>{
 const median=Array.from({length:30},(_,i)=>[200+i*20,300]);assert.ok(acceptsStroke(median,median));assert.equal(acceptsStroke([...median].reverse(),median),false);assert.equal(acceptsStroke(median.slice(0,5),median),false);assert.equal(acceptsStroke([[0,0],[1000,1000]],median),false);
});
for(const language of ['indonesian','cantonese','dutch','polish','swedish'])test(language+' has consistent starter writing and conversation content',async()=>{
 const p=new URL('../dist/'+language+'-writing/',import.meta.url),data=JSON.parse(await fs.readFile(new URL('data.json',p))),glyphs=JSON.parse(await fs.readFile(new URL('strokes.json',p)));
 assert.ok(data.phrases.length>=60);assert.ok(data.words.length>=40);assert.ok(data.dialogues.length>=8);assert.equal(data.notes.length,6);assert.ok(data.writingWords.length>=30);
 const items=[...data.letters,...data.words,...data.phrases],ids=items.map(i=>i.id);assert.equal(ids.length,new Set(ids).size);assert.ok(items.every(i=>i.text&&i.meaning));
 for(const section of ['phrases','words'])assert.equal(new Set(data[section].map(i=>i.text.toLocaleLowerCase(data.locale)+'\0'+i.meaning)).size,data[section].length);
 for(const item of [...data.letters,...data.writingWords])for(const char of [...item.text].filter(c=>! /\s/u.test(c)))assert.ok(glyphs[char]?.medians?.length,language+' '+char);
 if(language==='polish'){assert.equal(data.letters.length,64);assert.ok(glyphs['ą']);assert.ok(glyphs['Ł']);}if(language==='swedish')assert.equal(data.letters.length,58);
 if(language==='cantonese')for(const item of [...data.phrases,...data.words,...data.dialogues.flatMap(d=>d.lines)])assert.match(item.reading,/^[a-z]+[1-6](?: [a-z]+[1-6])*$/);
 for(const mode of ['writing','beginner']){const out=new URL('../dist/'+language+'-'+mode+'/',import.meta.url);const html=await fs.readFile(new URL('index.html',out),'utf8');assert.doesNotMatch(html,/\{\{/);assert.ok(html.includes('../'+language+(mode==='writing'?'-beginner/':'-writing/')));for(const file of ['app.js','core.js','styles.css','hero.webp','sw.js','LICENSE.txt'])assert.ok((await fs.stat(new URL(file,out))).size>0);}
});
