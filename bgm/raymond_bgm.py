"""레이먼드 정 BGM: 비 오는 밤의 누아르 재즈 (D minor, 70 BPM, swing), 루프용."""
import numpy as np
from scipy import signal
import sys

SR = 44100
BPM = 70
BEAT = 60 / BPM
BAR = 4 * BEAT
SW = 2 / 3                      # 스윙 8분음표 뒷박 위치
rng = np.random.default_rng(1119)

N_BARS = 24
TAIL_BARS = 2
TOTAL = int((N_BARS + TAIL_BARS) * BAR * SR)
LOOP = int(N_BARS * BAR * SR)

def mtof(m): return 440.0 * 2 ** ((m - 69) / 12)
def t_of(bar, beat): return (bar * 4 + beat) * BEAT

class Bus:
    def __init__(self): self.L = np.zeros(TOTAL); self.R = np.zeros(TOTAL)
    def add(self, x, start_s, pan=0.0, gain=1.0):
        i = int(start_s * SR)
        if i >= TOTAL: return
        x = x[:TOTAL - i] * gain
        l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
        self.L[i:i + len(x)] += x * l * 1.414; self.R[i:i + len(x)] += x * r * 1.414

def bp(x, lo, hi, order=2):
    sos = signal.butter(order, [lo, hi], btype='band', fs=SR, output='sos'); return signal.sosfilt(sos, x)
def lp(x, f, order=2):
    sos = signal.butter(order, f, btype='low', fs=SR, output='sos'); return signal.sosfilt(sos, x)
def hp(x, f, order=2):
    sos = signal.butter(order, f, btype='high', fs=SR, output='sos'); return signal.sosfilt(sos, x)

# ---------- 악기 ----------
def rhodes(m, dur, vel=0.7):
    f = mtof(m); n = int((dur + 1.6) * SR); t = np.arange(n) / SR
    dec = 1.2 + 2.2 * np.exp(-(m - 48) / 18)
    env = np.exp(-t / dec) * (1 - np.exp(-t / 0.002))
    rel = np.ones(n); off = int(dur * SR)
    if off < n: rel[off:] = np.exp(-np.arange(n - off) / (0.12 * SR))
    idx = (0.9 + 1.6 * vel) * np.exp(-t / 0.35)
    tine = 0.35 * vel * np.exp(-t / 0.04) * np.sin(2 * np.pi * f * 14 * t)
    y = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * t) + tine)
    y += 0.25 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / (dec * 0.5))
    return y * env * rel * vel

def bass(m, dur, vel=0.8):
    f = mtof(m); n = int((dur + 0.5) * SR); N = max(2, int(round(SR / f)))
    exc = np.zeros(n); burst = lp(rng.uniform(-1, 1, N), 900); burst[:88] *= np.linspace(0, 1, 88); exc[:N] = burst
    a = np.zeros(N + 2); a[0] = 1; a[N] = -0.4985; a[N + 1] = -0.4985
    y = signal.lfilter([1.0], a, exc)
    t = np.arange(n) / SR
    y += 0.6 * np.sin(2 * np.pi * f * t) * np.exp(-t / 0.9) * (1 - np.exp(-t / 0.004))
    off = int(dur * 0.92 * SR); rel = np.ones(n)
    if off < n: rel[off:] = np.exp(-np.arange(n - off) / (0.05 * SR))
    y = lp(y * rel, 1100)
    return y / (np.max(np.abs(y)) + 1e-9) * vel

def vibes(m, dur, vel=0.6):
    f = mtof(m); n = int((dur + 2.2) * SR); t = np.arange(n) / SR
    y = (np.sin(2 * np.pi * f * t) * np.exp(-t / 2.2)
         + 0.28 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t / 0.5)
         + 0.08 * np.sin(2 * np.pi * 10 * f * t) * np.exp(-t / 0.12))
    trem = 1 - 0.28 * (0.5 + 0.5 * np.sin(2 * np.pi * 5.2 * t))
    click = hp(rng.uniform(-1, 1, n), 3000) * np.exp(-t / 0.004) * 0.15
    off = int(dur * SR); rel = np.ones(n)
    if off < n: rel[off:] = np.exp(-np.arange(n - off) / (0.4 * SR))
    return (y * trem + click) * rel * vel

def ride(vel=0.5):
    n = int(1.4 * SR); t = np.arange(n) / SR
    frs = rng.uniform(2500, 12000, 48)
    y = sum(np.sin(2 * np.pi * fr * t + rng.uniform(0, 6)) * rng.uniform(.3, 1) for fr in frs) / 24
    y = 0.35 * y * np.exp(-t / 0.35) + 0.9 * bp(rng.uniform(-1, 1, n), 4000, 14000) * np.exp(-t / 0.45)
    return y * (1 - np.exp(-t / 0.001)) * vel

def brush_tap(vel=0.5):
    n = int(0.25 * SR); t = np.arange(n) / SR
    return bp(rng.uniform(-1, 1, n), 1200, 5500) * np.exp(-t / 0.07) * vel

def hat(vel=0.3):
    n = int(0.12 * SR); t = np.arange(n) / SR
    return hp(rng.uniform(-1, 1, n), 7000) * np.exp(-t / 0.03) * vel

def kick(vel=0.4):
    n = int(0.4 * SR); t = np.arange(n) / SR
    f = 55 + 40 * np.exp(-t / 0.03)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.18) * vel

# ---------- 화성 ----------
V = {  # 루트(베이스), 로즈 보이싱(루트리스)
 'Dm9': (38, [53, 57, 60, 64]), 'Gm9': (43, [58, 62, 65, 69]), 'A7b9': (45, [55, 58, 61, 64]),
 'Bbmaj7': (34, [53, 57, 62, 64]), 'Em7b5': (40, [55, 58, 62, 64]), 'Fmaj7': (41, [57, 60, 64, 67]),
}
A_SEC = [['Dm9'], ['Dm9'], ['Gm9'], ['A7b9'], ['Dm9'], ['Bbmaj7'], ['Em7b5'], ['A7b9']]
B_SEC = [['Fmaj7'], ['Bbmaj7'], ['Em7b5'], ['A7b9'], ['Dm9'], ['Gm9'], ['Em7b5', 'A7b9'], ['Dm9']]
FORM = A_SEC + B_SEC + A_SEC + [['Dm9'], ['Dm9']]   # 마지막 2마디는 꼬리(루프 앞에 겹침)

def chord_at(bar, beat):
    cs = FORM[bar]; return cs[0] if len(cs) == 1 or beat < 2 else cs[1]

keys, bas, mel, drm = Bus(), Bus(), Bus(), Bus()

# 로즈 컴핑
PATTERNS = [[(0, 1.6, .7), (1 + SW, .5, .55)], [(0, 2.6, .65), (3 + SW, .6, .5)],
            [(SW, 1.2, .6), (2 + SW, 1.0, .55)], [(0, 1.0, .7), (2, 1.6, .6)]]
for bar in range(N_BARS):
    pat = PATTERNS[(bar * 3 + bar // 4) % len(PATTERNS)]
    if len(FORM[bar]) == 2: pat = [(0, 1.6, .65), (2, 1.6, .6)]
    for bt, d, v in pat:
        root, voic = V[chord_at(bar, bt)]
        for k, m in enumerate(voic):
            keys.add(rhodes(m, d * BEAT, v * rng.uniform(.9, 1.05)), t_of(bar, bt) + k * 0.006, pan=-0.25 + k * 0.12, gain=0.16)

# 워킹 베이스
def walk(bar):
    out = []
    for beat in range(4):
        ch = chord_at(bar, beat); root = V[ch][0]
        nxt = V[chord_at(bar + 1, 0)][0] if bar + 1 < len(FORM) else V['Dm9'][0]
        tones = {'Dm9': [0, 3, 7, 10], 'Gm9': [0, 3, 7, 10], 'A7b9': [0, 4, 7, 10], 'Bbmaj7': [0, 4, 7, 11],
                 'Em7b5': [0, 3, 6, 10], 'Fmaj7': [0, 4, 7, 11]}[ch]
        if beat == 0 or (len(FORM[bar]) == 2 and beat == 2): m = root
        elif beat == 3: m = nxt + (1 if rng.random() < .5 else -1)
        else: m = root + tones[rng.integers(1, 4)] - (12 if rng.random() < .3 else 0)
        while m > 47: m -= 12
        while m < 28: m += 12
        out.append(m)
    return out
for bar in range(N_BARS):
    for beat, m in enumerate(walk(bar)):
        bas.add(bass(m, BEAT * 0.95, rng.uniform(.75, .9)), t_of(bar, beat), pan=0.05, gain=0.42)

# 브러시 드럼
for bar in range(N_BARS):
    for b in (0, 1, 1 + SW, 2, 3, 3 + SW):
        drm.add(ride(0.5 if b in (1 + SW, 3 + SW) else 0.65), t_of(bar, b), pan=0.35, gain=0.055)
    for b in (1, 3):
        drm.add(brush_tap(0.8), t_of(bar, b), pan=-0.1, gain=0.12); drm.add(hat(1), t_of(bar, b), pan=0.25, gain=0.05)
    for b in (0, 2):
        drm.add(kick(1), t_of(bar, b), gain=0.10)
sfade = int(0.5 * SR); sweep_n = LOOP + sfade; tt = np.arange(sweep_n) / SR
sweep = bp(rng.uniform(-1, 1, sweep_n), 1800, 6500) * (0.35 + 0.65 * (0.5 + 0.5 * np.sin(2 * np.pi * tt / BEAT - np.pi / 2)) ** 2)
sr_ = np.linspace(0, 1, sfade); sweep[:sfade] = sweep[:sfade] * sr_ + sweep[LOOP:LOOP + sfade] * (1 - sr_)
drm.add(sweep[:LOOP], 0, pan=-0.15, gain=0.022)

# 비브라폰 멜로디 (B: 9~16마디, A': 17~24마디)
MEL_B = [(0,0,2,76),(0,2+SW,1-SW,74),(0,3,1,72),(1,0,3,69),(1,3+SW,1-SW,67),(2,0,1,70),(2,1,1,69),(2,2,1,67),(2,3,1,65),
         (3,0,2,64),(3,2,1,61),(3,3,1,64),(4,0,1.5,65),(4,1+SW,1-SW,69),(4,2,2,72),(5,0,1,74),(5,1,SW,70),(5,1+SW,1.4,69),(5,3,1,67),
         (6,0,1,70),(6,1,1,67),(6,2,1,69),(6,3,1,73),(7,0,4,74)]
MEL_A2 = [(0,1,1,69),(0,2,2,77),(1,0,1,76),(1,1,1,74),(1,2,2,69),(2,0,3,70),(2,3,1,74),(3,0,1,73),(3,1,1,70),(3,2,2,69),
          (4,0,2,65),(4,2,1,69),(4,3,1,72),(5,0,3,74),(5,3,1,76),(6,0,2,74),(6,2,1,70),(6,3,1,67),(7,0,2,69),(7,2,2,73)]
for off, mel_list in ((8, MEL_B), (16, MEL_A2)):
    for b, bt, d, m in mel_list:
        mel.add(vibes(m, d * BEAT, rng.uniform(.55, .7)), t_of(off + b, bt), pan=0.15, gain=0.30)

# ---------- 믹스 ----------
def reverb_ir(sec=2.0, seed=7):
    r = np.random.default_rng(seed); n = int(sec * SR); t = np.arange(n) / SR
    ir = r.uniform(-1, 1, (2, n)) * np.exp(-t / (sec / 5))
    ir = np.stack([lp(ir[0], 6000), lp(ir[1], 6000)]); ir[:, :int(0.012 * SR)] = 0
    return ir / np.sqrt(np.sum(ir ** 2, axis=1, keepdims=True))
IR = reverb_ir()
def with_rev(bus, wet):
    L = bus.L + wet * signal.fftconvolve(bus.L, IR[0])[:TOTAL]
    R = bus.R + wet * signal.fftconvolve(bus.R, IR[1])[:TOTAL]
    return L, R
mix = np.zeros((2, TOTAL))
for bus, wet, g in ((keys, .35, 1.0), (bas, .12, 0.8), (mel, .45, 1.4), (drm, .25, 2.0)):
    L, R = with_rev(bus, wet); mix[0] += L * g; mix[1] += R * g
# 루프 접합: 꼬리를 앞으로 겹치기
music = mix[:, :LOOP].copy(); tail = mix[:, LOOP:]
music[:, :tail.shape[1]] += tail

# 빗소리 + LP 잡음 (루프 길이만큼)
fade = int(0.5 * SR); n = LOOP + fade; t = np.arange(n) / SR
rain = np.stack([lp(bp(rng.uniform(-1, 1, n), 500, 7000), 5000) for _ in range(2)]) * 0.045
for _ in range(int(n / SR * 30)):
    i = rng.integers(0, n - 2000); d = hp(rng.uniform(-1, 1, 1500), 2500) * np.exp(-np.arange(1500) / 120) * rng.uniform(.01, .05)
    c = rng.integers(0, 2); rain[c, i:i + 1500] += d
crack = np.zeros(n)
for _ in range(int(n / SR * 7)):
    i = rng.integers(0, n - 200); crack[i:i + 60] += hp(rng.uniform(-1, 1, 60), 2000) * rng.uniform(.02, .08)
crack += hp(rng.normal(0, 1, n), 1000) * 0.004
ramp = np.linspace(0, 1, fade)                         # 잡음 루프 이음매: 끝 다음 구간을 앞에 크로스페이드
for arr in (rain[0], rain[1], crack):
    arr[:fade] = arr[:fade] * ramp + arr[LOOP:LOOP + fade] * (1 - ramp)
rain = rain[:, :LOOP]; crack = crack[:LOOP]
rain *= 2.0; crack *= 1.6
music[0] += rain[0] + crack * 0.9; music[1] += rain[1] + crack

# 마스터: 로파이 톤 + 살짝 테이프 포화 + 정규화
pad = SR
music = np.stack([lp(np.concatenate([ch[-pad:], ch]), 10500)[pad:] for ch in music])   # 루프를 고려한 필터
music /= np.max(np.abs(music)) / 0.9
music = np.tanh(music * 1.2) / np.tanh(1.2)
rms = np.sqrt(np.mean(music ** 2)); music *= min(10 ** (-16 / 20) / rms, 0.89 / np.max(np.abs(music)))
out = sys.argv[1]
import wave
pcm = (music.T * 32767).astype(np.int16)
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('seconds', round(LOOP / SR, 1), 'rms_db', round(20 * np.log10(np.sqrt(np.mean(music ** 2))), 1))
