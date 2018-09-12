function setup() 
{
  createCanvas(windowWidth,windowHeight);
  stroke(0);
  strokeWeight(5);
  background(255,255,255);
  noFill();
}
var x=50;
var right=0 
w=100
h=100

function draw() 
{
  if (x == 50)
  {
    right=0
  }
  if (x == (width-50))
  {
    right=1;
  }
  if (right == 1)
  {
    clear();
    ellipse(x,height/2,w,h);
    x=x-5;
  }
  else 
  {
    clear();
    ellipse(x,height/2,w,h);
    x=x+5
  }
}
