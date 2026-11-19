import numpy as np
from PIL import Image, ImageFilter
rng=np.random.default_rng(4)
im=Image.open('raw2.png').convert('RGB'); W,H=im.size  # 1200x1600
# 1. camera tilt (keystone + slight rotation)
quad=(46,22, 18,1586, 1190,1572, 1162,8)
im=im.transform((W,H),Image.QUAD,quad,resample=Image.BICUBIC)
im=im.rotate(0.8,resample=Image.BICUBIC,center=(W/2,H/2))
im=im.crop((30,40,30+1140,40+1520)).resize((1080,1440),Image.LANCZOS); W,H=im.size
# 2. depth of field: blur edges
bl=im.filter(ImageFilter.GaussianBlur(3.2))
yy,xx=np.mgrid[0:H,0:W].astype(float)
cx,cy=W*0.46,H*0.52
d=np.sqrt(((xx-cx)/(W*0.50))**2+((yy-cy)/(H*0.50))**2)
m=np.clip((d-0.78)/0.42,0,1)**1.4
a=np.asarray(im).astype(float); b=np.asarray(bl).astype(float)
a=a*(1-m[...,None])+b*m[...,None]
# 3. lighting: warm overhead light from upper-left + vignette
lx,ly=W*0.28,H*0.05
ld=np.sqrt(((xx-lx)/W)**2+((yy-ly)/H)**2)
light=1.07-0.26*np.clip(ld,0,1.3)
vig=1-0.22*np.clip(np.sqrt(((xx-W/2)/(W*0.62))**2+((yy-H/2)/(H*0.62))**2)-0.55,0,1)
a=a*(light*vig)[...,None]
# 4. color: warm white balance, slightly lifted blacks, softer contrast
a[...,0]*=1.035; a[...,1]*=1.0; a[...,2]*=0.93
a=a*0.93+10
# 5. phone sharpening
img=Image.fromarray(np.clip(a,0,255).astype('uint8')).filter(ImageFilter.UnsharpMask(radius=1.4,percent=45,threshold=2))
a=np.asarray(img).astype(float)
# 6. sensor noise (luma + a little chroma), slightly soft grain
n=rng.normal(0,4.2,(H,W)); n=np.asarray(Image.fromarray(((n+64)).clip(0,255).astype('uint8')).filter(ImageFilter.GaussianBlur(0.5))).astype(float)-64
c=rng.normal(0,1.6,(H,W,3))
a=a+n[...,None]+c
out=Image.fromarray(np.clip(a,0,255).astype('uint8'))
out.save('final.png'); out.save('final.jpg',quality=88)
out.resize((540,720)).save('final_s.png')
out.crop((300,200,900,800)).save('final_crop.png')
