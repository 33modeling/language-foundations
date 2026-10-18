/*
 * 알파벳 인쇄체의 획 중심선. 채윤 독일어·프랑스어·스페인어가 같은 파일을 쓴다.
 *
 * 좌표는 1024 칸 정사각형, y는 아래로 커진다(SVG와 같다).
 *   대문자 위 170, 소문자 위 440, 기준선 800, 아래로 내려가는 획 끝 960.
 * 획 순서는 위에서 아래로, 왼쪽에서 오른쪽으로 쓰는 초등 인쇄체 관례를 따른다.
 * 둥근 획은 위에서 시작해 시계 반대 방향으로 돈다(o, c, a, d, g, q, e).
 * 각도는 y가 아래로 커지는 좌표에서 0=오른쪽, 90=아래, 180=왼쪽, 270=위이다.
 */
'use strict';

const STEP = 6;

function line(x1, y1, x2, y2) {
  const n = Math.max(2, Math.ceil(Math.hypot(x2 - x1, y2 - y1) / STEP));
  return Array.from({ length: n + 1 }, (_, i) => [x1 + (x2 - x1) * i / n, y1 + (y2 - y1) * i / n]);
}

// 각도가 커지면 화면에서 시계 방향, 작아지면 시계 반대 방향이다.
function arc(cx, cy, rx, ry, from, to) {
  const length = Math.abs(to - from) / 180 * Math.PI * Math.max(rx, ry);
  const n = Math.max(4, Math.ceil(length / STEP));
  return Array.from({ length: n + 1 }, (_, i) => {
    const a = (from + (to - from) * i / n) * Math.PI / 180;
    return [cx + rx * Math.cos(a), cy + ry * Math.sin(a)];
  });
}

function curve(p0, p1, p2, p3) {
  const rough = Math.hypot(p1[0] - p0[0], p1[1] - p0[1]) + Math.hypot(p2[0] - p1[0], p2[1] - p1[1]) + Math.hypot(p3[0] - p2[0], p3[1] - p2[1]);
  const n = Math.max(4, Math.ceil(rough / STEP));
  return Array.from({ length: n + 1 }, (_, i) => {
    const t = i / n;
    const u = 1 - t;
    return [0, 1].map((k) => u * u * u * p0[k] + 3 * u * u * t * p1[k] + 3 * u * t * t * p2[k] + t * t * t * p3[k]);
  });
}

// 이어지는 조각들을 한 획으로 붙인다.
function stroke(...parts) {
  const out = [];
  for (const part of parts) {
    for (const point of part) {
      const last = out[out.length - 1];
      if (!last || Math.hypot(point[0] - last[0], point[1] - last[1]) > 0.5) out.push(point);
    }
  }
  return out;
}

const X = 440;   // 소문자 위
const B = 800;   // 기준선
const T = 170;   // 대문자·올라가는 획 위
const D = 960;   // 내려가는 획 끝
const MID = 620; // 소문자 몸통 가운데
const CAP_MID = 485;


const LOWER = {
  a: () => [stroke(arc(470, MID, 160, 180, 330, 30)), line(630, X, 630, B)],
  b: () => [line(330, T, 330, B), stroke(arc(490, MID, 160, 180, 200, 520))],
  c: () => [stroke(arc(520, MID, 165, 180, 320, 40))],
  d: () => [stroke(arc(470, MID, 160, 180, 330, 30)), line(630, T, 630, B)],
  e: () => [stroke(line(355, MID, 685, MID), arc(520, MID, 165, 180, 360, 40))],
  f: () => [stroke(arc(560, 290, 100, 110, 330, 180), line(460, 290, 460, B)), line(350, X, 600, X)],
  g: () => [stroke(arc(470, MID, 160, 180, 330, 30)), stroke(line(630, X, 630, 860), arc(510, 860, 120, 100, 0, 150))],
  h: () => [line(340, T, 340, B), stroke(arc(500, 580, 160, 140, 180, 360), line(660, 580, 660, B))],
  i: () => [line(512, X, 512, B), line(512, 270, 512, 330)],
  j: () => [stroke(line(570, X, 570, 860), arc(450, 860, 120, 100, 0, 150)), line(570, 270, 570, 330)],
  k: () => [line(360, T, 360, B), line(650, X, 360, 650), line(455, 590, 660, B)],
  l: () => [line(512, T, 512, B)],
  m: () => [line(260, X, 260, B), stroke(arc(375, 570, 115, 130, 180, 360), line(490, 570, 490, B)), stroke(arc(605, 570, 115, 130, 180, 360), line(720, 570, 720, B))],
  n: () => [line(350, X, 350, B), stroke(arc(500, 580, 150, 140, 180, 360), line(650, 580, 650, B))],
  o: () => [stroke(arc(512, MID, 170, 180, 270, -90))],
  p: () => [line(340, X, 340, D), stroke(arc(500, MID, 160, 180, 200, 520))],
  q: () => [stroke(arc(470, MID, 160, 180, 330, 30)), line(630, X, 630, D)],
  r: () => [line(390, X, 390, B), stroke(arc(530, 580, 140, 140, 180, 305))],
  s: () => [stroke(
    curve([645, 495], [610, 440], [400, 420], [385, 515]),
    curve([385, 515], [372, 600], [650, 600], [655, 690]),
    curve([655, 690], [662, 800], [420, 820], [365, 750])
  )],
  t: () => [stroke(line(470, 260, 470, 720), arc(560, 720, 90, 80, 180, 75)), line(360, X, 600, X)],
  u: () => [stroke(line(350, X, 350, 640), arc(500, 640, 150, 160, 180, 0), line(650, 640, 650, X)), line(650, X, 650, B)],
  v: () => [stroke(line(330, X, 512, B), line(512, B, 694, X))],
  w: () => [stroke(line(250, X, 365, B), line(365, B, 512, 540), line(512, 540, 659, B), line(659, B, 774, X))],
  x: () => [line(345, X, 680, B), line(680, X, 345, B)],
  y: () => [line(345, X, 515, 790), line(690, X, 420, D)],
  z: () => [stroke(line(345, X, 680, X), line(680, X, 345, B), line(345, B, 680, B))],
  'ß': () => [stroke(
    line(340, B, 340, 330),
    arc(480, 330, 140, 155, 180, 360),
    curve([620, 330], [620, 415], [530, 450], [500, 470]),
    curve([500, 470], [700, 480], [720, 640], [665, 735]),
    curve([665, 735], [620, 805], [530, 815], [465, 790])
  )],
  'ı': () => [line(512, X, 512, B)],
  'œ': () => [stroke(arc(395, MID, 125, 180, 270, -90)), stroke(line(520, MID, 770, MID), arc(645, MID, 125, 180, 360, 40))],
  '¡': () => [line(512, 420, 512, 480), line(512, 580, 512, 940)],
  '¿': () => [line(512, 420, 512, 480), stroke(
    line(512, 580, 512, 660),
    curve([512, 660], [380, 690], [345, 790], [400, 860]),
    curve([400, 860], [470, 935], [630, 920], [675, 830])
  )]
};

const UPPER = {
  A: () => [line(512, T, 290, B), line(512, T, 734, B), line(372, 580, 652, 580)],
  B: () => [line(330, T, 330, B), stroke(line(330, T, 520, T), arc(520, 327.5, 150, 157.5, 270, 450), line(520, CAP_MID, 330, CAP_MID)),
    stroke(line(330, CAP_MID, 540, CAP_MID), arc(540, 642.5, 165, 157.5, 270, 450), line(540, B, 330, B))],
  C: () => [stroke(arc(535, CAP_MID, 245, 315, 320, 40))],
  D: () => [line(330, T, 330, B), stroke(line(330, T, 470, T), arc(470, CAP_MID, 240, 315, 270, 450), line(470, B, 330, B))],
  E: () => [line(345, T, 345, B), line(345, T, 680, T), line(345, CAP_MID, 630, CAP_MID), line(345, B, 680, B)],
  F: () => [line(355, T, 355, B), line(355, T, 680, T), line(355, CAP_MID, 630, CAP_MID)],
  G: () => [stroke(arc(530, CAP_MID, 245, 315, 320, 0)), line(590, CAP_MID, 775, CAP_MID)],
  H: () => [line(320, T, 320, B), line(704, T, 704, B), line(320, CAP_MID, 704, CAP_MID)],
  I: () => [line(512, T, 512, B)],
  J: () => [stroke(line(630, T, 630, 640), arc(475, 640, 155, 160, 0, 180))],
  K: () => [line(345, T, 345, B), line(700, T, 345, 565), line(460, 445, 710, B)],
  L: () => [stroke(line(350, T, 350, B), line(350, B, 680, B))],
  M: () => [line(265, T, 265, B), stroke(line(265, T, 512, 620), line(512, 620, 759, T)), line(759, T, 759, B)],
  N: () => [line(300, T, 300, B), line(300, T, 724, B), line(724, B, 724, T)],
  O: () => [stroke(arc(512, CAP_MID, 275, 315, 270, -90))],
  P: () => [line(340, T, 340, B), stroke(line(340, T, 530, T), arc(530, 335, 165, 165, 270, 450), line(530, 500, 340, 500))],
  Q: () => [stroke(arc(512, CAP_MID, 275, 315, 270, -90)), line(570, 640, 760, 850)],
  R: () => [line(340, T, 340, B), stroke(line(340, T, 530, T), arc(530, 335, 165, 165, 270, 450), line(530, 500, 340, 500)), line(500, 500, 700, B)],
  S: () => [stroke(
    curve([705, 260], [655, 165], [370, 155], [350, 300]),
    curve([350, 300], [330, 440], [705, 470], [705, 640]),
    curve([705, 640], [705, 805], [380, 835], [315, 705])
  )],
  T: () => [line(280, T, 744, T), line(512, T, 512, B)],
  U: () => [stroke(line(310, T, 310, 595), arc(512, 595, 202, 205, 180, 0), line(714, 595, 714, T))],
  V: () => [stroke(line(280, T, 512, B), line(512, B, 744, T))],
  W: () => [stroke(line(195, T, 340, B), line(340, B, 512, 340), line(512, 340, 684, B), line(684, B, 829, T))],
  X: () => [line(300, T, 724, B), line(724, T, 300, B)],
  Y: () => [line(290, T, 512, 500), line(734, T, 512, 500), line(512, 500, 512, B)],
  Z: () => [stroke(line(300, T, 724, T), line(724, T, 300, B), line(300, B, 724, B))]
};

// 강세 부호. cx는 바탕 글자의 가운데, top은 부호를 놓을 높이(소문자 300, 대문자 45).
const MARKS = {
  ogonek: (cx) => [stroke(curve([cx+60,B-10],[cx-100,B+100],[cx-30,990],[cx+80,930]))],
  ring: (cx,top) => [stroke(arc(cx,top+40,45,45,270,-90))],
  acute: (cx, top) => [line(cx + 45, top, cx - 35, top + 90)],
  grave: (cx, top) => [line(cx - 45, top, cx + 35, top + 90)],
  circumflex: (cx, top) => [stroke(line(cx - 85, top + 90, cx, top), line(cx, top, cx + 85, top + 90))],
  diaeresis: (cx, top) => [line(cx - 80, top + 20, cx - 80, top + 80), line(cx + 80, top + 20, cx + 80, top + 80)],
  tilde: (cx, top) => [stroke(curve([cx - 105, top + 75], [cx - 75, top + 5], [cx - 35, top + 15], [cx, top + 45]),
    curve([cx, top + 45], [cx + 35, top + 75], [cx + 75, top + 85], [cx + 105, top + 15]))],
  breve: (cx, top) => [stroke(arc(cx, top + 20, 72, 58, 180, 0))],
  dot: (cx, top) => [line(cx, top + 5, cx, top + 60)]
};

const COMPOSED = {
  'ą':['a','ogonek'],'Ą':['A','ogonek'],'ę':['e','ogonek'],'Ę':['E','ogonek'],
  'ć':['c','acute'],'Ć':['C','acute'],'ń':['n','acute'],'Ń':['N','acute'],
  'Ó':['O','acute'],'ś':['s','acute'],'Ś':['S','acute'],'ź':['z','acute'],'Ź':['Z','acute'],
  'ż':['z','dot'],'Ż':['Z','dot'],'å':['a','ring'],'Å':['A','ring'],
  'ä': ['a', 'diaeresis'], 'ö': ['o', 'diaeresis'], 'ü': ['u', 'diaeresis'],
  'Ä': ['A', 'diaeresis'], 'Ö': ['O', 'diaeresis'], 'Ü': ['U', 'diaeresis'],
  'é': ['e', 'acute'], 'è': ['e', 'grave'], 'ê': ['e', 'circumflex'], 'ë': ['e', 'diaeresis'],
  'à': ['a', 'grave'], 'â': ['a', 'circumflex'], 'î': ['ı', 'circumflex'], 'ï': ['ı', 'diaeresis'],
  'ô': ['o', 'circumflex'], 'û': ['u', 'circumflex'], 'ù': ['u', 'grave'],
  'É': ['E', 'acute'], 'È': ['E', 'grave'], 'Ê': ['E', 'circumflex'], 'À': ['A', 'grave'],
  'á': ['a', 'acute'], 'í': ['ı', 'acute'], 'ó': ['o', 'acute'], 'ú': ['u', 'acute'],
  'ñ': ['n', 'tilde'], 'Ñ': ['N', 'tilde'], 'ã': ['a', 'tilde'], 'õ': ['o', 'tilde'],
  'ì': ['ı', 'grave'], 'ò': ['o', 'grave'], 'ğ': ['g', 'breve'], 'Ğ': ['G', 'breve'], 'İ': ['I', 'dot']
};

function bounds(strokes) {
  const xs = strokes.flat().map((p) => p[0]);
  return [Math.min(...xs), Math.max(...xs)];
}

function base(ch) {
  const make = LOWER[ch] || UPPER[ch];
  if (!make) throw new Error(`No glyph for ${ch}`);
  return make();
}

function glyph(ch) {
  let strokes;
  if (COMPOSED[ch]) {
    const [letter, mark] = COMPOSED[ch];
    strokes = base(letter);
    const [left, right] = bounds(['a', 'u', 'g'].includes(letter) ? [strokes[0]] : strokes);
    const top = UPPER[letter] ? 45 : 295;
    strokes = strokes.concat(MARKS[mark]((left + right) / 2, top));
  } else if (ch === 'ç' || ch === 'Ç' || ch === 'ş' || ch === 'Ş') {
    strokes = base({ ç: 'c', Ç: 'C', ş: 's', Ş: 'S' }[ch]);
    const cx = { ç: 520, Ç: 535, ş: 515, Ş: 512 }[ch];
    strokes.push(stroke(line(cx, B, cx, 850), curve([cx, 850], [cx + 70, 850], [cx + 75, 925], [cx - 45, 935])));
  } else if(ch==='ł'||ch==='Ł'){
    strokes=base(ch==='ł'?'l':'L');strokes.push(line(370,650,650,470));
  } else if(ch==='-'){strokes=[line(350,600,675,600)];
  } else {
    strokes = base(ch);
  }
  // 글자 너비가 저마다 달라 가로 가운데를 512에 맞춘다.
  const [left, right] = bounds(strokes);
  const shift = 512 - (left + right) / 2;
  return strokes.map((points) => points.map(([x, y]) => [x + shift, y]));
}

module.exports = {
  glyph, line, arc, curve, stroke, MARKS,
  supported: [...Object.keys(LOWER), ...Object.keys(UPPER), ...Object.keys(COMPOSED), 'ç', 'Ç', 'ş', 'Ş']
};
