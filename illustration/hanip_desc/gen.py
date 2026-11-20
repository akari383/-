import random
random.seed(5)
T='file:///home/user/-/images/tex/'; IM='file:///home/user/-/images/hanip.jpg'
HEAD=f'''<!doctype html><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&family=Gaegu:wght@700&family=Hi+Melody&family=Nanum+Gothic+Coding:wght@400;700&family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:#000}}
.sc{{position:relative;width:540px;overflow:hidden;word-break:keep-all;background:radial-gradient(70% 50% at 30% 20%,#ffffff18,#0000),url({T}wood.jpg) 0 0/420px,#9a6a42}}
.o{{position:absolute}}
.pp{{background:url({T}paper.jpg) 0 0/256px,#f6f2ea}}
.sd{{filter:url(#rl) drop-shadow(0 1px 1px #0007) drop-shadow(0 3px 4px #0004) drop-shadow(0 16px 18px #0004)}}
.sd2{{filter:drop-shadow(0 1px 1px #0007) drop-shadow(0 3px 4px #0004) drop-shadow(0 14px 16px #0004)}}
.cv{{position:absolute;inset:0;pointer-events:none;background:linear-gradient(104deg,#00000012,#0000 16%,#ffffff22 44%,#0000 68%,#00000016)}}
.pn{{font-family:"Nanum Pen Script";color:#1f2c5c}}
.hm{{font-family:"Hi Melody";color:#2b2b2b}}
.mk{{font-family:"Gaegu";font-weight:700;color:#1d1d1d}}
.ty{{font-family:"Nanum Gothic Coding";color:#262626}}
.ns{{font-family:"Noto Sans KR"}}
.ink{{filter:url(#ink)}}
.tape{{position:absolute;z-index:5;background:url({T}tape.png) 0 0/100% 100%;filter:drop-shadow(0 1px 1px #0003)}}
.pen{{position:absolute;z-index:6;height:16px;border-radius:8px 3px 3px 8px;background:linear-gradient(#5a6fa8,#1d2a55 45%,#0e1633 80%,#28396e);filter:drop-shadow(3px 8px 6px #0006)}}
.pen::before{{content:"";position:absolute;left:-26px;top:3px;width:30px;height:10px;background:linear-gradient(#e9e9e9,#9a9a9a 60%,#cfcfcf);clip-path:polygon(0 50%,100% 0,100% 100%)}}
.pen::after{{content:"";position:absolute;right:30px;top:-3px;width:70px;height:6px;border-radius:3px;background:linear-gradient(#f5f5f5,#9b9b9b);box-shadow:0 1px 1px #0005}}
</style>
<svg width="0" height="0" style="position:absolute">
<filter id="rl" x="-10%" y="-10%" width="120%" height="120%" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency="0.006" numOctaves="2" seed="4" result="w"/>
<feDisplacementMap in="SourceGraphic" in2="w" scale="5" xChannelSelector="R" yChannelSelector="G" result="d"/>
<feTurbulence type="fractalNoise" baseFrequency="0.045" numOctaves="4" seed="8" result="n"/>
<feDiffuseLighting in="n" surfaceScale="1.3" lighting-color="#fff" result="l"><feDistantLight azimuth="225" elevation="68"/></feDiffuseLighting>
<feComponentTransfer in="l" result="l2"><feFuncR type="linear" slope="0.32" intercept="0.72"/><feFuncG type="linear" slope="0.32" intercept="0.72"/><feFuncB type="linear" slope="0.32" intercept="0.72"/></feComponentTransfer>
<feComposite in="d" in2="l2" operator="arithmetic" k1="1" k2="0" k3="0" k4="0" result="m"/>
<feComposite in="m" in2="d" operator="in"/>
</filter>
<filter id="ink"><feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="3" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="1.8"/><feGaussianBlur stdDeviation="0.22"/></filter>
<filter id="stp" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="2" seed="5" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.3 1.65" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in"/></filter>
</svg>'''
def torn(top=True,bottom=False,n=18,amp=1.6):
    pts=[]
    xs=[i*100/n for i in range(n+1)]
    tp=[f"{x:.1f}% {random.uniform(0,amp):.2f}%" for x in xs] if top else ["0 0","100% 0"]
    bt=[f"{x:.1f}% {100-random.uniform(0,amp):.2f}%" for x in reversed(xs)] if bottom else ["100% 100%","0 100%"]
    return "polygon("+",".join(tp+bt)+")"
shots={}
# 1 hero polaroid
shots['01']=(660,f'''
<div class="o sd" style="left:62px;top:58px;width:410px;padding:18px 18px 96px;transform:rotate(-3deg)"><div class="pp" style="position:absolute;inset:0;background-color:#fbfaf6"></div>
<div style="position:relative;aspect-ratio:1;background:url({IM}) 50% 30%/cover;filter:saturate(.86) contrast(1.03) sepia(.1) brightness(1.03);box-shadow:inset 0 0 0 1px #0003">
<div style="position:absolute;inset:0;background:linear-gradient(130deg,#ffffff40,#0000 34%),radial-gradient(#0000 62%,#00000030)"></div></div>
<div class="mk ink" style="position:absolute;left:26px;bottom:24px;font-size:46px;line-height:1;transform:rotate(-2deg)">한입이 (21)</div>
<div class="pn ink" style="position:absolute;right:24px;bottom:20px;font-size:27px;line-height:1.05;text-align:right">당근 주면<br>입양 고려함</div>
<div class="cv"></div></div>
<i class="tape" style="left:40px;top:44px;width:120px;height:32px;transform:rotate(-34deg)"></i><i class="tape" style="right:36px;top:40px;width:120px;height:32px;transform:rotate(28deg)"></i>
<div class="o ns" style="z-index:4;right:84px;top:92px;width:104px;height:104px;border-radius:50%;display:grid;place-items:center;text-align:center;font-weight:900;font-size:17px;line-height:1.2;color:#fff;background:radial-gradient(circle at 34% 28%,#ffb46a,#f07d22 55%,#d96410);transform:rotate(14deg);box-shadow:0 2px 3px #0006,0 6px 10px -4px #0005,inset 0 -3px 6px #0002,inset 0 2px 3px #fff6">입양 대기<br>1년 차</div>
<i class="pen" style="right:-60px;bottom:40px;width:300px;transform:rotate(-24deg)"></i>
''')
# 2 memo strip + ID badge
badge=f'''<div class="o sd2" style="left:64px;top:70px;width:412px;transform:rotate(-4deg)">
<div style="position:absolute;left:50%;top:-180px;width:40px;height:200px;margin-left:-20px;background:repeating-linear-gradient(90deg,#e8772a 0 3px,#d8681e 3px 6px);transform:rotate(10deg);transform-origin:bottom;box-shadow:inset 0 0 6px #0003"></div>
<div style="position:absolute;z-index:3;left:50%;top:-18px;width:58px;height:32px;margin-left:-29px;border-radius:7px;background:linear-gradient(#fbfbfb,#9a9a9a 55%,#dcdcdc);box-shadow:0 2px 3px #0006,inset 0 1px 0 #fff"></div>
<div style="position:relative;padding:11px;border-radius:18px;background:linear-gradient(135deg,#ffffff70,#ffffff30);box-shadow:inset 0 0 0 1px #fffa">
<div class="pp" style="border-radius:11px;overflow:hidden;background-color:#fff">
<div class="ns" style="display:flex;justify-content:space-between;padding:11px 16px;background:#ef7f26;color:#fff;font-weight:700;font-size:15px"><span>마포 수인보호센터</span><span>입양 대기 수인 등록증</span></div>
<div style="display:grid;grid-template-columns:110px 1fr;gap:14px;padding:14px 16px 10px">
<div style="height:138px;background:url({IM}) 50% 32%/cover;box-shadow:0 0 0 1px #0002;filter:saturate(.9)"></div>
<div class="ns" style="font-size:15px;line-height:1.75"><div><span style="color:#8a7f73;display:inline-block;width:52px">이름</span><b>한입이</b></div><div><span style="color:#8a7f73;display:inline-block;width:52px">종족</span><b>기니피그 수인</b></div><div><span style="color:#8a7f73;display:inline-block;width:52px">나이</span><b>21세 (성체 구조)</b></div><div><span style="color:#8a7f73;display:inline-block;width:52px">키</span><b>174cm</b></div><div><span style="color:#8a7f73;display:inline-block;width:52px">번호</span><b>No.0721</b></div></div></div>
<div class="ns" style="display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid #0000001f;text-align:center;font-size:12px;color:#8a7f73">
<div style="padding:8px 2px"><b style="display:block;font-size:20px;color:#e46d14">98%</b>배고픔(주장)</div><div style="padding:8px 2px;border-left:1px solid #0000001f"><b style="display:block;font-size:20px;color:#2b2622">0%</b>자립 의지</div><div style="padding:8px 2px;border-left:1px solid #0000001f"><b style="display:block;font-size:20px;color:#e46d14">D-92</b>자립 평가</div><div style="padding:8px 2px;border-left:1px solid #0000001f"><b style="display:block;font-size:20px;color:#2b2622">3곳</b>비밀 창고</div></div>
<div style="height:26px;margin:0 16px 12px;background:repeating-linear-gradient(90deg,#222 0 1px,#0000 1px 3px,#222 3px 5px,#0000 5px 6px,#222 6px 7px,#0000 7px 10px);opacity:.8"></div>
</div>
<div style="position:absolute;inset:0;border-radius:18px;background:linear-gradient(118deg,#0000 20%,#ffffff70 31%,#0000 42%,#0000 64%,#ffffff35 72%,#0000 80%)"></div>
</div></div>'''
shots['02']=(660,f'''
<div class="o sd" style="z-index:7;left:30px;top:500px;width:480px;padding:18px 22px 22px 56px;transform:rotate(2deg);clip-path:{torn(True,True)}">
<div class="pp" style="position:absolute;inset:0;background:linear-gradient(90deg,#0000 40px,#f0a7a7 40px 42px,#0000 42px),repeating-linear-gradient(#0000 0 37px,#b9cbe6 37px 38px) 0 16px,url({T}paper.jpg) 0 0/256px,#fbf9f3"></div>
<div class="pn ink" style="position:relative;font-size:29px;line-height:38px"><div>면담 메모 — "저 입양 안 해도 괜찮거든요."</div><div style="color:#c4372f">→ 당근 보자마자 "입양도 고려해 볼게요." (5초)</div></div><div class="cv"></div></div>
{badge}
''')
# 3 case file
shots['03']=(660,f'''
<div class="o sd" style="left:30px;top:70px;width:480px;height:540px;transform:rotate(1.5deg)">
<div style="position:absolute;left:0;top:-30px;width:200px;height:34px;border-radius:10px 10px 0 0;background:url({T}paper.jpg) 0 0/256px,#d8b47a;background-blend-mode:multiply"></div>
<div style="position:absolute;left:18px;top:-24px;padding:2px 10px;background:#fbfaf3" class="ty"><b style="font-size:15px">No.0721 · 한입이</b></div>
<div style="position:absolute;inset:0;border-radius:4px 12px 6px 6px;background:url({T}paper.jpg) 0 0/256px,#d8b47a;background-blend-mode:multiply"></div>
<div class="cv"></div>
<div class="pp" style="position:absolute;left:22px;top:26px;right:20px;bottom:26px;padding:24px 22px;background-color:#fbfaf6;transform:rotate(-1.4deg);box-shadow:0 2px 4px #0003,0 8px 12px -6px #0003">
<div class="ty" style="font-size:19px;font-weight:700;letter-spacing:.04em;padding-bottom:8px;border-bottom:2px solid #333;margin-bottom:12px">입양 대기 수인 상담 기록</div>
<div class="ty" style="font-size:15.5px;line-height:1.9;display:grid;grid-template-columns:92px 1fr;gap:4px 8px">
<span style="color:#777">대기 기간</span><span>1년 (면담 시 구석에 웅크림)</span>
<span style="color:#777">근무 이력</span><span><s style="color:#999">편의점</s> 진열대 과자 섭취<br><s style="color:#999">카페</s> 당근 케이크 섭취<br><s style="color:#999">물류센터</s> 근무 중 낮잠</span>
<span style="color:#777">동반 입양</span><span>두입이 (기니피그) <b class="pn ink" style="font-size:24px;font-weight:400">← 필수래요</b></span>
<span style="color:#777">특이사항</span><span>세상에서 제일 불쌍한 표정 보유</span></div>
<div class="ns" style="display:inline-block;margin-top:18px;padding:8px 14px;border:4px solid #d02f2f;border-radius:7px;color:#d02f2f;font-weight:900;font-size:24px;letter-spacing:.12em;transform:rotate(-9deg);opacity:.84;filter:url(#stp)">입양 대기</div>
<div class="cv"></div>
<div style="position:absolute;right:30px;top:-14px;width:20px;height:60px;border:3px solid #9aa0a6;border-radius:11px;box-shadow:1px 2px 2px #0004"><div style="position:absolute;left:2px;top:8px;width:8px;height:38px;border:2.5px solid #b4b9be;border-radius:7px"></div></div>
</div></div>
<div class="o sd2 pn" style="z-index:5;right:26px;bottom:34px;width:190px;padding:26px 16px 18px;background:linear-gradient(170deg,#0000 58%,#00000018),url({T}paper.jpg) 0 0/256px,#fbe57c;background-blend-mode:normal,multiply;font-size:31px;line-height:1.15;color:#2b2622;transform:rotate(6deg)"><span class="ink">불쌍한 척입니다.<br>— 박다정</span></div>
''')
# 4 index cards
cards=[("\"삐이이익!\"","배고프다. 밥 먹은 지 5분이어도."),("끄릉끄릉","기분 좋음. 본인은 모름."),("팝콘 점프","너무 기뻐서 통통. \"다리에 쥐 났어.\""),("이 딱딱","삐짐 or 질투. 주로 옆집 개 때문."),("얼음","먼저 다가가면 굳음. 곧 담요 속으로."),("담요 끌기","오늘 밤 주인 침대로 가겠다는 뜻.")]
cs=''
pos=[(46,96,-2.2),(282,90,2),(48,272,1.5),(280,268,-1.6),(46,446,-1),(284,444,2.2)]
for (t,b),(x,y,r) in zip(cards,pos):
    cs+=f'''<div class="o sd" style="left:{x}px;top:{y}px;width:210px;height:160px;padding:9px 12px;transform:rotate({r}deg)"><div class="pp" style="position:absolute;inset:0;background:linear-gradient(#0000 34px,#e88 34px 35px,#0000 35px),repeating-linear-gradient(#0000 0 27px,#b6c8e3 27px 28px) 0 35px,url({T}paper.jpg) 0 0/256px,#fffdf8"></div>
<div class="mk ink" style="position:relative;font-size:23px;line-height:24px">{t}</div><div class="pn ink" style="position:relative;margin-top:10px;font-size:24px;line-height:28px">{b}</div><div class="cv"></div></div>'''
shots['04']=(640,f'''
<div class="o mk" style="z-index:6;left:120px;top:26px;width:300px;padding:9px 0;text-align:center;font-size:27px;background:url({T}tape.png) 0 0/100% 100%;transform:rotate(-2deg);filter:drop-shadow(0 2px 2px #0003)"><span class="ink">한입이 사용 설명서</span></div>
{cs}''')
# 5 map
shots['05']=(580,f'''
<div class="o sd" style="left:28px;top:36px;width:470px;height:500px;padding:34px 22px 20px;transform:rotate(-1.2deg);clip-path:{torn(True,False,24,1.2)}">
<div class="pp" style="position:absolute;inset:0;background:linear-gradient(#a9c3e340 1px,#0000 1px) 0 0/16px 16px,linear-gradient(90deg,#a9c3e340 1px,#0000 1px) 0 0/16px 16px,url({T}paper.jpg) 0 0/256px,#fbfaf5"></div>
<div class="pn ink" style="position:relative;font-size:32px;margin-bottom:12px">비밀 식량 창고 지도 (추정)</div>
<div class="ink" style="position:relative;height:370px;border:3px solid #2b3a6bcc;border-radius:3px">
<i style="position:absolute;left:56%;top:-2px;height:62%;border-left:2.5px solid #2b3a6bbb"></i><i style="position:absolute;left:-2px;right:-2px;top:62%;border-top:2.5px solid #2b3a6bbb"></i><i style="position:absolute;left:36%;top:62%;bottom:-2px;border-left:2.5px solid #2b3a6bbb"></i>
<b class="pn" style="position:absolute;left:10px;top:6px;font-size:26px;font-weight:400">거실</b><b class="pn" style="position:absolute;left:59%;top:6px;font-size:26px;font-weight:400">부엌</b><b class="pn" style="position:absolute;left:10px;top:64%;font-size:26px;font-weight:400">현관</b><b class="pn" style="position:absolute;left:39%;top:64%;font-size:26px;font-weight:400">침실</b>
<b class="mk" style="position:absolute;left:24%;top:30%;font-size:40px;color:#d8312a">✕</b><span class="pn" style="position:absolute;left:33%;top:30%;font-size:24px;color:#b8302a">소파 담요 속</span>
<b class="mk" style="position:absolute;left:80%;top:18%;font-size:40px;color:#d8312a">✕</b><span class="pn" style="position:absolute;left:60%;top:34%;font-size:22px;line-height:1.05;color:#b8302a">냉장고 아래칸<br>(코 박음)</span>
<b class="mk" style="position:absolute;left:12%;top:74%;font-size:40px;color:#d8312a">✕</b><span class="pn" style="position:absolute;left:3%;top:88%;font-size:22px;color:#b8302a">신발장 운동화</span>
<b class="mk" style="position:absolute;left:58%;top:72%;font-size:40px;color:#d8312a">✕</b><span class="pn" style="position:absolute;left:44%;top:87%;font-size:22px;color:#b8302a">주인 가방 앞주머니</span>
<b class="mk" style="position:absolute;left:90%;top:70%;font-size:34px;color:#d8312a">?</b></div>
<div class="cv"></div></div>
<i class="o" style="z-index:6;left:300px;bottom:-30px;width:280px;height:26px;border-radius:12px 4px 4px 12px;background:linear-gradient(#ff7a6a,#d02f2f 45%,#8e1a14 85%,#c43a30);transform:rotate(-14deg);filter:drop-shadow(3px 8px 6px #0006)"></i>
''')
# 6 clipboard
rows=[("요리",0,"계란 태움 (일부러)"),("청소",None,"청소기 켜자 잠듦"),("장보기",1,"당근만 사 옴"),("생활 리듬",0,"낮잠 3회"),("애교",4,"평가 항목 아님;;")]
tr=''
for n,c,m in rows:
    dg=''.join((f'<span style="position:relative;display:inline-block;margin-right:4px">{g}<i class="ink" style="position:absolute;left:50%;top:50%;width:26px;height:24px;margin:-12px 0 0 -13px;border:2px solid #1f2c5c;border-radius:50% 44% 56% 47%;transform:rotate(-10deg)"></i></span>' if i==c else f'<span style="display:inline-block;margin-right:4px">{g}</span>') for i,g in enumerate('①②③④⑤'))
    tr+=f'<tr><td style="width:84px;background:#f1eee6;font-weight:700;text-align:center">{n}</td><td style="width:124px;color:#666;white-space:nowrap">{dg}</td><td class="pn ink" style="font-size:23px">{m}</td></tr>'
shots['06']=(610,f'''
<div class="o sd2" style="left:34px;top:40px;width:472px;height:540px;border-radius:14px;background:url({T}paper.jpg) 0 0/256px,#8f5f3a;background-blend-mode:multiply;transform:rotate(1.2deg)">
<div style="position:absolute;inset:0;border-radius:14px;background:linear-gradient(110deg,#ffffff14,#0000 40%,#0000001c)"></div>
<div class="pp sd" style="position:absolute;left:20px;right:20px;top:46px;bottom:22px;padding:22px 18px;background-color:#fdfcf8">
<div class="ns" style="text-align:center;font-weight:900;font-size:21px;letter-spacing:.2em">수인 자립 평가표</div>
<div class="ns" style="text-align:center;font-size:12.5px;color:#888;margin-bottom:12px">평가일 2027. 02. 21. (D-92) · 마포 수인보호센터</div>
<table class="ns" style="width:100%;border-collapse:collapse;font-size:15px">{tr.replace('<td','<td style="padding:9px 6px;border:1px solid #555"' ).replace('style="padding:9px 6px;border:1px solid #555" style="','style="padding:9px 6px;border:1px solid #555;')}</table>
<div class="pn ink" style="margin-top:16px;font-size:33px;color:#c8322b;transform:rotate(-2deg)">작전명: 적당히 무능해 보이기!!</div>
<div class="ns" style="text-align:right;font-size:13px;color:#777;margin-top:6px">평가자 <b class="pn ink" style="font-size:28px;font-weight:400;color:#1f2c5c">박다정</b></div>
<div class="cv"></div></div>
<div style="position:absolute;z-index:3;left:50%;top:-12px;width:170px;height:58px;margin-left:-85px;border-radius:12px 12px 20px 20px;background:linear-gradient(#fdfdfd,#b9b9b9 45%,#ececec 70%,#9c9c9c);box-shadow:0 4px 6px #0006,inset 0 1px 0 #fff"></div>
</div>
<i class="pen" style="left:-80px;bottom:24px;width:290px;transform:rotate(18deg)"></i>
''')
# 7 sticky notes
notes=[("#fbe57c","\"주인아.<br>나 배고파.\"",-3,50,94),("#f7b6c2","\"내가 그런 게 아니라 간식이 거기 있었어.\"",2.5,284,88),("#bfe6cc","\"나 이제 다 컸거든? ……근데 안아 줘.\"",2,52,318),("#fcc68a","\"나 사랑하지? 그럼 당근 하나만 더 줘.\"",-2,286,312)]
ns=''
for c,t,r,x,y in notes:
    ns+=f'<div class="o sd2 hm" style="left:{x}px;top:{y}px;width:204px;height:204px;padding:30px 18px 16px;background:linear-gradient(168deg,#0000 60%,#0000001c),url({T}paper.jpg) 0 0/256px,{c};background-blend-mode:normal,multiply;font-size:27px;line-height:1.3;transform:rotate({r}deg)"><span class="ink">{t}</span><div style="position:absolute;left:0;right:0;top:0;height:40px;background:linear-gradient(#ffffff26,#0000)"></div></div>'
shots['07']=(560,f'''<div class="o mk" style="z-index:6;left:150px;top:24px;width:240px;padding:9px 0;text-align:center;font-size:27px;background:url({T}tape.png) 0 0/100% 100%;transform:rotate(1.5deg);filter:drop-shadow(0 2px 2px #0003)"><span class="ink">자주 하는 말</span></div>{ns}''')
# 8 notebook
lines=[("✓","11/21 입양 — 당근 하나에 넘어옴",False),("","집안 실세 — ?",True),("","자립 평가 — 적당히, 적당히",True),("","혼자 자기 싫어 — ?",True),("","평생 얹혀살기 — ?",True)]
ls=''.join(f'<div style="display:flex;align-items:center;gap:12px;height:40px;color:{"#8c94ad" if d else "#1f2c5c"}"><i style="flex:none;width:20px;height:20px;border:2px solid #1f2c5c;display:grid;place-items:center;font:700 26px/1 Gaegu;font-style:normal;color:#c8322b">{c}</i>{t}</div>' for c,t,d in lines)
shots['08']=(520,f'''
<div class="o sd" style="left:34px;top:36px;width:472px;height:440px;padding:44px 20px 16px 62px;transform:rotate(-1deg)">
<div class="pp" style="position:absolute;inset:0;background:linear-gradient(90deg,#0000 46px,#f0a7a7 46px 48px,#0000 48px),repeating-linear-gradient(#0000 0 39px,#b9cbe6 39px 40px) 0 52px,url({T}paper.jpg) 0 0/256px,#fbf9f3"></div>
<div style="position:absolute;left:14px;right:14px;top:10px;height:18px;background:radial-gradient(circle,#5a3a20 5px,#0000 5.5px) 0 0/26px 18px repeat-x;opacity:.9"></div>
<div class="pn ink" style="position:relative;font-size:36px;line-height:52px">입양 일지</div>
<div class="pn ink" style="position:relative;font-size:27px">{ls}</div><div class="cv"></div></div>
''')
# 9 people + closing
shots['09']=(700,f'''
<div class="o sd" style="left:26px;top:40px;width:270px;height:156px;padding:18px;transform:rotate(-3deg)"><div class="pp" style="position:absolute;inset:0;background-color:#fff"></div>
<div class="ns" style="position:relative;display:flex;align-items:center;gap:7px;font-weight:700;font-size:13px;color:#ef7f26"><i style="width:16px;height:16px;border-radius:50%;background:#ef7f26"></i>마포 수인보호센터</div>
<div class="ns" style="position:relative;margin-top:10px;font-weight:700;font-size:20px;color:#222">박다정</div><div class="ns" style="position:relative;font-size:12.5px;color:#555">사후관리 복지사 · 한입이 담당</div>
<div class="pn ink" style="position:relative;margin-top:6px;text-align:right;font-size:25px;transform:rotate(-3deg)">입이 씨, 저 다 보여요.</div><div class="cv"></div></div>
<div class="o sd" style="left:330px;top:58px;width:180px;height:200px;padding:30px 14px 12px;text-align:center;transform:rotate(6deg);clip-path:polygon(20% 0,80% 0,100% 13%,100% 100%,0 100%,0 13%)"><div style="position:absolute;inset:0;background:url({T}paper.jpg) 0 0/256px,#c99a62;background-blend-mode:multiply"></div>
<i style="position:absolute;left:50%;top:10px;width:16px;height:16px;margin-left:-8px;border-radius:50%;background:#6a4a2a;box-shadow:inset 0 2px 3px #000a"></i>
<div class="ns" style="position:relative;font-weight:700;font-size:16px;line-height:1.5;color:#3a2a18">두입이<br>기니피그 · ♂<br>동반 입양 (필수)</div><div class="pn ink" style="position:relative;margin-top:6px;font-size:24px">한입이 동생 (자칭)</div><div class="cv"></div></div>
<i class="o" style="left:410px;top:-10px;width:3px;height:80px;background:linear-gradient(90deg,#b08a5a,#e0c08a,#9a7444);transform:rotate(14deg);box-shadow:1px 2px 2px #0004"></i>
<div class="o sd" style="left:46px;top:280px;width:448px;padding:22px 22px 30px;transform:rotate(1.4deg)"><div class="pp" style="position:absolute;inset:0;background:url({T}paper.jpg) 0 0/256px,#e6eefa;background-blend-mode:multiply"></div>
<div class="pn ink" style="position:relative;font-size:28px;line-height:1.3;color:#3b4a7a">택배 대신 받아 뒀어요! 언제든 놀러 오세요~<br>— 옆집 복실</div>
<div class="hm ink" style="position:absolute;right:44px;bottom:10px;font-size:38px;color:#d8312a;transform:rotate(-9deg)">가지 마</div><div class="cv"></div></div>
<div class="o sd" style="left:48px;top:470px;width:444px;padding:22px 26px;text-align:center;transform:rotate(-1.6deg);clip-path:{torn(True,True,16,4)}"><div class="pp" style="position:absolute;inset:0;background-color:#fbf9f3"></div>
<div class="pn ink" style="position:relative;font-size:33px;line-height:1.35">뻔뻔함 뒤에 숨긴 건,<br>다시 버려질까 봐 무서운 마음.</div><div class="cv"></div></div>
''')
for k,(h,body) in shots.items():
    open(f'shot{k}.html','w',encoding='utf-8').write(HEAD+f'<div class="sc" style="height:{h}px">'+body+'</div>')
print(list(shots))
