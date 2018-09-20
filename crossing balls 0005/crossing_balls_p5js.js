function setup() 
{
  createCanvas(500,500);
  stroke(0);
  strokeWeight(5);
  background(255,255,255);
  noFill();
}

var x=50;
var y=450;
var right=0;

function draw() 
{
  if (x == 50 && y == 450)
  {
    right=0;
  }
  if (x == 450 && y == 50)
  {
    right=1;
  }
  if (right == 1)
  {
    clear();
    ellipse(x,height/2,100,100);
    x=x-5;
    ellipse(y,height/2,100,100);
    y=y+5;
  }
  else 
  {
    clear();
    ellipse(x,height/2,100,100);
    x=x+5;
    ellipse(y,height/2,100,100);
    y=y-5;   
  }
}
