void setup ()
{
size(500,500);
stroke(0);
strokeWeight(5);
background(255,0,0);
//noFill();
}
//int x=(3/8)*width,y=(3/8)*height;
void draw()
{
  rect(width/8,height/8,width/4,height/4);
  rect(3*width/8,3*width/8,width/4,height/4);
  rect(5*width/8,5*width/8,width/4,height/4);
  ellipse(width/4,height/4,width/4,width/4);
  ellipse(width/2,width/2,width/4,width/4);
  ellipse(3*width/4,3*width/4,width/4,height/4);
  point(width/4,height/4);
  point(width/2,height/2);
  point(3*width/4,3*width/4);
}
