export const DAY=86400000;
export const topics={greetings:'인사·감사',introductions:'자기소개',essentials:'필수 표현',food:'식당·카페',transport:'교통',shopping:'쇼핑',directions:'길 묻기',stay:'숙소',help:'도움 요청',time:'시간·날씨',words:'기초 단어',basics:'기본 인사',airport:'공항',hotel:'숙소',restaurant:'식당',cafe:'카페',sightseeing:'관광',connectivity:'통신',emergency:'도움 요청',numbers:'숫자·시간',smalltalk:'자기소개'};
export const escapeHTML=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export function normalizeAnswer(value,locale='en'){return String(value).normalize('NFC').toLocaleLowerCase(locale).replace(/[.!?。？！,，:;“”"'’‘…()]/gu,'').replace(/\s+/gu,' ').trim();}
export function gradeReview(previous,known,now=Date.now()){
 const step=known?Math.min(5,(previous?.step||0)+1):0;
 return {step,count:(previous?.count||0)+1,last:now,due:now+(known?[0,1,3,7,14,30][step]*DAY:10*60000)};
}
export function deduplicateItems(items,locale){
 const unique=[],byText=new Map(),aliases={};
 for(const original of items){
  const text=original.text.normalize('NFC').toLocaleLowerCase(locale).trim().replace(/\s+/gu,' ')+'\0'+original.meaning.normalize('NFC').trim(),existing=byText.get(text);
  if(existing){aliases[original.id]=existing.id;existing.topics=[...new Set([...(existing.topics||[existing.topic]),...(original.topics||[original.topic])])];}
  else{const item={...original};unique.push(item);byText.set(text,item);}
 }
 return {items:unique,aliases};
}
export function validateBackup(input,{language,mode,ids,aliases={}}){
 if(!input||input.schema!=='language-foundations/v1'||input.language!==language||input.mode!==mode)throw Error('같은 언어·과정에서 내보낸 학습 기록을 선택하세요.');
 if(!input.progress||typeof input.progress!=='object'||Array.isArray(input.progress)||!Array.isArray(input.favorites))throw Error('학습 기록 형식을 확인하세요.');
 const progress={};
 for(const [id,row] of Object.entries(input.progress)){
  const canonical=ids.has(id)?id:Object.hasOwn(aliases,id)&&aliases[id];
  if(!canonical||!ids.has(canonical))continue;
  if(!row||!['step','count','last','due'].every(k=>Number.isFinite(row[k]))||row.step<0||row.step>5||!Number.isInteger(row.step)||row.count<0||!Number.isSafeInteger(row.count)||row.last<0||row.due<0||row.last>8640000000000000||row.due>8640000000000000)throw Error('복습 기록의 숫자가 올바르지 않습니다.');
  const previous=progress[canonical],latest=previous?.last>row.last?previous:row;
  progress[canonical]={step:latest.step,count:row.count+(previous?.count||0),last:latest.last,due:latest.due};
  if(!Number.isSafeInteger(progress[canonical].count))throw Error('복습 기록의 숫자가 올바르지 않습니다.');
 }
 return {progress,favorites:[...new Set(input.favorites.map(id=>ids.has(id)?id:Object.hasOwn(aliases,id)&&aliases[id]).filter(id=>ids.has(id)))]};
}
export function selectVoice(voices,locale){
 const target=locale.toLowerCase();
 if(target==='zh-hk')return voices.find(v=>/^(yue(?:-|$)|zh-hk$)/i.test(v.lang))||null;
 return voices.find(v=>v.lang.toLowerCase()===target)||voices.find(v=>v.lang.toLowerCase().split('-')[0]===target.split('-')[0])||null;
}
const distance=(a,b)=>Math.hypot(a[0]-b[0],a[1]-b[1]);
export function acceptsStroke(points,median){
 if(!points.length||!median.length)return false;
 if(distance(points[0],median[0])>110||distance(points.at(-1),median.at(-1))>115)return false;
 const close=(point,list)=>list.some(p=>distance(point,p)<90);
 const coverage=median.filter(p=>close(p,points)).length/median.length;
 const precision=points.filter(p=>close(p,median)).length/points.length;
 // Reversing, skipping most of a stroke, or scribbling over the square is not a completed stroke.
 return coverage>=.72&&precision>=.72;
}
export function mergeRecords(current,incoming){const merged={...current};for(const [id,row]of Object.entries(incoming))if(!merged[id]||row.last>merged[id].last)merged[id]=row;return merged;}
