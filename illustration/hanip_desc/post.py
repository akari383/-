import sys, numpy as np
from PIL import Image, ImageFilter
def photo(src,dst,seed):
    rng=np.random.default_rng(seed)
    im=Image.open(src).convert('RGB'); W,H=im.size
    # slight camera tilt (keystone) + rotation, crop margins
    j=lambda s: rng.uniform(-s,s)
    m=0.018
    quad=(W*m+j(6),H*m*0.6+j(6), W*m*0.4+j(6),H*(1-m*0.6)+j(6), W*(1-m*0.4)+j(6),H*(1-m*0.6)+j(6), W*(1-m)+j(6),H*m*0.6+j(6))
    im=im.transform((W,H),Image.QUAD,quad,resample=Image.BICUBIC)
    im=im.rotate(j(0.5),resample=Image.BICUBIC)
    cx,cy=int(W*0.03),int(H*0.03)
    im=im.crop((cx,cy,W-cx,H-cy)); W,H=im.size
    a=np.asarray(im).astype(float)
    yy,xx=np.mgrid[0:H,0:W].astype(float)
    # shallow depth of field toward edges
    b=np.asarray(im.filter(ImageFilter.GaussianBlur(2.6))).astype(float)
    d=np.sqrt(((xx-W*0.5)/(W*0.55))**2+((yy-H*0.5)/(H*0.55))**2)
    mk=np.clip((d-0.8)/0.4,0,1)**1.5
    a=a*(1-mk[...,None])+b*mk[...,None]
    # window light from upper-left, falloff + vignette
    ld=np.sqrt(((xx-W*0.15)/W)**2+((yy+H*0.1)/max(W,H))**2)
    light=1.10-0.30*np.clip(ld,0,1.3)
    vig=1-0.20*np.clip(np.sqrt(((xx-W/2)/(W*0.6))**2+((yy-H/2)/(H*0.6))**2)-0.5,0,1)
    a=a*(light*vig)[...,None]
    # warm white balance, soft highlights, lifted blacks
    a[...,0]*=1.04; a[...,2]*=0.92
    a=255*(1-np.exp(-a/255*1.25))/(1-np.exp(-1.25))
    a=a*0.95+7
    # subtle chromatic aberration at edges
    sh=1
    a[...,0]=np.roll(a[...,0],sh,axis=1)*mk+a[...,0]*(1-mk)
    a[...,2]=np.roll(a[...,2],-sh,axis=1)*mk+a[...,2]*(1-mk)
    img=Image.fromarray(np.clip(a,0,255).astype('uint8')).filter(ImageFilter.UnsharpMask(radius=1.3,percent=50,threshold=2))
    a=np.asarray(img).astype(float)
    n=rng.normal(0,4.0,(H,W)); n=np.asarray(Image.fromarray((n+64).clip(0,255).astype('uint8')).filter(ImageFilter.GaussianBlur(0.55))).astype(float)-64
    a=a+n[...,None]+rng.normal(0,1.5,(H,W,3))
    out=Image.fromarray(np.clip(a,0,255).astype('uint8'))
    out=out.resize((960,round(960*H/W)),Image.LANCZOS)
    out.save(dst,quality=84,optimize=True,progressive=True)
    return out.size
for i,k in enumerate(sys.argv[1:]):
    print(k,photo(f'raw{k}.png',f'p{k}.jpg',100+i))
