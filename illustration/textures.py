import numpy as np
from PIL import Image, ImageDraw, ImageFilter
rng=np.random.default_rng(21)
def field(h,w,beta,seed=None):
    r=np.random.default_rng(seed)
    fy=np.fft.fftfreq(h)[:,None]; fx=np.fft.fftfreq(w)[None,:]
    f=np.sqrt(fx**2+fy**2); f[0,0]=1
    spec=(r.normal(size=(h,w))+1j*r.normal(size=(h,w)))/f**beta
    spec[0,0]=0
    x=np.real(np.fft.ifft2(spec)); x=(x-x.mean())/x.std(); return x
# --- paper (tileable 512) ---
N=512
p=np.full((N,N,3),[247,244,236],float)
lo=field(N,N,1.8,1)*3.2; hi=field(N,N,0.4,2)*2.4
p+=(lo+hi)[...,None]
img=Image.fromarray(np.clip(p,0,255).astype('uint8'))
d=ImageDraw.Draw(img,'RGBA')
for _ in range(260):
    x,y=rng.uniform(0,N,2); a=rng.uniform(0,np.pi); L=rng.uniform(4,16)
    c=int(rng.uniform(200,235)); al=int(rng.uniform(25,60))
    for ox in (-N,0,N):
        for oy in (-N,0,N):
            d.line([(x+ox,y+oy),(x+ox+L*np.cos(a),y+oy+L*np.sin(a))],fill=(c,c-4,c-12,al),width=1)
img=img.filter(ImageFilter.GaussianBlur(0.35))
img.save('paper.jpg',quality=88)
# --- wood desk (tileable 800) ---
W=H=800
yy,xx=np.mgrid[0:H,0:W].astype(float)
warp=field(H,W,2.2,3)*0.9
fine=field(H,W,0.9,4)
ring=np.sin(2*np.pi*(yy/H*9+warp*0.55))
grain=0.5+0.5*ring
streak=field(H,W,1.4,5)
# planks: seams every 1/4 height (periodic)
seam=np.abs(((yy/H*4)%1)-0.0)
plank_shift=np.floor(yy/H*4)
tone=np.take([0,-10,6,-5],plank_shift.astype(int)%4)
base=np.array([170,120,78])
dark=np.array([118,76,44])
mix=(grain*0.55+0.45*(0.5+0.18*streak))[...,None]
wood=dark+(base-dark)*mix
wood+=tone[...,None]+fine[...,None]*4
dist=np.minimum((yy/H*4)%1,1-(yy/H*4)%1)*H/4
wood*=np.clip(0.55+dist/3.0,0.55,1)[...,None]
wood=np.clip(wood,0,255).astype('uint8')
Image.fromarray(wood).filter(ImageFilter.GaussianBlur(0.6)).save('wood.jpg',quality=86)
# --- grunge mask (tileable 256, white=keep) ---
g=field(256,256,0.6,6)+field(256,256,1.6,7)*0.6
a=np.clip((g+1.15)*200,0,255)
a=np.where(g<-1.25,0,a)
Image.fromarray(a.astype('uint8'),'L').save('grunge.png')
# --- masking tape (alpha PNG) ---
TW,TH=240,64
t=np.zeros((TH,TW,4),float)
t[...,:3]=[236,224,196]; t[...,:3]+=field(TH,TW,1.0,8)[...,None]*5
alpha=np.full((TH,TW),190.0)
for side in (0,1):
    edge=np.cumsum(rng.normal(0,1.2,TH)); edge=edge-edge.min(); edge=np.clip(edge,0,9)+2
    for yv in range(TH):
        e=int(edge[yv])
        if side==0: alpha[yv,:e]=0
        else: alpha[yv,TW-e:]=0
t[...,3]=alpha
Image.fromarray(np.clip(t,0,255).astype('uint8'),'RGBA').save('tape.png')
