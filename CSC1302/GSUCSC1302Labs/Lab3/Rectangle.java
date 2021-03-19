package csc1302;
/*@author Preetham Thelluri
 * The purpose of this lab is to see how certain methods can be overridden and used. 
 * In this case, we are overriding the toString() method.
 * */
public class Rectangle {
	int x = 0;
	int y = 0;
	int height = 0;
	int width = 0;
	public void setFields(int newx, int newy, int newheight, int newwidth) {
		x = newx;
		y = newy;
		height = newheight;
		width = newwidth;
	}	
	public int getX() {
		return x;
	}
	public int getY() {
		return y;
	}
	public int getheight() {
		return height;
	}
	public int getwidth() {
		return width;
	}
	public int area() {
		return(height * width);
	}
	public int perimeter() {
		return(2*(height + width));
	}
	public String toString() {
		return("Rectangle [x = " + getX() + ", y = " + getY() + ", height = " + getheight() + ", width = " + getwidth() + "] Area is " + area() + ".");
	}
}
