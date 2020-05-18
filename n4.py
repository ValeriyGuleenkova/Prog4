from PIL import Image,ImageDraw
st = input()
st1 = st.split()
N = float(st1[0])
int_f = st1[1]
out_f = st1[2]
pic = Image.open(int_f)
pix = pic.load()
pic_new = Image.new("RGB",(int(pic.size[0]*N),int(pic.size[1]*N)))
draw = ImageDraw.Draw(pic_new)
for i in range (pic_new.size[0]):
    for j in range (pic_new.size[1]):
        draw.point((i,j),pix[i//N,j//N])
pic_new.save(out_f,"bmp")

