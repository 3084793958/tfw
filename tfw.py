import turtle
import random
import turtle as image
pc1=0
pc2=0
pc3=0
pc4=0
chs=4
tz=0
pcs=0
turtle.title("太富翁")
turtle.setup(800,600)
turtle.bgpic("tfw.gif")
wjs=turtle.Turtle()
wjs.up()
wjs.hideturtle()
turtle.up()
wj1=turtle.Turtle()
wj1.up()
wj1.fillcolor("red")
wj1.speed(speed=0)
wj1.setpos(356.25,-256.25)
wj1.setheading(180)
image.up()
image.hideturtle()
tzbj=turtle.Turtle()
pd=turtle.Turtle()
tzsz=turtle.Turtle()
tou=turtle.Turtle()
gz1fz=turtle.Turtle()
gz2fz=turtle.Turtle()
gz3fz=turtle.Turtle()
gz4fz=turtle.Turtle()
huihefz=turtle.Turtle()
dc1fz=turtle.Turtle()
dc2fz=turtle.Turtle()
dc3fz=turtle.Turtle()
dc4fz=turtle.Turtle()
q1fz=turtle.Turtle()
q2fz=turtle.Turtle()
q3fz=turtle.Turtle()
q4fz=turtle.Turtle()
draw=turtle.Turtle()
draw2=turtle.Turtle()
draw3=turtle.Turtle()
draw4=turtle.Turtle()
pc1fz=turtle.Turtle()
pc2fz=turtle.Turtle()
pc3fz=turtle.Turtle()
pc4fz=turtle.Turtle()
gz1fz.up()
gz2fz.up()
gz3fz.up()
gz4fz.up()
q1fz.up()
q2fz.up()
q3fz.up()
q4fz.up()
huihefz.up()
tzbj.up()
tzsz.up()
tou.up()
dc1fz.up()
dc2fz.up()
dc3fz.up()
dc4fz.up()
draw.up()
draw2.up()
draw3.up()
draw4.up()
pc1fz.up()
pc2fz.up()
pc3fz.up()
pc4fz.up()
pd.up()
tzsz.hideturtle()
gz1fz.hideturtle()
gz2fz.hideturtle()
gz3fz.hideturtle()
gz4fz.hideturtle()
huihefz.hideturtle()
pd.hideturtle()
dc1fz.hideturtle()
dc2fz.hideturtle()
dc3fz.hideturtle()
dc4fz.hideturtle()
q1fz.hideturtle()
q2fz.hideturtle()
q3fz.hideturtle()
q4fz.hideturtle()
turtle.hideturtle()
pc1fz.hideturtle()
pc2fz.hideturtle()
pc3fz.hideturtle()
pc4fz.hideturtle()
tzbj.color("red")
draw.color("#006600")
draw2.color("#006600")
draw3.color("#006600")
draw4.color("#006600")
tou.color("#FFFFFF")
turtle.speed(speed=0)
draw.speed(speed=0)
draw2.speed(speed=0)
draw3.speed(speed=0)
draw4.speed(speed=0)
tzbj.speed(speed=0)
tzsz.speed(speed=0)
tou.speed(speed=0)
q1fz.speed(speed=0)
q2fz.speed(speed=0)
q3fz.speed(speed=0)
q4fz.speed(speed=0)
tzbj.setpos(0,265)
tzsz.setpos(-5,253)
tou.setpos(100,265)
turtle.setpos(90,253)
draw.setpos(500,500)
wj2=turtle.Turtle()
wj2.up()
wj2.fillcolor("blue")
wj2.speed(speed=0)
wj2.setpos(356.25,-256.25)
wj2.shape(name="turtle")
wj2.setheading(180)
wj3=turtle.Turtle()
wj3.up()
wj3.fillcolor("yellow")
wj3.speed(speed=0)
wj3.setpos(356.25,-256.25)
wj3.shape(name="turtle")
wj3.setheading(180)
wj4=turtle.Turtle()
wj4.up()
wj4.fillcolor("green")
wj4.speed(speed=0)
wj4.setpos(356.25,-256.25)
wj4.shape(name="turtle")
wj4.setheading(180)
wj1.shape(name="turtle")
tzbj.shape(name="square")
tou.shape(name="square")
draw.shape(name="square")
draw2.shape(name="square")
draw3.shape(name="square")
draw4.shape(name="square")
draw.shapesize(stretch_wid=1.1, stretch_len=4, outline=None)
draw2.shapesize(stretch_wid=1.1, stretch_len=4, outline=None)
draw3.shapesize(stretch_wid=1.1, stretch_len=4, outline=None)
draw4.shapesize(stretch_wid=1.1, stretch_len=4, outline=None)
draw.setpos(-350,190)
draw2.setpos(-350,50)
draw3.setpos(-350,-65)
draw4.setpos(-350,-215)
while True:
    wj=turtle.textinput("玩家数量", "请输入玩家数量(2~4)")
    if (wj==str(2)):
        pc3fz.setx(1)
        pc4fz.setx(1)
        break
    if (wj==str(3)):
        pc4fz.setx(1)
        break
    if (wj==str(4)):
        break
wjs.setx(int(wj))
pc1=(int(pc1fz.xcor()))
pc2=(int(pc2fz.xcor()))
pc3=(int(pc3fz.xcor()))
pc4=(int(pc4fz.xcor()))
turtle.write("投", align="left",font=("宋体",15,"normal"))
name1=turtle.textinput("玩家1名称", "请输入玩家1的名称(如不填写，默认空白)")
turtle.setpos(-390,215)
turtle.write(name1, align="left",font=("宋体",18,"normal"))
name2=turtle.textinput("玩家2名称", "请输入玩家2的名称(如不填写，默认空白)")
turtle.setpos(-390,75)
turtle.write(name2, align="left",font=("宋体",18,"normal"))
if (pc3==0):
    name3=turtle.textinput("玩家3名称", "请输入玩家3的名称(如不填写，默认空白)")
    turtle.setpos(-390,-40)
    turtle.write(name3, align="left",font=("宋体",18,"normal"))
if (pc4==0):
    name4=turtle.textinput("玩家4名称", "请输入玩家4的名称(如不填写，默认空白)")
    turtle.setpos(-390,-185)
    turtle.write(name4, align="left",font=("宋体",18,"normal"))
huihefz.forward(1)
q1fz.setx(6666)
q2fz.setx(6666)
if (pc3==0):
    q3fz.setx(6666)
if (pc4==0):
    q4fz.setx(6666)
if (pc3==1):
    pc3fz.setx(1)
if (pc4==1):
    pc4fz.setx(1)
draw.setpos(-350,190)
draw2.setpos(-350,50)
draw3.setpos(-350,-65)
draw4.setpos(-350,-215)
if (pc1==1):
    wj1.hideturtle()
if (pc2==1):
    wj2.hideturtle()
if (pc3==1):
    wj3.hideturtle()
if (pc4==1):
    wj4.hideturtle()
z1=turtle.Turtle()
z2=turtle.Turtle()
z3=turtle.Turtle()
z4=turtle.Turtle()
z5=turtle.Turtle()
z6=turtle.Turtle()
z7=turtle.Turtle()
z8=turtle.Turtle()
z1.up()
z2.up()
z3.up()
z4.up()
z5.up()
z6.up()
z7.up()
z8.up()
z1.hideturtle()
z2.hideturtle()
z3.hideturtle()
z4.hideturtle()
z5.hideturtle()
z6.hideturtle()
z7.hideturtle()
z8.hideturtle()
z1.setheading(0)
z2.setheading(0)
z3.setheading(0)
z4.setheading(0)
z5.setheading(0)
z6.setheading(0)
z7.setheading(0)
z8.setheading(0)
f1=turtle.Turtle()
f2=turtle.Turtle()
f3=turtle.Turtle()
f4=turtle.Turtle()
f5=turtle.Turtle()
f6=turtle.Turtle()
f7=turtle.Turtle()
f8=turtle.Turtle()
f1.up()
f2.up()
f3.up()
f4.up()
f5.up()
f6.up()
f7.up()
f8.up()
f1.hideturtle()
f2.hideturtle()
f3.hideturtle()
f4.hideturtle()
f5.hideturtle()
f6.hideturtle()
f7.hideturtle()
f8.hideturtle()
f1.setheading(0)
f2.setheading(0)
f3.setheading(0)
f4.setheading(0)
f5.setheading(0)
f6.setheading(0)
f7.setheading(0)
f8.setheading(0)
ssfz=turtle.Turtle()
ssfz.up()
ssfz.hideturtle()
xffz=turtle.Turtle()
xffz.up()
xffz.hideturtle()
xunhuan=turtle.Turtle()
xunhuan.up()
xunhuan.hideturtle()
tzfz=turtle.Turtle()
tzfz.up()
tzfz.hideturtle()
q1=(int(q1fz.xcor()))
q2=(int(q2fz.xcor()))
q3=(int(q3fz.xcor()))
q4=(int(q4fz.xcor()))
draw.setpos(-350,190)
draw2.setpos(-350,50)
draw3.setpos(-350,-65)
draw4.setpos(-350,-215)
diy=turtle.textinput("diy","是否使用玩家图片DIY（1是，2否）（如果使用DIY，请在本目录下放图片）（图片必须为.gif）（玩家1的图片为1.gif,玩家2的图片为2.gif,玩家3的图片为3.gif,玩家4的图片为4.gif）(请放入文件后才使用DIY，否则会报错)")
if (diy==str(1)):
    image.addshape("1.gif")
    wj1.shape("1.gif")
    image.addshape("2.gif")
    wj2.shape("2.gif")
    if (pc3==0):
        image.addshape("3.gif")
        wj3.shape("3.gif")
    if (pc4==0):
        image.addshape("4.gif")
        wj4.shape("4.gif")
if (pc1==0):
    turtle.setpos(-390,180)
    turtle.write(q1, align="left",font=("宋体",15,"normal"))
if (pc2==0):
    turtle.setpos(-390,40)
    turtle.write(q2, align="left",font=("宋体",15,"normal"))
if (pc3==0):
    turtle.setpos(-390,-75)
    turtle.write(q3, align="left",font=("宋体",15,"normal"))
if (pc4==0):
    turtle.setpos(-390,-225)
    turtle.write(q4, align="left",font=("宋体",15,"normal"))
def touzi(x,y):
    if (x>85)and(x<115)and(y>250)and(y<280):
        pc1=(int(pc1fz.xcor()))
        pc2=(int(pc2fz.xcor()))
        pc3=(int(pc3fz.xcor()))
        pc4=(int(pc4fz.xcor()))
        q1=(int(q1fz.xcor()))
        q2=(int(q2fz.xcor()))
        q3=(int(q3fz.xcor()))
        q4=(int(q4fz.xcor()))
        draw.setpos(-350,190)
        draw2.setpos(-350,50)
        draw3.setpos(-350,-65)
        draw4.setpos(-350,-215)
        if (pc1==0):
            turtle.setpos(-390,180)
            turtle.write(q1, align="left",font=("宋体",15,"normal"))
        if (pc2==0):
            turtle.setpos(-390,40)
            turtle.write(q2, align="left",font=("宋体",15,"normal"))
        if (pc3==0):
            turtle.setpos(-390,-75)
            turtle.write(q3, align="left",font=("宋体",15,"normal"))
        if (pc4==0):
            turtle.setpos(-390,-225)
            turtle.write(q4, align="left",font=("宋体",15,"normal"))
        jianyu=[-278,-281]
        yyz=[(z1.xcor()),(z1.ycor()),(z1.heading()),(z2.xcor()),(z2.ycor()),(z2.heading()),(z3.xcor()),(z3.ycor()),(z3.heading()),(z4.xcor()),(z4.ycor()),(z4.heading()),(z5.xcor()),(z5.ycor()),(z5.heading()),(z6.xcor()),(z6.ycor()),(z6.heading()),(z7.xcor()),(z7.ycor()),(z7.heading()),(z8.xcor()),(z8.ycor()),(z8.heading())]
        fzs=[(f1.xcor()),(f1.ycor()),(f1.heading()),(f2.xcor()),(f2.ycor()),(f2.heading()),(f3.xcor()),(f3.ycor()),(f3.heading()),(f4.xcor()),(f4.ycor()),(f4.heading()),(f5.xcor()),(f5.ycor()),(f5.heading()),(f6.xcor()),(f6.ycor()),(f6.heading()),(f7.xcor()),(f7.ycor()),(f7.heading()),(f8.xcor()),(f8.ycor()),(f8.heading())]
        xzbj=[356.25,268.75,181.25,93.75,6.25,-81.25,-168.75,-256.25,-256.25,-256.25,-256.25,-256.25,-256.25,-168.75,-81.25,6.25,93.75,181.25,268.75,356.25,356.25,356.25,356.25,356.25]
        yzbj=[-256.25,-256.25,-256.25,-256.25,-256.25,-256.25,-256.25,-256.25,-168.75,-81.25,6.25,93.75,181.25,181.25,181.25,181.25,181.25,181.25,181.25,181.25,93.75,6.25,-81.25,-168.75]
        jg=[2000,600,0,1000,1500,0,2000,0,1800,2000,0,2600,0,2000,2400,0,3600,0,3000,0,3200,0,0,1400]
        mingyun=['被雷劈-2000','收到圣诞礼物+1000','坐飞机前进10格','把SB打残，进监狱','荣获吃席大奖，直接回起点，并在起点奖励的基础上+1000（仅这次有效）']
        jihui=['被老六制裁-6666','加入WTO（世界贸易组织）+10000','再来1次','收税（一栋别墅800）','货币贬值,钱减少一半']
        tzbj.shape(name="square")
        tz=random.randint(1,6)
        tzsz.write(tz, align="left",font=("宋体",15,"normal"))
        tzfz.setx(tz)
        dc1=(int(dc1fz.xcor()))
        dc2=(int(dc2fz.xcor()))
        dc3=(int(dc3fz.xcor()))
        dc4=(int(dc4fz.xcor()))
        gezi1=(int(gz1fz.xcor()))
        gezi2=(int(gz2fz.xcor()))
        gezi3=(int(gz3fz.xcor()))
        gezi4=(int(gz4fz.xcor()))
        huihe=(int(huihefz.xcor()))
        xffz.setx(10)
        while True:
            if (huihe==1)and((pc1==1)or(dc1!=0)):
                huihefz.forward(1)
            if (huihe==2)and((pc2==1)or(dc2!=0)):
                huihefz.forward(1)
            if (huihe==3)and((pc3==1)or(dc3!=0)):
                huihefz.forward(1)
            if (huihe==4)and((pc4==1)or(dc4!=0)):
                huihefz.forward(1)
            if (dc1!=0)and(dc2!=0)and((xffz.xcor())==2):
                dc1fz.setx(0)
                dc2fz.setx(0)
            if (dc1!=0)and(dc3!=0)and((xffz.xcor())==2):
                dc1fz.setx(0)
                dc3fz.setx(0)
            if (dc1!=0)and(dc4!=0)and((xffz.xcor())==2):
                dc1fz.setx(0)
                dc4fz.setx(0)
            if (dc2!=0)and(dc3!=0)and((xffz.xcor())==2):
                dc2fz.setx(0)
                dc3fz.setx(0)
            if (dc2!=0)and(dc4!=0)and((xffz.xcor())==2):
                dc2fz.setx(0)
                dc4fz.setx(0)
            if (dc3!=0)and(dc4!=0)and((xffz.xcor())==2):
                dc3fz.setx(0)
                dc4fz.setx(0)
            if (dc1!=0)and(dc2!=0)and(dc3!=0)and((xffz.xcor())==3):
                dc1fz.setx(0)
                dc2fz.setx(0)
                dc3fz.setx(0)
            if (dc1!=0)and(dc2!=0)and(dc4!=0)and((xffz.xcor())==3):
                dc1fz.setx(0)
                dc2fz.setx(0)
                dc4fz.setx(0)
            if (dc1!=0)and(dc3!=0)and(dc4!=0)and((xffz.xcor())==3):
                dc1fz.setx(0)
                dc3fz.setx(0)
                dc4fz.setx(0)
            if (dc4!=0)and(dc2!=0)and(dc3!=0)and((xffz.xcor())==3):
                dc4fz.setx(0)
                dc2fz.setx(0)
                dc3fz.setx(0)
            if (dc1!=0)and(dc2!=0)and(dc3!=0)and(dc4!=0)and((xffz.xcor())==4):
                dc1fz.setx(0)
                dc2fz.setx(0)
                dc3fz.setx(0)
                dc4fz.setx(0)
            if (huihe>(wjs.xcor())):
                huihefz.setx(1)          
            xffz.backward(1)
            huihe=(int(huihefz.xcor()))
            dc1=(int(dc1fz.xcor()))
            dc2=(int(dc2fz.xcor()))
            dc3=(int(dc3fz.xcor()))
            dc4=(int(dc4fz.xcor()))
            if ((xffz.xcor())<1):
                break
        while((tzfz.xcor())>0):
            tzfz.backward(1)
            if (huihe==1)and(pc1==0)and(dc1==0):
                if (gezi1!=23):
                    gz1fz.forward(1)
                else:
                    gz1fz.setx(0)
                gezi1=(int(gz1fz.xcor()))
                x1=xzbj[gezi1]
                y1=yzbj[gezi1]
                wj1.setpos(x1,y1)
            if (huihe==2)and(pc2==0)and(dc2==0):
                if (gezi2!=23):
                    gz2fz.forward(1)
                else:
                    gz2fz.setx(0)
                gezi2=(int(gz2fz.xcor()))
                x2=xzbj[gezi2]
                y2=yzbj[gezi2]
                wj2.setpos(x2,y2)
            if (huihe==3)and(pc3==0)and(dc3==0):
                if (gezi3!=23):
                    gz3fz.forward(1)
                else:
                    gz3fz.setx(0)
                gezi3=(int(gz3fz.xcor()))
                x3=xzbj[gezi3]
                y3=yzbj[gezi3]
                wj3.setpos(x3,y3)
            if (huihe==4)and(pc4==0)and(dc4==0):
                if (gezi4!=23):
                    gz4fz.forward(1)
                else:
                    gz4fz.setx(0)
                gezi4=(int(gz4fz.xcor()))
                x4=xzbj[gezi4]
                y4=yzbj[gezi4]
                wj4.setpos(x4,y4)
            if (gezi1==0)and(huihe==1):
                q1fz.forward(1000)
            if (gezi2==0)and(huihe==2):
                q2fz.forward(1000)
            if (gezi3==0)and(huihe==3):
                q3fz.forward(1000)
            if (gezi4==0)and(huihe==4):
                q4fz.forward(1000)
            q1=(int(q1fz.xcor()))
            q2=(int(q2fz.xcor()))
            q3=(int(q3fz.xcor()))
            q4=(int(q4fz.xcor()))
        huihefz.forward(1)
        q1=(int(q1fz.xcor()))
        q2=(int(q2fz.xcor()))
        q3=(int(q3fz.xcor()))
        q4=(int(q4fz.xcor()))
        if (q1<0):
            pc1=1
        if (q2<0):
            pc2=1
        if (q3<0):
            pc3=1
        if (q4<0):
            pc4=1
        yq=random.randint(0,4)
        if ((gezi1==2)or(gezi1==10)or(gezi1==17)or(gezi1==21))and(huihe==1):
            turtle.textinput("命运：", mingyun[yq])
            if (yq==0):
                q1fz.forward(-2000)
            if (yq==1):
                q1fz.forward(+1000)
            if (yq==2):
                ydfz=10
                while True:
                    if (gezi1!=23):
                        gz1fz.forward(1)
                    else:
                        gz1fz.setx(0)
                    gezi1=(int(gz1fz.xcor()))
                    x1=xzbj[gezi1]
                    y1=yzbj[gezi1]
                    wj1.setpos(x1,y1)
                    ydfz-=1
                    if (ydfz==0):
                        break
            if (yq==3):
                x1=jianyu[0]
                y1=jianyu[1]
                wj1.setpos(x1,y1)
                dc1fz.setx(4)
                gz1fz.setx(7)
            if (yq==4):
                gz1fz.setx(0)
                gezi1=0
                x1=xzbj[gezi1]
                y1=yzbj[gezi1]
                wj1.setpos(x1,y1)
                q1fz.forward(+1000)
        if ((gezi2==2)or(gezi2==10)or(gezi2==17)or(gezi2==21))and(huihe==2):
            turtle.textinput("命运：", mingyun[yq])
            if (yq==0):
                q2fz.forward(-2000)
            if (yq==1):
                q2fz.forward(+1000)
            if (yq==2):
                ydfz=10
                while True:
                    if (gezi2!=23):
                        gz2fz.forward(1)
                    else:
                        gz2fz.setx(0)
                    gezi2=(int(gz2fz.xcor()))
                    x2=xzbj[gezi2]
                    y2=yzbj[gezi2]
                    wj2.setpos(x2,y2)
                    ydfz-=1
                    if (ydfz==0):
                        break
            if (yq==3):
                x2=jianyu[0]
                y2=jianyu[1]
                wj2.setpos(x2,y2)
                dc2fz.setx(4)
                gz2fz.setx(7)
            if (yq==4):
                gz2fz.setx(0)
                gezi2=0
                x2=xzbj[gezi2]
                y2=yzbj[gezi2]
                wj2.setpos(x2,y2)
                q2fz.forward(+1000)
        if ((gezi3==2)or(gezi3==10)or(gezi3==17)or(gezi3==21))and(huihe==3):
            turtle.textinput("命运：", mingyun[yq])
            if (yq==0):
                q3fz.forward(-2000)
            if (yq==1):
                q3fz.forward(+1000)
            if (yq==2):
                ydfz=10
                while True:
                    if (gezi3!=23):
                        gz3fz.forward(1)
                    else:
                        gz3fz.setx(0)
                    gezi3=(int(gz3fz.xcor()))
                    x3=xzbj[gezi3]
                    y3=yzbj[gezi3]
                    wj3.setpos(x3,y3)
                    ydfz-=1
                    if (ydfz==0):
                        break
            if (yq==3):
                x3=jianyu[0]
                y3=jianyu[1]
                wj3.setpos(x3,y3)
                dc3fz.setx(4)
                gz3fz.setx(7)
            if (yq==4):
                gz3fz.setx(0)
                gezi3=0
                x3=xzbj[gezi3]
                y3=yzbj[gezi3]
                wj3.setpos(x3,y3)
                q3fz.forward(+1000)
        if ((gezi4==2)or(gezi4==10)or(gezi4==17)or(gezi4==21))and(huihe==4):
            turtle.textinput("命运：", mingyun[yq])
            if (yq==0):
                q4fz.forward(-2000)
            if (yq==1):
                q4fz.forward(+1000)
            if (yq==2):
                ydfz=10
                while True:
                    if (gezi4!=23):
                        gz4fz.forward(1)
                    else:
                        gz4fz.setx(0)
                    gezi4=(int(gz4fz.xcor()))
                    x4=xzbj[gezi4]
                    y4=yzbj[gezi4]
                    wj4.setpos(x4,y4)
                    ydfz-=1
                    if (ydfz==0):
                        break
            if (yq==3):
                x4=jianyu[0]
                y4=jianyu[1]
                wj4.setpos(x4,y4)
                dc4fz.setx(4)
                gz4fz.setx(7)
            if (yq==4):
                gz4fz.setx(0)
                gezi4=0
                x4=xzbj[gezi4]
                y4=yzbj[gezi4]
                wj4.setpos(x4,y4)
                q4fz.forward(+1000)
        if ((gezi1==5)or(gezi1==15)or(gezi1==22))and(huihe==1):
            turtle.textinput("机会：", jihui[yq])
            if (yq==0):
                q1fz.forward(-6666)
            if (yq==1):
                q1fz.forward(+10000)
            if (yq==2):
                huihefz.backward(1)
            if (yq==3):
                ssfz.setx(23)
                while (int(ssfz.xcor())!=0):
                    if ((yyz[(int(ssfz.xcor()))-1])==1):
                        ss=(fzs[(int(ssfz.xcor()))-1])
                        q1fz.backward((int(ss))*800)
                    ssfz.backward(1)
            if (yq==4):
                q1fz.backward((q1/2))
        if ((gezi2==5)or(gezi2==15)or(gezi2==22))and(huihe==2):
            turtle.textinput("机会：", jihui[yq])
            if (yq==0):
                q2fz.forward(-6666)
            if (yq==1):
                q2fz.forward(+10000)
            if (yq==2):
                huihefz.backward(1)
            if (yq==3):
                ssfz.setx(23)
                while (int(ssfz.xcor())!=0):
                    if ((yyz[(int(ssfz.xcor()))-1])==2):
                        ss=(fzs[(int(ssfz.xcor()))-1])
                        q2fz.backward((int(ss))*800)
                    ssfz.backward(1)
            if (yq==4):
                q2fz.backward((q2/2))
        if ((gezi3==5)or(gezi3==15)or(gezi3==22))and(huihe==3):
            turtle.textinput("机会：", jihui[yq])
            if (yq==0):
                q3fz.forward(-6666)
            if (yq==1):
                q3fz.forward(+10000)
            if (yq==2):
                huihefz.backward(1)
            if (yq==3):
                ssfz.setx(23)
                while (int(ssfz.xcor())!=0):
                    if ((yyz[(int(ssfz.xcor()))-1])==3):
                        ss=(fzs[(int(ssfz.xcor()))-1])
                        q3fz.backward((int(ss))*800)
                    ssfz.backward(1)
            if (yq==4):
                q3fz.backward((q3/2))
        if ((gezi4==5)or(gezi4==15)or(gezi4==22))and(huihe==4):
            turtle.textinput("机会：", jihui[yq])
            if (yq==0):
                q4fz.forward(-6666)
            if (yq==1):
                q4fz.forward(+10000)
            if (yq==2):
                huihefz.backward(1)
            if (yq==3):
                ssfz.setx(23)
                while (int(ssfz.xcor())!=0):
                    if ((yyz[(int(ssfz.xcor()))-1])==4):
                        ss=(fzs[(int(ssfz.xcor()))-1])
                        q4fz.backward((int(ss))*800)
                    ssfz.backward(1)
            if (yq==4):
                q4fz.backward((q4/2))
            #
            gezi1=(int(gz1fz.xcor()))
            gezi2=(int(gz2fz.xcor()))
            gezi3=(int(gz3fz.xcor()))
            gezi4=(int(gz4fz.xcor()))
        draw.setpos(-350,190)
        draw2.setpos(-350,50)
        draw3.setpos(-350,-65)
        draw4.setpos(-350,-215)
        if (pc1==0):
            turtle.setpos(-390,180)
            turtle.write(q1, align="left",font=("宋体",15,"normal"))
        if (pc2==0):
            turtle.setpos(-390,40)
            turtle.write(q2, align="left",font=("宋体",15,"normal"))
        if (pc3==0):
            turtle.setpos(-390,-75)
            turtle.write(q3, align="left",font=("宋体",15,"normal"))
        if (pc4==0):
            turtle.setpos(-390,-225)
            turtle.write(q4, align="left",font=("宋体",15,"normal"))
        if (pc1==0)and(gezi1==19):
            x1=jianyu[0]
            y1=jianyu[1]
            wj1.setpos(x1,y1)
            dc1fz.setx(4)
            gz1fz.setx(7)
        if (pc2==0)and(gezi2==19):
            x2=jianyu[0]
            y2=jianyu[1]
            wj2.setpos(x2,y2)
            dc2fz.setx(4)
            gz2fz.setx(7)
        if (pc3==0)and(gezi3==19):
            x3=jianyu[0]
            y3=jianyu[1]
            wj3.setpos(x3,y3)
            dc3fz.setx(4)
            gz3fz.setx(7)
        if (pc4==0)and(gezi4==19):
            x4=jianyu[0]
            y4=jianyu[1]
            wj4.setpos(x4,y4)
            dc4fz.setx(4)
            gz4fz.setx(7)
        if (pc1==0)and(gezi1==12):
            dc1fz.setx(4)
            gz1fz.setx(13)
        if (pc2==0)and(gezi2==12):
            dc2fz.setx(4)
            gz2fz.setx(13)
        if (pc3==0)and(gezi3==12):
            dc3fz.setx(4)
            gz3fz.setx(13)
        if (pc4==0)and(gezi4==12):
            dc4fz.setx(4)
            gz4fz.setx(13)
        if (dc1!=0):
            dc1fz.forward(-1)
        if (dc2!=0):
            dc2fz.forward(-1)
        if (dc3!=0):
            dc3fz.forward(-1)
        if (dc4!=0):
            dc4fz.forward(-1)
        if (gezi1==0)and(huihe==1):
            q1fz.forward(1000)
        if (gezi2==0)and(huihe==2):
            q2fz.forward(1000)
        if (gezi3==0)and(huihe==3):
            q3fz.forward(1000)
        if (gezi4==0)and(huihe==4):
            q4fz.forward(1000)
        gm=0
        md=0
        mf=0
        if (gezi1!=0)and(gezi1!=2)and(gezi1!=5)and(gezi1!=7)and(gezi1!=10)and(gezi1!=12)and(gezi1!=15)and(gezi1!=17)and(gezi1!=19)and(gezi1!=21)and(gezi1!=22):
            if (huihe==1):
                if ((yyz[gezi1-1])==0.0)and((q1>(jg[gezi1]))or(q1==(jg[gezi1]))):
                    gm=turtle.textinput("购买", "是否购买此地？（1：是，2：否）")
                    if (gm==str(1)):
                        q1fz.backward((jg[gezi1]))
                if ((yyz[gezi1-1])==1):
                    if (q1>(jg[gezi1]*0.9)):
                        mf=turtle.textinput("建造", "是否建造黄金VIP别墅？（1：是，2：否）（花费土地价格的90%）")
                        if (mf==str(1)):
                            q1fz.backward((jg[gezi1]*0.9))
                    md=turtle.textinput("卖地", "是否卖地？（1：是，2：否）（返还10%）")
                    if (md==str(1)):
                        q1fz.forward((jg[gezi1]/10))
                if ((yyz[gezi1-1])==2):
                    fk=((jg[gezi1]/10)+((fzs[gezi1-1]*(jg[gezi1]/2))))
                    turtle.textinput("此地玩家2",("付款:",fk,"别墅数量:",fzs[gezi1-1]))
                    q2fz.forward(fk)
                    q1fz.backward(fk)
                if ((yyz[gezi1-1])==3):
                    fk=((jg[gezi1]/10)+((fzs[gezi1-1]*(jg[gezi1]/2))))
                    turtle.textinput("此地玩家3",("付款:",fk,"别墅数量:",fzs[gezi1-1]))
                    q3fz.forward(fk)
                    q1fz.backward(fk)
                if ((yyz[gezi1-1])==4):
                    fk=((jg[gezi1]/10)+((fzs[gezi1-1]*(jg[gezi1]/2))))
                    turtle.textinput("此地玩家4",("付款:",fk,"别墅数量:",fzs[gezi1-1]))
                    q4fz.forward(fk)
                    q1fz.backward(fk)
        if (gezi2!=0)and(gezi2!=2)and(gezi2!=5)and(gezi2!=7)and(gezi2!=10)and(gezi2!=12)and(gezi2!=15)and(gezi2!=17)and(gezi2!=19)and(gezi2!=21)and(gezi2!=22):
            if (huihe==2):
                if ((yyz[gezi2-1])==0.0)and((q2>(jg[gezi2]))or(q2==(jg[gezi2]))):
                    gm=turtle.textinput("购买", "是否购买此地？（1：是，2：否）")
                    if (gm==str(1)):
                        q2fz.backward((jg[gezi2]))
                if ((yyz[gezi2-1])==2):
                    if (q2>(jg[gezi2]*0.9)):
                        mf=turtle.textinput("建造", "是否建造黄金VIP别墅？（1：是，2：否）（花费土地价格的90%）")
                        if (mf==str(1)):
                            q2fz.backward((jg[gezi2]*0.9))
                    md=turtle.textinput("卖地", "是否卖地？（1：是，2：否）（返还10%）")
                    if (md==str(1)):
                        q2fz.forward((jg[gezi2]/10))
                if ((yyz[gezi2-1])==1):
                    fk=((jg[gezi2]/10)+((fzs[gezi2-1]*(jg[gezi2]/2))))
                    turtle.textinput("此地玩家1",("付款:",fk,"别墅数量:",fzs[gezi2-1]))
                    q1fz.forward(fk)
                    q2fz.backward(fk)
                if ((yyz[gezi2-1])==3):
                    fk=((jg[gezi2]/10)+((fzs[gezi2-1]*(jg[gezi2]/2))))
                    turtle.textinput("此地玩家3",("付款:",fk,"别墅数量:",fzs[gezi2-1]))
                    q3fz.forward(fk)
                    q2fz.backward(fk)
                if ((yyz[gezi2-1])==4):
                    fk=((jg[gezi1]/10)+((fzs[gezi2-1]*(jg[gezi2]/2))))
                    turtle.textinput("此地玩家4",("付款:",fk,"别墅数量:",fzs[gezi2-1]))
                    q4fz.forward(fk)
                    q2fz.backward(fk)
        if (gezi3!=0)and(gezi3!=2)and(gezi3!=5)and(gezi3!=7)and(gezi3!=10)and(gezi3!=12)and(gezi3!=15)and(gezi3!=17)and(gezi3!=19)and(gezi3!=21)and(gezi3!=22):
            if (huihe==3):
                if ((yyz[gezi3-1])==0.0)and((q3>(jg[gezi3]))or(q3==(jg[gezi3]))):
                    gm=turtle.textinput("购买", "是否购买此地？（1：是，2：否）")
                    if (gm==str(1)):
                        q3fz.backward((jg[gezi3]))
                if ((yyz[gezi3-1])==3):
                    if (q3>(jg[gezi3]*0.9)):
                        mf=turtle.textinput("建造", "是否建造黄金VIP别墅？（1：是，2：否）（花费土地价格的90%）")
                        if (mf==str(1)):
                            q3fz.backward((jg[gezi3]*0.9))
                    md=turtle.textinput("卖地", "是否卖地？（1：是，2：否）（返还10%）")
                    if (md==str(1)):
                        q3fz.forward((jg[gezi3]/10))
                if ((yyz[gezi3-1])==1):
                    fk=((jg[gezi3]/10)+((fzs[gezi3-1]*(jg[gezi3]/2))))
                    turtle.textinput("此地玩家1",("付款:",fk,"别墅数量:",fzs[gezi3-1]))
                    q1fz.forward(fk)
                    q3fz.backward(fk)
                if ((yyz[gezi3-1])==2):
                    fk=((jg[gezi3]/10)+((fzs[gezi3-1]*(jg[gezi3]/2))))
                    turtle.textinput("此地玩家2",("付款:",fk,"别墅数量:",fzs[gezi3-1]))
                    q2fz.forward(fk)
                    q3fz.backward(fk)
                if ((yyz[gezi3-1])==4):
                    fk=((jg[gezi3]/10)+((fzs[gezi3-1]*(jg[gezi3]/2))))
                    turtle.textinput("此地玩家4",("付款:",fk,"别墅数量:",fzs[gezi3-1]))
                    q4fz.forward(fk)
                    q3fz.backward(fk)
        if (gezi4!=0)and(gezi4!=2)and(gezi4!=5)and(gezi4!=7)and(gezi4!=10)and(gezi4!=12)and(gezi4!=15)and(gezi4!=17)and(gezi4!=19)and(gezi4!=21)and(gezi4!=22):
            if (huihe==4):
                if ((yyz[gezi4-1])==0.0)and((q4>(jg[gezi4]))or(q4==(jg[gezi4]))):
                    gm=turtle.textinput("购买", "是否购买此地？（1：是，2：否）")
                    if (gm==str(1)):
                        q4fz.backward((jg[gezi4]))
                if ((yyz[gezi4-1])==4):
                    if (q4>(jg[gezi4]*0.9)):
                        mf=turtle.textinput("建造", "是否建造黄金VIP别墅？（1：是，2：否）（花费土地价格的90%）")
                        if (mf==str(1)):
                            q4fz.backward((jg[gezi4]*0.9))
                    md=turtle.textinput("卖地", "是否卖地？（1：是，2：否）（返还10%）")
                    if (md==str(1)):
                        q4fz.forward((jg[gezi4]/10))
                if ((yyz[gezi4-1])==1):
                    fk=((jg[gezi4]/10)+((fzs[gezi4-1]*(jg[gezi4]/2))))
                    turtle.textinput("此地玩家1",("付款:",fk,"别墅数量:",fzs[gezi4-1]))
                    q1fz.forward(fk)
                    q4fz.backward(fk)
                if ((yyz[gezi4-1])==2):
                    fk=((jg[gezi4]/10)+((fzs[gezi4-1]*(jg[gezi4]/2))))
                    turtle.textinput("此地玩家2",("付款:",fk,"别墅数量:",fzs[gezi4-1]))
                    q2fz.forward(fk)
                    q4fz.backward(fk)
                if ((yyz[gezi4-1])==3):
                    fk=((jg[gezi4]/10)+((fzs[gezi4-1]*(jg[gezi4]/2))))
                    turtle.textinput("此地玩家3",("付款:",fk,"别墅数量:",fzs[gezi4-1]))
                    q3fz.forward(fk)
                    q4fz.backward(fk)
        if ((huihe==1)and(gm==str(1))):
            if (gezi1==1):
               z1.setx(huihe)
            if (gezi1==3):
               z1.setheading(huihe)
            if (gezi1==4):
               z2.setx(huihe)
            if (gezi1==6):
               z2.setheading(huihe)
            if (gezi1==8):
               z3.sety(huihe)
            if (gezi1==9):
               z3.setheading(huihe)
            if (gezi1==11):
               z4.sety(huihe)
            if (gezi1==13):
               z5.setx(huihe)
            if (gezi1==14):
               z5.sety(huihe)
            if (gezi1==16):
               z6.setx(huihe)
            if (gezi1==18):
               z6.setheading(huihe)
            if (gezi1==20):
               z7.sety(huihe)
            if (gezi1==23):
               z8.sety(huihe)
        if ((huihe==2)and(gm==str(1))):
            if (gezi2==1):
               z1.setx(huihe)
            if (gezi2==3):
               z1.setheading(huihe)
            if (gezi2==4):
               z2.setx(huihe)
            if (gezi2==6):
               z2.setheading(huihe)
            if (gezi2==8):
               z3.sety(huihe)
            if (gezi2==9):
               z3.setheading(huihe)
            if (gezi2==11):
               z4.sety(huihe)
            if (gezi2==13):
               z5.setx(huihe)
            if (gezi2==14):
               z5.sety(huihe)
            if (gezi2==16):
               z6.setx(huihe)
            if (gezi2==18):
               z6.setheading(huihe)
            if (gezi2==20):
               z7.sety(huihe)
            if (gezi2==23):
               z8.sety(huihe)
        if ((huihe==3)and(gm==str(1))):
            if (gezi3==1):
               z1.setx(huihe)
            if (gezi3==3):
               z1.setheading(huihe)
            if (gezi3==4):
               z2.setx(huihe)
            if (gezi3==6):
               z2.setheading(huihe)
            if (gezi3==8):
               z3.sety(huihe)
            if (gezi3==9):
               z3.setheading(huihe)
            if (gezi3==11):
               z4.sety(huihe)
            if (gezi3==13):
               z5.setx(huihe)
            if (gezi3==14):
               z5.sety(huihe)
            if (gezi3==16):
               z6.setx(huihe)
            if (gezi3==18):
               z6.setheading(huihe)
            if (gezi3==20):
               z7.sety(huihe)
            if (gezi3==23):
               z8.sety(huihe)
        if ((huihe==4)and(gm==str(1))):
            if (gezi4==1):
               z1.setx(huihe)
            if (gezi4==3):
               z1.setheading(huihe)
            if (gezi4==4):
               z2.setx(huihe)
            if (gezi4==6):
               z2.setheading(huihe)
            if (gezi4==8):
               z3.sety(huihe)
            if (gezi4==9):
               z3.setheading(huihe)
            if (gezi4==11):
               z4.sety(huihe)
            if (gezi4==13):
               z5.setx(huihe)
            if (gezi4==14):
               z5.sety(huihe)
            if (gezi4==16):
               z6.setx(huihe)
            if (gezi4==18):
               z6.setheading(huihe)
            if (gezi4==20):
               z7.sety(huihe)
            if (gezi4==23):
               z8.sety(huihe)
        if ((huihe==1)and(md==str(1))):
            if (gezi1==1):
               z1.setx(0)
               f1.setx(0)
            if (gezi1==3):
               z1.setheading(0)
               f1.setheading(0)
            if (gezi1==4):
               z2.setx(0)
               f2.setx(0)
            if (gezi1==6):
               z2.setheading(0)
               f2.setheading(0)
            if (gezi1==8):
               z3.sety(0)
               f3.sety(0)
            if (gezi1==9):
               z3.setheading(0)
               f3.setheading(0)
            if (gezi1==11):
               z4.sety(0)
               f4.sety(0)
            if (gezi1==13):
               z5.setx(0)
               f5.setx(0)
            if (gezi1==14):
               z5.sety(0)
               f5.sety(0)
            if (gezi1==16):
               z6.setx(0)
               f6.setx(0)
            if (gezi1==18):
               z6.setheading(0)
               f6.setheading(0)
            if (gezi1==20):
               z7.sety(0)
               f7.sety(0)
            if (gezi1==23):
               z8.sety(0)
               f8.sety(0)
        if ((huihe==2)and(md==str(1))):
            if (gezi2==1):
               z1.setx(0)
               f1.setx(0)
            if (gezi2==3):
               z1.setheading(0)
               f1.setheading(0)
            if (gezi2==4):
               z2.setx(0)
               f2.setx(0)
            if (gezi2==6):
               z2.setheading(0)
               f2.setheading(0)
            if (gezi2==8):
               z3.sety(0)
               f3.sety(0)
            if (gezi2==9):
               z3.setheading(0)
               f3.setheading(0)
            if (gezi2==11):
               z4.sety(0)
               f4.sety(0)
            if (gezi2==13):
               z5.setx(0)
               f5.setx(0)
            if (gezi2==14):
               z5.sety(0)
               f5.sety(0)
            if (gezi2==16):
               z6.setx(0)
               f6.setx(0)
            if (gezi2==18):
               z6.setheading(0)
               f6.setheading(0)
            if (gezi2==20):
               z7.sety(0)
               f7.sety(0)
            if (gezi2==23):
               z8.sety(0)
               f8.sety(0)
        if ((huihe==3)and(md==str(1))):
            if (gezi3==1):
               z1.setx(0)
               f1.setx(0)
            if (gezi3==3):
               z1.setheading(0)
               f1.setheading(0)
            if (gezi3==4):
               z2.setx(0)
               f2.setx(0)
            if (gezi3==6):
               z2.setheading(0)
               f2.setheading(0)
            if (gezi3==8):
               z3.sety(0)
               f3.sety(0)
            if (gezi3==9):
               z3.setheading(0)
               f3.setheading(0)
            if (gezi3==11):
               z4.sety(0)
               f4.sety(0)
            if (gezi3==13):
               z5.setx(0)
               f5.setx(0)
            if (gezi3==14):
               z5.sety(0)
               f5.sety(0)
            if (gezi3==16):
               z6.setx(0)
               f6.setx(0)
            if (gezi3==18):
               z6.setheading(0)
               f6.setheading(0)
            if (gezi3==20):
               z7.sety(0)
               f7.sety(0)
            if (gezi3==23):
               z8.sety(0)
               f8.sety(0)
        if ((huihe==4)and(md==str(1))):
            if (gezi4==1):
               z1.setx(0)
               f1.setx(0)
            if (gezi4==3):
               z1.setheading(0)
               f1.setheading(0)
            if (gezi4==4):
               z2.setx(0)
               f2.setx(0)
            if (gezi4==6):
               z2.setheading(0)
               f2.setheading(0)
            if (gezi4==8):
               z3.sety(0)
               f3.sety(0)
            if (gezi4==9):
               z3.setheading(0)
               f3.setheading(0)
            if (gezi4==11):
               z4.sety(0)
               f4.sety(0)
            if (gezi4==13):
               z5.setx(0)
               f5.setx(0)
            if (gezi4==14):
               z5.sety(0)
               f5.sety(0)
            if (gezi4==16):
               z6.setx(0)
               f6.setx(0)
            if (gezi4==18):
               z6.setheading(0)
               f6.setheading(0)
            if (gezi4==20):
               z7.sety(0)
               f7.sety(0)
            if (gezi4==23):
               z8.sety(0)
               f8.sety(0)
        if ((huihe==1)and(mf==str(1))):
            if (gezi1==1):
                fz=f1.xcor()
                f1.setx(fz+1)
            if (gezi1==3):
                f1.left(1)
            if (gezi1==4):
                fz=f2.xcor()
                f2.setx(fz+1)
            if (gezi1==6):
                f2.left(1)
            if (gezi1==8):
                fz=f3.ycor()
                f3.sety(fz+1)
            if (gezi1==9):
                f3.left(1)
            if (gezi1==11):
                fz=f4.ycor()
                f4.sety(fz+1)
            if (gezi1==13):
                fz=f5.xcor()
                f5.setx(fz+1)
            if (gezi1==14):
                fz=f5.ycor()
                f5.sety(fz+1)
            if (gezi1==16):
                fz=f6.xcor()
                f6.setx(fz+1)
            if (gezi1==18):
                f6.left(1)
            if (gezi1==20):
                fz=f7.ycor()
                f7.sety(fz+1)
            if (gezi1==23):
                fz=f8.ycor()
                f8.sety(fz+1)
        if ((huihe==2)and(mf==str(1))):
            if (gezi2==1):
                fz=f1.xcor()
                f1.setx(fz+1)
            if (gezi2==3):
                f1.left(1)
            if (gezi2==4):
                fz=f2.xcor()
                f2.setx(fz+1)
            if (gezi2==6):
                f2.left(1)
            if (gezi2==8):
                fz=f3.ycor()
                f3.sety(fz+1)
            if (gezi2==9):
                f3.left(1)
            if (gezi2==11):
                fz=f4.ycor()
                f4.sety(fz+1)
            if (gezi2==13):
                fz=f5.xcor()
                f5.setx(fz+1)
            if (gezi2==14):
                fz=f5.ycor()
                f5.sety(fz+1)
            if (gezi2==16):
                fz=f6.xcor()
                f6.setx(fz+1)
            if (gezi2==18):
                f6.left(1)
            if (gezi2==20):
                fz=f7.ycor()
                f7.sety(fz+1)
            if (gezi2==23):
                fz=f8.ycor()
                f8.sety(fz+1)
        if ((huihe==3)and(mf==str(1))):
            if (gezi3==1):
                fz=f1.xcor()
                f1.setx(fz+1)
            if (gezi3==3):
                f1.left(1)
            if (gezi3==4):
                fz=f2.xcor()
                f2.setx(fz+1)
            if (gezi3==6):
                f2.left(1)
            if (gezi3==8):
                fz=f3.ycor()
                f3.sety(fz+1)
            if (gezi3==9):
                f3.left(1)
            if (gezi3==11):
                fz=f4.ycor()
                f4.sety(fz+1)
            if (gezi3==13):
                fz=f5.xcor()
                f5.setx(fz+1)
            if (gezi3==14):
                fz=f5.ycor()
                f5.sety(fz+1)
            if (gezi3==16):
                fz=f6.xcor()
                f6.setx(fz+1)
            if (gezi3==18):
                f6.left(1)
            if (gezi3==20):
                fz=f7.ycor()
                f7.sety(fz+1)
            if (gezi3==23):
                fz=f8.ycor()
                f8.sety(fz+1)
        if ((huihe==4)and(mf==str(1))):
            if (gezi4==1):
                fz=f1.xcor()
                f1.setx(fz+1)
            if (gezi4==3):
                f1.left(1)
            if (gezi4==4):
                fz=f2.xcor()
                f2.setx(fz+1)
            if (gezi4==6):
                f2.left(1)
            if (gezi4==8):
                fz=f3.ycor()
                f3.sety(fz+1)
            if (gezi4==9):
                f3.left(1)
            if (gezi4==11):
                fz=f4.ycor()
                f4.sety(fz+1)
            if (gezi4==13):
                fz=f5.xcor()
                f5.setx(fz+1)
            if (gezi4==14):
                fz=f5.ycor()
                f5.sety(fz+1)
            if (gezi4==16):
                fz=f6.xcor()
                f6.setx(fz+1)
            if (gezi4==18):
                f6.left(1)
            if (gezi4==20):
                fz=f7.ycor()
                f7.sety(fz+1)
            if (gezi4==23):
                fz=f8.ycor()
                f8.sety(fz+1)
        q1=(int(q1fz.xcor()))
        q2=(int(q2fz.xcor()))
        q3=(int(q3fz.xcor()))
        q4=(int(q4fz.xcor()))
        draw.setpos(-350,190)
        draw2.setpos(-350,50)
        draw3.setpos(-350,-65)
        draw4.setpos(-350,-215)
        if (pc1==0):
            turtle.setpos(-390,180)
            turtle.write(q1, align="left",font=("宋体",15,"normal"))
        if (pc2==0):
            turtle.setpos(-390,40)
            turtle.write(q2, align="left",font=("宋体",15,"normal"))
        if (pc3==0):
            turtle.setpos(-390,-75)
            turtle.write(q3, align="left",font=("宋体",15,"normal"))
        if (pc4==0):
            turtle.setpos(-390,-225)
            turtle.write(q4, align="left",font=("宋体",15,"normal"))
        xunhuan.setx(23)
        while (q1<0)and((int(xunhuan.xcor()))!=0):
            if ((yyz[(int(xunhuan.xcor()))-1])==1):
                q1fz.forward((jg[(int(xunhuan.xcor()))]/10))
                xh=(int(xunhuan.xcor()))
                if (xh==1):
                    z1.setx(0)
                    f1.setx(0)
                if (xh==3):
                    z1.setheading(0)
                    f1.setheading(0)
                if (xh==4):
                    z2.setx(0)
                    f2.setx(0)
                if (xh==6):
                    z2.setheading(0)
                    f2.setheading(0)
                if (xh==8):
                    z3.sety(0)
                    f3.sety(0)
                if (xh==9):
                    z3.setheading(0)
                    f3.setheading(0)
                if (xh==11):
                    z4.sety(0)
                    f4.sety(0)
                if (xh==13):
                    z5.setx(0)
                    f5.setx(0)
                if (xh==14):
                    z5.sety(0)
                    f5.sety(0)
                if (xh==16):
                    z6.setx(0)
                    f6.setx(0)
                if (xh==18):
                    z6.setheading(0)
                    f6.setheading(0)
                if (xh==20):
                    z7.sety(0)
                    f7.sety(0)
                if (xh==23):
                    z8.sety(0)
                    f8.sety(0)
            xunhuan.backward(1)
            q1=(int(q1fz.xcor()))
        xunhuan.setx(23)
        while (q2<0)and((int(xunhuan.xcor()))!=0):
            if ((yyz[(int(xunhuan.xcor()))-1])==2):
                q2fz.forward((jg[(int(xunhuan.xcor()))]/10))
                xh=(int(xunhuan.xcor()))
                if (xh==1):
                    z1.setx(0)
                    f1.setx(0)
                if (xh==3):
                    z1.setheading(0)
                    f1.setheading(0)
                if (xh==4):
                    z2.setx(0)
                    f2.setx(0)
                if (xh==6):
                    z2.setheading(0)
                    f2.setheading(0)
                if (xh==8):
                    z3.sety(0)
                    f3.sety(0)
                if (xh==9):
                    z3.setheading(0)
                    f3.setheading(0)
                if (xh==11):
                    z4.sety(0)
                    f4.sety(0)
                if (xh==13):
                    z5.setx(0)
                    f5.setx(0)
                if (xh==14):
                    z5.sety(0)
                    f5.sety(0)
                if (xh==16):
                    z6.setx(0)
                    f6.setx(0)
                if (xh==18):
                    z6.setheading(0)
                    f6.setheading(0)
                if (xh==20):
                    z7.sety(0)
                    f7.sety(0)
                if (xh==23):
                    z8.sety(0)
                    f8.sety(0)
            xunhuan.backward(1)
            q2=(int(q2fz.xcor()))
        xunhuan.setx(23)
        while (q3<0)and((int(xunhuan.xcor()))!=0):
            if ((yyz[(int(xunhuan.xcor()))-1])==3):
                q3fz.forward((jg[(int(xunhuan.xcor()))]/10))
                xh=(int(xunhuan.xcor()))
                if (xh==1):
                    z1.setx(0)
                    f1.setx(0)
                if (xh==3):
                    z1.setheading(0)
                    f1.setheading(0)
                if (xh==4):
                    z2.setx(0)
                    f2.setx(0)
                if (xh==6):
                    z2.setheading(0)
                    f2.setheading(0)
                if (xh==8):
                    z3.sety(0)
                    f3.sety(0)
                if (xh==9):
                    z3.setheading(0)
                    f3.setheading(0)
                if (xh==11):
                    z4.sety(0)
                    f4.sety(0)
                if (xh==13):
                    z5.setx(0)
                    f5.setx(0)
                if (xh==14):
                    z5.sety(0)
                    f5.sety(0)
                if (xh==16):
                    z6.setx(0)
                    f6.setx(0)
                if (xh==18):
                    z6.setheading(0)
                    f6.setheading(0)
                if (xh==20):
                    z7.sety(0)
                    f7.sety(0)
                if (xh==23):
                    z8.sety(0)
                    f8.sety(0)
            xunhuan.backward(1)
            q3=(int(q3fz.xcor()))
        xunhuan.setx(23)
        while (q4<0)and((int(xunhuan.xcor()))!=0):
            if ((yyz[(int(xunhuan.xcor()))-1])==4):
                q4fz.forward((jg[(int(xunhuan.xcor()))]/10))
                xh=(int(xunhuan.xcor()))
                if (xh==1):
                    z1.setx(0)
                    f1.setx(0)
                if (xh==3):
                    z1.setheading(0)
                    f1.setheading(0)
                if (xh==4):
                    z2.setx(0)
                    f2.setx(0)
                if (xh==6):
                    z2.setheading(0)
                    f2.setheading(0)
                if (xh==8):
                    z3.sety(0)
                    f3.sety(0)
                if (xh==9):
                    z3.setheading(0)
                    f3.setheading(0)
                if (xh==11):
                    z4.sety(0)
                    f4.sety(0)
                if (xh==13):
                    z5.setx(0)
                    f5.setx(0)
                if (xh==14):
                    z5.sety(0)
                    f5.sety(0)
                if (xh==16):
                    z6.setx(0)
                    f6.setx(0)
                if (xh==18):
                    z6.setheading(0)
                    f6.setheading(0)
                if (xh==20):
                    z7.sety(0)
                    f7.sety(0)
                if (xh==23):
                    z8.sety(0)
                    f8.sety(0)
            xunhuan.backward(1)
            q4=(int(q4fz.xcor()))
        q1=(int(q1fz.xcor()))
        q2=(int(q2fz.xcor()))
        q3=(int(q3fz.xcor()))
        q4=(int(q4fz.xcor()))
        draw.setpos(-350,190)
        draw2.setpos(-350,50)
        draw3.setpos(-350,-65)
        draw4.setpos(-350,-215)
        if (pc1==0):
            turtle.setpos(-390,180)
            turtle.write(q1, align="left",font=("宋体",15,"normal"))
        if (pc2==0):
            turtle.setpos(-390,40)
            turtle.write(q2, align="left",font=("宋体",15,"normal"))
        if (pc3==0):
            turtle.setpos(-390,-75)
            turtle.write(q3, align="left",font=("宋体",15,"normal"))
        if (pc4==0):
            turtle.setpos(-390,-225)
            turtle.write(q4, align="left",font=("宋体",15,"normal"))
        if (q1<0):
            pc1=1
        if (q2<0):
            pc2=1
        if (q3<0):
            pc3=1
        if (q4<0):
            pc4=1
        if (pc1==1)and(wj1.isvisible()):
            wj1.hideturtle()
            wjs.backward(1)
        if (pc2==1)and(wj2.isvisible()):
            wj2.hideturtle()
            wjs.backward(1)
        if (pc3==1)and(wj3.isvisible()):
            wj3.hideturtle()
            wjs.backward(1)
        if (pc4==1)and(wj4.isvisible()):
            wj4.hideturtle()
            wjs.backward(1)
        if ((wjs.xcor())==1):
            if (pc1==0):
                turtle.textinput("玩家1胜利", "玩家1胜利，游戏结束")
            if (pc2==0):
                turtle.textinput("玩家2胜利", "玩家2胜利，游戏结束")
            if (pc3==0):
                turtle.textinput("玩家3胜利", "玩家3胜利，游戏结束")
            if (pc4==0):
                turtle.textinput("玩家4胜利", "玩家4胜利，游戏结束")
turtle.onscreenclick(touzi,1,add=False)
turtle.listen()
turtle.mainloop()
