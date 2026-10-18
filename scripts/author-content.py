"""Maintain native examples and Korean teaching notes in one place."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]

# topic | native sentence | Korean meaning | pronunciation (Cantonese Jyutping)
PHRASES={
'dutch':'''greetings|Hallo!|안녕하세요!
greetings|Goedemorgen.|좋은 아침이에요.
greetings|Goedemiddag.|안녕하세요. (오후 인사)
greetings|Goedenavond.|안녕하세요. (저녁 인사)
greetings|Tot ziens!|또 만나요!
greetings|Dank u wel.|감사합니다. (공손하게)
greetings|Dank je wel.|고마워요. (친근하게)
greetings|Graag gedaan.|천만에요.
greetings|Sorry.|미안해요.
greetings|Geen probleem.|괜찮아요.
introductions|Hoe heet je?|이름이 뭐예요?
introductions|Ik heet Min.|제 이름은 민이에요.
introductions|Aangenaam.|만나서 반가워요.
introductions|Waar kom je vandaan?|어디에서 왔어요?
introductions|Ik kom uit Zuid-Korea.|저는 한국에서 왔어요.
introductions|Ik leer Nederlands.|저는 네덜란드어를 배우고 있어요.
introductions|Ik spreek een beetje Nederlands.|네덜란드어를 조금 해요.
introductions|Spreekt u Engels?|영어 하세요? (공손하게)
introductions|Hoe gaat het?|어떻게 지내요?
introductions|Goed, dank je.|잘 지내요. 고마워요.
essentials|Ja.|네.
essentials|Nee.|아니요.
essentials|Alstublieft.|부탁합니다. / 여기 있습니다. (공손하게)
essentials|Ik begrijp het niet.|이해하지 못했어요.
essentials|Kunt u dat herhalen?|다시 말씀해 주시겠어요?
essentials|Kunt u langzamer spreken?|조금 천천히 말씀해 주시겠어요?
essentials|Wat betekent dit?|이것은 무슨 뜻이에요?
essentials|Hoe zeg je dit in het Nederlands?|이것을 네덜란드어로 어떻게 말해요?
food|Ik wil graag een koffie.|커피 한 잔 주세요.
food|Een thee, alstublieft.|차 한 잔 주세요.
food|Mag ik de menukaart?|메뉴판을 받을 수 있을까요?
food|Ik ben vegetariër.|저는 채식주의자예요.
food|Zonder melk, alstublieft.|우유는 빼 주세요.
food|Mag ik een glas water?|물 한 잔 주시겠어요?
food|Het is lekker.|맛있어요.
food|Mag ik de rekening?|계산서 주세요.
transport|Waar is het station?|역이 어디예요?
transport|Een kaartje naar Amsterdam, alstublieft.|암스테르담행 표 한 장 주세요.
transport|Hoe laat vertrekt de trein?|기차는 몇 시에 출발해요?
transport|Op welk spoor?|몇 번 승강장인가요?
transport|Gaat deze bus naar het centrum?|이 버스는 시내로 가나요?
transport|Ik wil hier uitstappen.|여기서 내리고 싶어요.
transport|Hoe lang duurt het?|얼마나 걸려요?
shopping|Hoeveel kost dit?|이것은 얼마예요?
shopping|Kan ik met een kaart betalen?|카드로 계산할 수 있나요?
shopping|Heeft u een kleinere maat?|더 작은 사이즈가 있나요?
shopping|Ik kijk alleen even.|잠깐 구경만 할게요.
shopping|Ik neem deze.|이것으로 할게요.
shopping|Mag ik een bonnetje?|영수증 주시겠어요?
directions|Waar is het toilet?|화장실이 어디예요?
directions|Is het ver?|먼가요?
directions|Ga rechtdoor.|곧장 가세요.
directions|Sla linksaf.|왼쪽으로 도세요.
directions|Sla rechtsaf.|오른쪽으로 도세요.
directions|Kunt u het op de kaart aanwijzen?|지도에서 가리켜 주시겠어요?
stay|Ik heb een reservering.|예약했어요.
stay|Ik wil graag inchecken.|체크인하고 싶어요.
stay|Wat is het wifiwachtwoord?|와이파이 비밀번호가 뭔가요?
stay|Hoe laat is het ontbijt?|아침 식사는 몇 시예요?
stay|Ik blijf twee nachten.|이틀 밤 머물 거예요.
help|Ik heb hulp nodig.|도움이 필요해요.
help|Ik ben verdwaald.|길을 잃었어요.
help|Ik voel me niet goed.|몸이 좋지 않아요.
help|Waar is een apotheek?|약국이 어디예요?
help|Bel een ambulance, alstublieft.|구급차를 불러 주세요.
time|Hoe laat is het?|몇 시예요?
time|Vandaag heb ik tijd.|오늘은 시간이 있어요.
time|Tot morgen!|내일 봐요!
time|Het regent.|비가 와요.
time|Het is koud.|추워요.''',
'polish':'''greetings|Dzień dobry.|안녕하세요. (낮 인사)
greetings|Dobry wieczór.|안녕하세요. (저녁 인사)
greetings|Cześć!|안녕! (친근하게)
greetings|Do widzenia.|안녕히 가세요. / 안녕히 계세요.
greetings|Do zobaczenia!|또 만나요!
greetings|Dziękuję.|감사합니다.
greetings|Proszę.|부탁합니다. / 여기 있습니다.
greetings|Nie ma za co.|천만에요.
greetings|Przepraszam.|죄송합니다. / 실례합니다.
greetings|Nic nie szkodzi.|괜찮아요.
introductions|Jak masz na imię?|이름이 뭐예요? (친근하게)
introductions|Mam na imię Min.|제 이름은 민이에요.
introductions|Miło mi.|만나서 반가워요.
introductions|Skąd jesteś?|어디에서 왔어요? (친근하게)
introductions|Jestem z Korei Południowej.|저는 한국에서 왔어요.
introductions|Uczę się polskiego.|저는 폴란드어를 배우고 있어요.
introductions|Mówię trochę po polsku.|폴란드어를 조금 해요.
introductions|Czy mówi pan po angielsku?|영어 하세요? (남성에게 공손하게)
introductions|Czy mówi pani po angielsku?|영어 하세요? (여성에게 공손하게)
introductions|Jak się masz?|어떻게 지내요? (친근하게)
introductions|Dobrze, dziękuję.|잘 지내요. 고마워요.
essentials|Tak.|네.
essentials|Nie.|아니요.
essentials|Nie rozumiem.|이해하지 못했어요.
essentials|Proszę powtórzyć.|다시 말씀해 주세요.
essentials|Proszę mówić wolniej.|조금 천천히 말씀해 주세요.
essentials|Co to znaczy?|이것은 무슨 뜻이에요?
essentials|Jak to powiedzieć po polsku?|이것을 폴란드어로 어떻게 말해요?
food|Poproszę kawę.|커피 한 잔 주세요.
food|Poproszę herbatę.|차 한 잔 주세요.
food|Poproszę menu.|메뉴판 주세요.
food|Bez mięsa, proszę.|고기는 빼 주세요.
food|Bez mleka, proszę.|우유는 빼 주세요.
food|Poproszę szklankę wody.|물 한 잔 주세요.
food|To jest smaczne.|맛있어요.
food|Poproszę rachunek.|계산서 주세요.
transport|Gdzie jest dworzec?|역이 어디예요?
transport|Poproszę bilet do Warszawy.|바르샤바행 표 한 장 주세요.
transport|O której odjeżdża pociąg?|기차는 몇 시에 출발해요?
transport|Z którego peronu?|몇 번 승강장에서 출발하나요?
transport|Czy ten autobus jedzie do centrum?|이 버스는 시내로 가나요?
transport|Chcę tutaj wysiąść.|여기서 내리고 싶어요.
transport|Jak długo to trwa?|얼마나 걸려요?
shopping|Ile to kosztuje?|이것은 얼마예요?
shopping|Czy mogę zapłacić kartą?|카드로 계산할 수 있나요?
shopping|Czy jest mniejszy rozmiar?|더 작은 사이즈가 있나요?
shopping|Tylko oglądam.|구경만 할게요.
shopping|Wezmę to.|이것으로 할게요.
shopping|Poproszę paragon.|영수증 주세요.
directions|Gdzie jest toaleta?|화장실이 어디예요?
directions|Czy to daleko?|먼가요?
directions|Proszę iść prosto.|곧장 가세요.
directions|Proszę skręcić w lewo.|왼쪽으로 도세요.
directions|Proszę skręcić w prawo.|오른쪽으로 도세요.
directions|Proszę pokazać na mapie.|지도에서 가리켜 주세요.
stay|Mam rezerwację.|예약했어요.
stay|Chcę się zameldować.|체크인하고 싶어요.
stay|Jakie jest hasło do Wi-Fi?|와이파이 비밀번호가 뭔가요?
stay|O której jest śniadanie?|아침 식사는 몇 시예요?
stay|Zostaję na dwie noce.|이틀 밤 머물 거예요.
help|Potrzebuję pomocy.|도움이 필요해요.
help|Nie mogę znaleźć drogi.|길을 찾지 못하겠어요.
help|Źle się czuję.|몸이 좋지 않아요.
help|Gdzie jest apteka?|약국이 어디예요?
help|Proszę wezwać karetkę.|구급차를 불러 주세요.
time|Która jest godzina?|몇 시예요?
time|Dzisiaj mam czas.|오늘은 시간이 있어요.
time|Do jutra!|내일 봐요!
time|Pada deszcz.|비가 와요.
time|Jest zimno.|추워요.''',
'swedish':'''greetings|Hej!|안녕하세요!
greetings|God morgon.|좋은 아침이에요.
greetings|God kväll.|안녕하세요. (저녁 인사)
greetings|Hej då!|잘 가요! / 안녕히 계세요!
greetings|Vi ses!|또 만나요!
greetings|Tack.|감사합니다.
greetings|Tack så mycket.|정말 감사합니다.
greetings|Varsågod.|천만에요. / 여기 있습니다.
greetings|Ursäkta.|실례합니다.
greetings|Förlåt.|미안해요.
greetings|Ingen fara.|괜찮아요.
introductions|Vad heter du?|이름이 뭐예요?
introductions|Jag heter Min.|제 이름은 민이에요.
introductions|Trevligt att träffas.|만나서 반가워요.
introductions|Var kommer du ifrån?|어디에서 왔어요?
introductions|Jag kommer från Sydkorea.|저는 한국에서 왔어요.
introductions|Jag lär mig svenska.|저는 스웨덴어를 배우고 있어요.
introductions|Jag talar lite svenska.|스웨덴어를 조금 해요.
introductions|Talar du engelska?|영어 하세요?
introductions|Hur mår du?|어떻게 지내요?
introductions|Jag mår bra, tack.|잘 지내요. 고마워요.
essentials|Ja.|네.
essentials|Nej.|아니요.
essentials|Jag förstår inte.|이해하지 못했어요.
essentials|Kan du säga det igen?|다시 말씀해 주시겠어요?
essentials|Kan du prata långsammare?|조금 천천히 말씀해 주시겠어요?
essentials|Vad betyder det?|이것은 무슨 뜻이에요?
essentials|Hur säger man det på svenska?|이것을 스웨덴어로 어떻게 말해요?
food|En kaffe, tack.|커피 한 잔 주세요.
food|En kopp te, tack.|차 한 잔 주세요.
food|Kan jag få menyn?|메뉴판을 받을 수 있을까요?
food|Jag äter inte kött.|저는 고기를 먹지 않아요.
food|Utan mjölk, tack.|우유는 빼 주세요.
food|Kan jag få ett glas vatten?|물 한 잔 주시겠어요?
food|Det smakar gott.|맛있어요.
food|Kan jag få notan?|계산서 주세요.
transport|Var ligger stationen?|역이 어디예요?
transport|En biljett till Stockholm, tack.|스톡홀름행 표 한 장 주세요.
transport|När går tåget?|기차는 언제 출발해요?
transport|Från vilket spår?|몇 번 승강장에서 출발하나요?
transport|Går den här bussen till centrum?|이 버스는 시내로 가나요?
transport|Jag vill gå av här.|여기서 내리고 싶어요.
transport|Hur lång tid tar det?|얼마나 걸려요?
shopping|Vad kostar det?|이것은 얼마예요?
shopping|Kan jag betala med kort?|카드로 계산할 수 있나요?
shopping|Finns det en mindre storlek?|더 작은 사이즈가 있나요?
shopping|Jag tittar bara.|구경만 할게요.
shopping|Jag tar den här.|이것으로 할게요.
shopping|Kan jag få ett kvitto?|영수증 주시겠어요?
directions|Var är toaletten?|화장실이 어디예요?
directions|Är det långt?|먼가요?
directions|Gå rakt fram.|곧장 가세요.
directions|Sväng vänster.|왼쪽으로 도세요.
directions|Sväng höger.|오른쪽으로 도세요.
directions|Kan du visa på kartan?|지도에서 가리켜 주시겠어요?
stay|Jag har en bokning.|예약했어요.
stay|Jag vill checka in.|체크인하고 싶어요.
stay|Vad är lösenordet till wifi?|와이파이 비밀번호가 뭔가요?
stay|När är frukosten?|아침 식사는 언제예요?
stay|Jag stannar två nätter.|이틀 밤 머물 거예요.
help|Jag behöver hjälp.|도움이 필요해요.
help|Jag har gått vilse.|길을 잃었어요.
help|Jag mår inte bra.|몸이 좋지 않아요.
help|Var finns ett apotek?|약국이 어디예요?
help|Ring en ambulans, tack.|구급차를 불러 주세요.
time|Vad är klockan?|몇 시예요?
time|Jag har tid idag.|오늘은 시간이 있어요.
time|Vi ses imorgon!|내일 봐요!
time|Det regnar.|비가 와요.
time|Det är kallt.|추워요.''',
'cantonese':'''greetings|你好。|안녕하세요.|nei5 hou2
greetings|早晨。|좋은 아침이에요.|zou2 san4
greetings|你好嗎？|잘 지내세요?|nei5 hou2 maa3
greetings|我幾好。|저는 잘 지내요.|ngo5 gei2 hou2
greetings|再見。|안녕히 가세요. / 안녕히 계세요.|zoi3 gin3
greetings|拜拜。|잘 가요!|baai1 baai3
greetings|多謝。|감사합니다. (선물·큰 호의에)|do1 ze6
greetings|唔該。|감사합니다. / 실례합니다. (도움·서비스에)|m4 goi1
greetings|唔使客氣。|천만에요.|m4 sai2 haak3 hei3
greetings|對唔住。|죄송합니다.|deoi3 m4 zyu6
greetings|唔緊要。|괜찮아요.|m4 gan2 jiu3
introductions|你叫咩名？|이름이 뭐예요?|nei5 giu3 me1 meng2
introductions|我叫阿明。|제 이름은 아밍이에요.|ngo5 giu3 aa3 ming4
introductions|好高興識你。|만나서 반가워요.|hou2 gou1 hing3 sik1 nei5
introductions|你係邊度人？|어디 출신이에요?|nei5 hai6 bin1 dou6 jan4
introductions|我係韓國人。|저는 한국 사람이에요.|ngo5 hai6 hon4 gwok3 jan4
introductions|我學緊廣東話。|저는 광둥어를 배우고 있어요.|ngo5 hok6 gan2 gwong2 dung1 waa2
introductions|我識講少少廣東話。|광둥어를 조금 할 줄 알아요.|ngo5 sik1 gong2 siu2 siu2 gwong2 dung1 waa2
introductions|你識唔識講英文？|영어 할 줄 아세요?|nei5 sik1 m4 sik1 gong2 jing1 man4
essentials|係。|네. / 맞아요.|hai6
essentials|唔係。|아니에요.|m4 hai6
essentials|好。|좋아요.|hou2
essentials|唔好。|하지 마세요. / 싫어요.|m4 hou2
essentials|我唔明。|이해하지 못했어요.|ngo5 m4 ming4
essentials|請你再講一次。|다시 한 번 말씀해 주세요.|cing2 nei5 zoi3 gong2 jat1 ci3
essentials|唔該講慢啲。|조금 천천히 말씀해 주세요.|m4 goi1 gong2 maan6 di1
essentials|呢個係咩意思？|이것은 무슨 뜻이에요?|ni1 go3 hai6 me1 ji3 si1
essentials|廣東話點講？|광둥어로 어떻게 말해요?|gwong2 dung1 waa2 dim2 gong2
food|唔該，一杯咖啡。|커피 한 잔 주세요.|m4 goi1 jat1 bui1 gaa3 fe1
food|唔該，一杯茶。|차 한 잔 주세요.|m4 goi1 jat1 bui1 caa4
food|唔該，俾個餐牌我。|메뉴판 주세요.|m4 goi1 bei2 go3 caan1 paai2 ngo5
food|我唔食肉。|저는 고기를 먹지 않아요.|ngo5 m4 sik6 juk6
food|唔落奶，唔該。|우유는 넣지 말아 주세요.|m4 lok6 naai5 m4 goi1
food|唔該，一杯水。|물 한 잔 주세요.|m4 goi1 jat1 bui1 seoi2
food|好好食。|정말 맛있어요.|hou2 hou2 sik6
food|唔該，埋單。|계산해 주세요.|m4 goi1 maai4 daan1
transport|車站喺邊度？|정류장 / 역은 어디예요?|ce1 zaam6 hai2 bin1 dou6
transport|唔該，一張去中環嘅飛。|중완행 표 한 장 주세요.|m4 goi1 jat1 zoeng1 heoi3 zung1 waan4 ge3 fei1
transport|幾點開車？|몇 시에 출발해요?|gei2 dim2 hoi1 ce1
transport|邊個月台？|어느 승강장인가요?|bin1 go3 jyut6 toi4
transport|呢架巴士去唔去中環？|이 버스는 중완에 가나요?|ni1 gaa3 baa1 si2 heoi3 m4 heoi3 zung1 waan4
transport|我想喺呢度落車。|여기서 내리고 싶어요.|ngo5 soeng2 hai2 ni1 dou6 lok6 ce1
transport|要幾耐？|얼마나 걸려요?|jiu3 gei2 noi6
shopping|呢個幾多錢？|이것은 얼마예요?|ni1 go3 gei2 do1 cin2
shopping|可唔可以用信用卡？|신용카드를 쓸 수 있나요?|ho2 m4 ho2 ji5 jung6 seon3 jung6 kaat1
shopping|有冇細啲嘅？|더 작은 것이 있나요?|jau5 mou5 sai3 di1 ge3
shopping|我睇吓先。|먼저 좀 구경할게요.|ngo5 tai2 haa5 sin1
shopping|我要呢個。|이것으로 할게요.|ngo5 jiu3 ni1 go3
shopping|唔該，俾張單我。|영수증 주세요.|m4 goi1 bei2 zoeng1 daan1 ngo5
directions|廁所喺邊度？|화장실이 어디예요?|ci3 so2 hai2 bin1 dou6
directions|遠唔遠？|먼가요?|jyun5 m4 jyun5
directions|一直行。|곧장 가세요.|jat1 zik6 haang4
directions|轉左。|왼쪽으로 도세요.|zyun3 zo2
directions|轉右。|오른쪽으로 도세요.|zyun3 jau6
directions|唔該，喺地圖指俾我睇。|지도에서 가리켜 주세요.|m4 goi1 hai2 dei6 tou4 zi2 bei2 ngo5 tai2
stay|我訂咗房。|방을 예약했어요.|ngo5 deng6 zo2 fong2
stay|我想辦理入住。|체크인하고 싶어요.|ngo5 soeng2 baan6 lei5 jap6 zyu6
stay|Wi-Fi密碼係咩？|와이파이 비밀번호가 뭔가요?|wai1 fai1 mat6 maa5 hai6 me1
stay|幾點食早餐？|아침 식사는 몇 시예요?|gei2 dim2 sik6 zou2 caan1
stay|我住兩晚。|이틀 밤 머물 거예요.|ngo5 zyu6 loeng5 maan5
help|我需要幫手。|도움이 필요해요.|ngo5 seoi1 jiu3 bong1 sau2
help|我蕩失路。|길을 잃었어요.|ngo5 dong6 sat1 lou6
help|我唔舒服。|몸이 좋지 않아요.|ngo5 m4 syu1 fuk6
help|藥房喺邊度？|약국이 어디예요?|joek6 fong4 hai2 bin1 dou6
help|唔該，叫救護車。|구급차를 불러 주세요.|m4 goi1 giu3 gau3 wu6 ce1
time|而家幾點？|지금 몇 시예요?|ji4 gaa1 gei2 dim2
time|我今日有時間。|오늘은 시간이 있어요.|ngo5 gam1 jat6 jau5 si4 gaan3
time|聽日見。|내일 봐요.|ting1 jat6 gin3
time|落雨喇。|비가 오네요.|lok6 jyu5 laa3
time|好凍。|추워요.|hou2 dung3'''
}

WORDS={
'dutch':'''water|물
thee|차
koffie|커피
melk|우유
brood|빵
kaas|치즈
appel|사과
rijst|쌀 / 밥
huis|집
school|학교
boek|책
pen|펜
fiets|자전거
trein|기차
bus|버스
station|역
vriend|친구 (남성)
vriendin|친구 (여성)
familie|가족
kind|아이
dag|날 / 낮
nacht|밤
vandaag|오늘
morgen|내일
links|왼쪽
rechts|오른쪽
groot|큰
klein|작은
goed|좋은
mooi|아름다운
een|하나
twee|둘
drie|셋
vier|넷
vijf|다섯
zes|여섯
zeven|일곱
acht|여덟
negen|아홉
tien|열''',
'polish':'''woda|물
herbata|차
kawa|커피
mleko|우유
chleb|빵
ser|치즈
jabłko|사과
ryż|쌀 / 밥
dom|집
szkoła|학교
książka|책
długopis|펜
rower|자전거
pociąg|기차
autobus|버스
dworzec|역
przyjaciel|친구 (남성)
przyjaciółka|친구 (여성)
rodzina|가족
dziecko|아이
dzień|날 / 낮
noc|밤
dzisiaj|오늘
jutro|내일
lewo|왼쪽
prawo|오른쪽
duży|큰 (남성형)
mały|작은 (남성형)
dobry|좋은 (남성형)
piękny|아름다운 (남성형)
jeden|하나
dwa|둘
trzy|셋
cztery|넷
pięć|다섯
sześć|여섯
siedem|일곱
osiem|여덟
dziewięć|아홉
dziesięć|열''',
'swedish':'''vatten|물
te|차
kaffe|커피
mjölk|우유
bröd|빵
ost|치즈
äpple|사과
ris|쌀 / 밥
hus|집
skola|학교
bok|책
penna|펜
cykel|자전거
tåg|기차
buss|버스
station|역
vän|친구
familj|가족
barn|아이
ö|섬
dag|날 / 낮
natt|밤
idag|오늘
imorgon|내일
vänster|왼쪽
höger|오른쪽
stor|큰
liten|작은
bra|좋은 / 잘
vacker|아름다운
ett|하나 (ett형)
två|둘
tre|셋
fyra|넷
fem|다섯
sex|여섯
sju|일곱
åtta|여덟
nio|아홉
tio|열''',
'cantonese':'''水|물|seoi2
茶|차|caa4
咖啡|커피|gaa3 fe1
牛奶|우유|ngau4 naai5
麵包|빵|min6 baau1
蘋果|사과|ping4 gwo2
飯|밥|faan6
屋企|집|uk1 kei2
學校|학교|hok6 haau6
書|책|syu1
筆|펜 / 붓|bat1
單車|자전거|daan1 ce1
火車|기차|fo2 ce1
巴士|버스|baa1 si2
車站|역 / 정류장|ce1 zaam6
朋友|친구|pang4 jau5
小朋友|아이|siu2 pang4 jau5
香港|홍콩|hoeng1 gong2
廣東話|광둥어|gwong2 dung1 waa2
今日|오늘|gam1 jat6
聽日|내일|ting1 jat6
左|왼쪽|zo2
右|오른쪽|jau6
大|큰|daai6
細|작은|sai3
好|좋은|hou2
食飯|밥을 먹다|sik6 faan6
飲水|물을 마시다|jam2 seoi2
一|하나|jat1
二|둘|ji6
三|셋|saam1
四|넷|sei3
五|다섯|ng5
六|여섯|luk6
七|일곱|cat1
八|여덟|baat3
九|아홉|gau2
十|열|sap6
早晨|좋은 아침|zou2 san4
再見|다시 만나요|zoi3 gin3'''
}

META={
'indonesian':{'ko':'인도네시아어','native':'Bahasa Indonesia','locale':'id-ID','accent':'#18766d','alphabet':'abcdefghijklmnopqrstuvwxyz','special':'','country':'인도네시아','intro':'인사부터 작은 대화까지, 한 글자씩 시작해요.','sources':[{'label':'인도네시아 교육부 BIPA 학습 자료','url':'https://bipa.kemendikdasmen.go.id/belajar'}]},
'cantonese':{'ko':'광둥어','native':'廣東話','locale':'zh-HK','accent':'#a65432','alphabet':'一二三四五六七八九十人大小口日月水火天中我你好早多食飲係唔謝見','special':'','country':'홍콩','intro':'번체자를 쓰고, 월병 표기로 소리와 성조를 익혀요.','sources':[{'label':'홍콩중문대 광둥어 학습 자료','url':'https://www.ilc.cuhk.edu.hk/en/chresources/indept_resources.aspx'},{'label':'홍콩중문대 월병 표기 학습','url':'https://ling.cuhk.edu.hk/jyutpingteaching/typing_10weeks.pdf'}]},
'dutch':{'ko':'네덜란드어','native':'Nederlands','locale':'nl-NL','accent':'#a6502c','alphabet':'abcdefghijklmnopqrstuvwxyz','special':'','country':'네덜란드','intro':'알파벳에서 운하 옆 카페의 첫 대화까지.','sources':[{'label':'네덜란드어 연합 Taalunie','url':'https://taalunie.org/'},{'label':'네덜란드어 철자 사전','url':'https://woordenlijst.org/'}]},
'polish':{'ko':'폴란드어','native':'Polski','locale':'pl-PL','accent':'#9b3c58','alphabet':'aąbcćdeęfghijklłmnńoóprsśtuwyzźż','special':'ąćęłńóśźżĄĆĘŁŃÓŚŹŻ','country':'폴란드','intro':'작은 부호까지 또박또박, 인사부터 자신 있게.','sources':[{'label':'폴란드어 학습·문법 polski.info','url':'https://polski.info/grammar/nouns?hl=pl'},{'label':'폴란드어 문자 체계 · UNGEGN','url':'https://unstats.un.org/unsd/geoinfo/ungegn/docs/_data_ICAcourses/_pdf/selfstudy/s14/S14_merge_total.pdf'}]},
'swedish':{'ko':'스웨덴어','native':'Svenska','locale':'sv-SE','accent':'#526d91','alphabet':'abcdefghijklmnopqrstuvwxyzåäö','special':'åäöÅÄÖ','country':'스웨덴','intro':'å·ä·ö를 쓰고, 일상 속 짧은 대화를 시작해요.','sources':[{'label':'스웨덴 한림원 사전 svenska.se','url':'https://svenska.se/'},{'label':'스웨덴 언어·민속 연구소 Isof','url':'https://www.isof.se/'}]}
}

NOTES={
'indonesian':[
['a·i·u·e·o를 먼저','i는 /i/, u는 /u/로 읽습니다. e는 단어에 따라 /ə/ 또는 /e~ɛ/여서 같은 글자가 다른 소리를 냅니다.','enak · empat'],
['ng·ny·sy는 함께 읽어요','ng는 받침 ㅇ 같은 /ŋ/, ny는 /ɲ/, sy는 /ʃ/에 가깝습니다. 한글 표기는 소리를 완전히 담지 못하므로 단어 음성도 함께 들어 보세요.','orang · banyak · syarat'],
['저는 …입니다','Saya 뒤에 이름·직업·출신을 놓아 자기소개할 수 있습니다. 영어의 be동사에 해당하는 말을 매번 넣지는 않습니다.','Saya Min. / Saya dari Korea.'],
['tidak와 bukan','동사·형용사의 부정에는 보통 tidak, 명사 확인의 부정에는 보통 bukan을 씁니다.','Saya tidak mengerti. / Saya bukan guru.'],
['공손하게 부탁하기','Tolong은 도움이나 행동을 부탁할 때, permisi는 말을 걸거나 지나갈 때 씁니다. Pak·Bu 같은 호칭도 상황에 맞게 사용합니다.','Tolong pelan-pelan. / Permisi.'],
['시간을 나타내는 말','동사가 영어처럼 시제마다 형태를 바꾸지는 않습니다. sudah(이미), sedang(…하는 중), akan(…할 예정)이나 시간 표현을 덧붙입니다.','Saya sudah makan. / Besok saya pergi.']],
'cantonese':[
['월병 숫자는 성조','월병(Jyutping)은 음절 뒤의 1~6으로 성조를 적습니다. 같은 철자라도 숫자가 달라지면 다른 말이 될 수 있습니다. 숫자를 빼지 않고 함께 읽으세요.','si1 · si2 · si3 · si4 · si5 · si6'],
['성조의 높낮이','홍콩 광둥어의 대표적인 설명에서 1은 높게 평평하게, 2는 올라가게, 3은 중간 높이, 4는 낮아지게, 5는 낮게 시작해 올라가게, 6은 낮게 평평하게 읽습니다. 실제 음성의 억양도 함께 들어 보세요.','詩 si1 · 史 si2 · 試 si3 · 時 si4 · 市 si5 · 事 si6'],
['번체자와 구어체','이 과정은 홍콩에서 쓰는 번체자와 광둥어 구어체를 씁니다. 我係…와 같은 표현은 보통화의 我是…와 표기·발음이 다릅니다.','我係韓國人。 ngo5 hai6 hon4 gwok3 jan4'],
['감사 표현 두 가지','작은 도움·서비스에는 唔該를, 선물이나 큰 호의에는 多謝를 주로 씁니다. 상황에 맞는 예문을 함께 외우세요.','唔該 m4 goi1 / 多謝 do1 ze6'],
['긍정·부정으로 질문','동사나 형용사를 긍정+부정으로 되풀이해 질문할 수 있습니다. 有冇, 係唔係, 識唔識 같은 꼴을 익히세요.','有冇…？ jau5 mou5 / 係唔係？ hai6 m4 hai6'],
['위치는 喺','있거나 위치한다는 말은 喺 hai2, …이다는 말은 係 hai6입니다. 모양과 성조가 모두 다릅니다.','廁所喺邊度？ ci3 so2 hai2 bin1 dou6']],
'dutch':[
['ij는 i와 j를 함께','ij는 두 글자로 적는 모음 결합입니다. 단어 첫머리를 대문자로 적을 때는 두 글자를 함께 IJ로 씁니다. y로 바꾸지 않습니다.','ijs → IJs / IJsselmeer'],
['길고 짧은 모음','단모음·장모음과 음절의 열림·닫힘이 철자에 영향을 줍니다. aa·ee·oo·uu와 단일 모음을 단어째 비교해 보세요.','man / maan · bom / boom'],
['u와 je','u는 공손한 상대 호칭이고, je·jij는 친근한 호칭입니다. 처음 만난 상대에게 공손하게 부탁할 때 Kunt u…?를 쓸 수 있습니다.','Kunt u dat herhalen?'],
['평서문의 동사 위치','기본 평서문에서는 활용된 동사가 두 번째 문장 성분 자리에 옵니다. 시간 표현을 앞에 두면 주어가 동사 뒤로 갑니다.','Ik leer Nederlands. / Vandaag leer ik Nederlands.'],
['de와 het를 같이 외워요','명사는 de 또는 het와 묶어 외우면 좋습니다. 복수 명사의 정관사는 de입니다.','de fiets · het huis · de huizen'],
['주문은 graag와 함께','Ik wil graag…로 원하는 것을 말하고 alstublieft로 공손하게 덧붙일 수 있습니다.','Ik wil graag een koffie.']],
'polish':[
['32개 글자','폴란드어의 기본 알파벳은 32자입니다. q·v·x는 외래 이름이나 일부 외래어에서 보일 수 있지만 기본 32자에 포함하지 않습니다.','ą ć ę ł ń ó ś ź ż'],
['부호도 글자의 일부','ą와 a, ł와 l, ż와 ź는 서로 다른 글자입니다. 따라 쓰기와 받아쓰기에서 부호까지 확인합니다.','l / ł · z / ź / ż'],
['자주 만나는 소리 결합','sz·cz·rz·ch·dz·dź·dż는 자주 함께 읽는 결합입니다. ć·ś·ź·ń처럼 부드러운 자음과 구별해 단어째 들으세요.','szkoła · cześć · dzień'],
['pan과 pani','남성에게 공손하게 말할 때 pan, 여성에게 pani를 씁니다. 동사 형태도 친근한 ty와 다르므로 문장째 익힙니다.','Czy mówi pan po angielsku? / Czy mówi pani po angielsku?'],
['명사의 형태가 바뀌어요','명사는 문장에서 하는 역할에 따라 형태가 달라집니다. 기본형 kawa가 주문 문장 Poproszę kawę에서는 kawę가 됩니다.','kawa → Poproszę kawę.'],
['자기소개 세 문장','이름은 Mam na imię…, 출신은 Jestem z…, 학습 중인 언어는 Uczę się…로 시작해 보세요.','Mam na imię Min. / Uczę się polskiego.']],
'swedish':[
['å·ä·ö는 독립된 글자','스웨덴어 알파벳은 a~z 다음에 å·ä·ö가 오는 29자입니다. a·o에 붙은 장식으로 생각하지 말고 별개 글자로 익히세요.','åtta · äpple · ö'],
['긴 모음과 긴 자음','강세 있는 음절에서 모음과 뒤 자음의 길이가 뜻을 구별할 수 있습니다. 철자만으로 단정하지 말고 음성을 함께 들으세요.','tak / tack'],
['동사는 인칭에 따라 그대로','현재형에서는 주어가 jag·du·vi로 바뀌어도 동사 형태가 같습니다.','jag talar / du talar / vi talar'],
['en과 ett를 함께','명사를 en·ett와 함께 외우세요. 정관사는 보통 명사 뒤에 붙습니다.','en bok → boken / ett hus → huset'],
['평서문의 동사 위치','기본 평서문에서는 활용된 동사가 두 번째 문장 성분 자리에 옵니다. 시간 표현을 먼저 말하면 주어가 뒤로 갑니다.','Jag har tid idag. / Idag har jag tid.'],
['tack와 공손한 요청','주문 뒤에 tack을 붙이거나 Kan jag få…?로 부탁할 수 있습니다.','En kaffe, tack. / Kan jag få notan?']]
}

# Dialogues use indices into authored phrases, with original short replies.
DIALOGUES={
'dutch':[
['첫 만남',[('A','Hallo!','안녕하세요!'),('B','Hallo! Hoe heet je?','안녕하세요! 이름이 뭐예요?'),('A','Ik heet Min. En jij?','저는 민이에요. 당신은요?'),('B','Ik heet Emma. Aangenaam.','저는 엠마예요. 반가워요.')]],
['카페 주문',[('A','Goedemorgen. Wat wilt u drinken?','안녕하세요. 무엇을 마시겠어요?'),('B','Een koffie, alstublieft.','커피 한 잔 주세요.'),('A','Met melk?','우유를 넣을까요?'),('B','Nee, zonder melk. Dank u wel.','아니요. 우유는 빼 주세요. 감사합니다.')]],
['길 묻기',[('A','Sorry, waar is het station?','실례합니다. 역이 어디예요?'),('B','Ga rechtdoor en sla linksaf.','곧장 가서 왼쪽으로 도세요.'),('A','Is het ver?','먼가요?'),('B','Nee, ongeveer vijf minuten lopen.','아니요. 걸어서 약 5분이에요.')]],
['계산하기',[('A','Hoeveel kost dit?','이것은 얼마예요?'),('B','Vijf euro.','5유로예요.'),('A','Kan ik met een kaart betalen?','카드로 계산할 수 있나요?'),('B','Ja, natuurlijk.','네, 물론이에요.')]],
['기차 타기',[('A','Hoe laat vertrekt de trein?','기차는 몇 시에 출발해요?'),('B','Om tien uur.','10시에요.'),('A','Op welk spoor?','몇 번 승강장인가요?'),('B','Op spoor twee.','2번 승강장이에요.')]],
['체크인',[('A','Ik heb een reservering.','예약했어요.'),('B','Op welke naam?','어떤 이름으로 예약하셨어요?'),('A','Op naam van Min.','민이라는 이름으로요.'),('B','Welkom!','환영합니다!')]],
['도움 요청',[('A','Ik begrijp het niet.','이해하지 못했어요.'),('B','Zal ik het herhalen?','다시 말해 드릴까요?'),('A','Ja, graag. Langzamer, alstublieft.','네, 부탁드려요. 조금 천천히요.'),('B','Natuurlijk.','물론이에요.')]],
['내일 약속',[('A','Heb je morgen tijd?','내일 시간 있어요?'),('B','Ja, in de middag.','네, 오후에요.'),('A','Zullen we koffie drinken?','커피 마실까요?'),('B','Goed idee. Tot morgen!','좋아요. 내일 봐요!')]]],
'polish':[
['첫 만남',[('A','Cześć! Jak masz na imię?','안녕! 이름이 뭐예요?'),('B','Mam na imię Min. A ty?','저는 민이에요. 당신은요?'),('A','Mam na imię Anna.','저는 안나예요.'),('B','Miło mi.','반가워요.')]],
['카페 주문',[('A','Dzień dobry. Co podać?','안녕하세요. 무엇을 드릴까요?'),('B','Poproszę kawę.','커피 한 잔 주세요.'),('A','Z mlekiem?','우유를 넣을까요?'),('B','Tak, proszę.','네, 부탁해요.')]],
['길 묻기',[('A','Przepraszam, gdzie jest dworzec?','실례합니다. 역이 어디예요?'),('B','Proszę iść prosto.','곧장 가세요.'),('A','Czy to daleko?','먼가요?'),('B','Nie, pięć minut pieszo.','아니요. 걸어서 5분이에요.')]],
['계산하기',[('A','Ile to kosztuje?','이것은 얼마예요?'),('B','Dziesięć złotych.','10즈워티예요.'),('A','Czy mogę zapłacić kartą?','카드로 계산할 수 있나요?'),('B','Tak, proszę.','네, 그렇게 하세요.')]],
['기차 타기',[('A','O której odjeżdża pociąg?','기차는 몇 시에 출발해요?'),('B','O dziesiątej.','10시에요.'),('A','Z którego peronu?','몇 번 승강장에서 출발하나요?'),('B','Z peronu drugiego.','2번 승강장에서요.')]],
['체크인',[('A','Mam rezerwację.','예약했어요.'),('B','Na jakie nazwisko?','성함이 어떻게 되세요?'),('A','Kim.','김입니다.'),('B','Proszę bardzo.','여기 있습니다.')]],
['천천히 부탁하기',[('A','Nie rozumiem.','이해하지 못했어요.'),('B','Powtórzyć?','다시 말할까요?'),('A','Tak. Proszę mówić wolniej.','네. 천천히 말씀해 주세요.'),('B','Dobrze.','알겠어요.')]],
['내일 약속',[('A','Masz jutro czas?','내일 시간 있어요?'),('B','Tak, po południu.','네, 오후에요.'),('A','Może kawa?','커피 한잔할까요?'),('B','Chętnie. Do jutra!','좋아요. 내일 봐요!')]]],
'swedish':[
['첫 만남',[('A','Hej! Vad heter du?','안녕하세요! 이름이 뭐예요?'),('B','Jag heter Min. Och du?','저는 민이에요. 당신은요?'),('A','Jag heter Elsa.','저는 엘사예요.'),('B','Trevligt att träffas.','반가워요.')]],
['카페 주문',[('A','Hej! Vad vill du ha?','안녕하세요! 무엇을 드릴까요?'),('B','En kaffe, tack.','커피 한 잔 주세요.'),('A','Vill du ha mjölk?','우유를 넣으시겠어요?'),('B','Nej tack, utan mjölk.','아니요. 우유는 빼 주세요.')]],
['길 묻기',[('A','Ursäkta, var ligger stationen?','실례합니다. 역이 어디예요?'),('B','Gå rakt fram och sväng höger.','곧장 가서 오른쪽으로 도세요.'),('A','Är det långt?','먼가요?'),('B','Nej, fem minuter till fots.','아니요. 걸어서 5분이에요.')]],
['계산하기',[('A','Vad kostar det?','이것은 얼마예요?'),('B','Tjugo kronor.','20크로나예요.'),('A','Kan jag betala med kort?','카드로 계산할 수 있나요?'),('B','Ja, det går bra.','네, 괜찮아요.')]],
['기차 타기',[('A','När går tåget?','기차는 언제 출발해요?'),('B','Klockan tio.','10시에요.'),('A','Från vilket spår?','몇 번 승강장에서 출발하나요?'),('B','Från spår två.','2번 승강장이에요.')]],
['체크인',[('A','Jag har en bokning.','예약했어요.'),('B','Vad heter du?','성함이 어떻게 되세요?'),('A','Jag heter Min Kim.','제 이름은 민 김이에요.'),('B','Välkommen!','환영합니다!')]],
['천천히 부탁하기',[('A','Jag förstår inte.','이해하지 못했어요.'),('B','Ska jag säga det igen?','다시 말해 드릴까요?'),('A','Ja, lite långsammare, tack.','네, 조금 천천히 부탁해요.'),('B','Självklart.','물론이에요.')]],
['내일 약속',[('A','Har du tid imorgon?','내일 시간 있어요?'),('B','Ja, på eftermiddagen.','네, 오후에요.'),('A','Ska vi ta en fika?','커피 한잔하며 쉴까요?'),('B','Gärna! Vi ses imorgon.','좋아요! 내일 봐요.')]]],
'cantonese':[
['첫 만남',[('A','你好。','안녕하세요.','nei5 hou2'),('B','你好，你叫咩名？','안녕하세요. 이름이 뭐예요?','nei5 hou2 nei5 giu3 me1 meng2'),('A','我叫阿明。','제 이름은 아밍이에요.','ngo5 giu3 aa3 ming4'),('B','好高興識你。','만나서 반가워요.','hou2 gou1 hing3 sik1 nei5')]],
['차 주문',[('A','飲咩呀？','무엇을 마실래요?','jam2 me1 aa3'),('B','唔該，一杯茶。','차 한 잔 주세요.','m4 goi1 jat1 bui1 caa4'),('A','熱嘅定凍嘅？','뜨거운 것으로요, 차가운 것으로요?','jit6 ge3 ding6 dung3 ge3'),('B','熱嘅，唔該。','뜨거운 것으로 주세요.','jit6 ge3 m4 goi1')]],
['길 묻기',[('A','唔該，車站喺邊度？','실례합니다. 역이 어디예요?','m4 goi1 ce1 zaam6 hai2 bin1 dou6'),('B','一直行，轉左。','곧장 가서 왼쪽으로 도세요.','jat1 zik6 haang4 zyun3 zo2'),('A','遠唔遠？','먼가요?','jyun5 m4 jyun5'),('B','唔遠。','멀지 않아요.','m4 jyun5')]],
['계산하기',[('A','呢個幾多錢？','이것은 얼마예요?','ni1 go3 gei2 do1 cin2'),('B','二十蚊。','20달러예요.','ji6 sap6 man1'),('A','可唔可以用信用卡？','신용카드를 쓸 수 있나요?','ho2 m4 ho2 ji5 jung6 seon3 jung6 kaat1'),('B','可以。','가능해요.','ho2 ji5')]],
['버스 확인',[('A','呢架巴士去唔去中環？','이 버스는 중완에 가나요?','ni1 gaa3 baa1 si2 heoi3 m4 heoi3 zung1 waan4'),('B','去。','가요.','heoi3'),('A','要幾耐？','얼마나 걸려요?','jiu3 gei2 noi6'),('B','大概十分鐘。','약 10분이에요.','daai6 koi3 sap6 fan1 zung1')]],
['감사 표현',[('A','呢份禮物送俾你。','이 선물을 드릴게요.','ni1 fan6 lai5 mat6 sung3 bei2 nei5'),('B','多謝。','감사합니다.','do1 ze6'),('A','唔使客氣。','천만에요.','m4 sai2 haak3 hei3'),('B','我好鍾意。','정말 마음에 들어요.','ngo5 hou2 zung1 ji3')]],
['천천히 부탁하기',[('A','我唔明。','이해하지 못했어요.','ngo5 m4 ming4'),('B','你想我再講一次？','다시 한 번 말해 줄까요?','nei5 soeng2 ngo5 zoi3 gong2 jat1 ci3'),('A','係，唔該講慢啲。','네. 천천히 부탁해요.','hai6 m4 goi1 gong2 maan6 di1'),('B','好。','좋아요.','hou2')]],
['내일 인사',[('A','你聽日有冇時間？','내일 시간 있어요?','nei5 ting1 jat6 jau5 mou5 si4 gaan3'),('B','有。','있어요.','jau5'),('A','聽日見。','내일 봐요.','ting1 jat6 gin3'),('B','好，拜拜。','좋아요. 잘 가요.','hou2 baai1 baai3')]]]
}

for key,meta in META.items():
 existing=json.loads((ROOT/'data'/f'{key}.json').read_text()) if key=='indonesian' and (ROOT/'data'/f'{key}.json').exists() else {}
 out={**existing,**meta,'key':key,'notes':[{'title':t,'text':body,'example':ex} for t,body,ex in NOTES[key]]}
 if key in PHRASES:
  out['phrases']=[]
  for i,line in enumerate(PHRASES[key].splitlines(),1):
   topic,text,meaning,*reading=line.split('|');out['phrases'].append({'id':f'{key}-p{i:03}','topic':topic,'text':text,'meaning':meaning,'reading':reading[0] if reading else ''})
  out['words']=[]
  for i,line in enumerate(WORDS[key].splitlines(),1):
   text,meaning,*reading=line.split('|');out['words'].append({'id':f'{key}-w{i:03}','topic':'words','text':text,'meaning':meaning,'reading':reading[0] if reading else ''})
  out['dialogues']=[{'id':f'{key}-d{i:02}','title':title,'lines':[{'who':row[0],'text':row[1],'meaning':row[2],'reading':row[3] if len(row)>3 else ''} for row in lines]} for i,(title,lines) in enumerate(DIALOGUES[key],1)]
 (ROOT/'data'/f'{key}.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Authored five language packs.')
