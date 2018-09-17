function setup() 
{
  createCanvas(384,384);
  stroke(0);
  strokeWeight(3);
  background(0,255,255);
  noFill();
}

var x=24;
var right=0; 
count=10;

function draw() 
{
  if (x == 24)
  {
    right=0;
    count=count-2;
  }
  if (x == 360)
  {
    right=1;
    count=count-2;
  }
  if (right == 1)
  {
    clear();
    ellipse(x,height/2,48,48);
    x=x-count;
  }
  else
  {
    clear();
    ellipse(x,height/2,48,48);
    x=x+count;
  }
  if (count == 0)
  {
    noLoop();
  }
}
