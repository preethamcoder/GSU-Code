package csc1302;
import java.util.*;

public class Rectangle implements Comparable<Rectangle>{
	private int height;
	private int width;
	private Point topCorner = new Point();
	
	public Rectangle (int h, int w, Point p) {
		height = h;
		width = w;
		topCorner = p;
	}
	public int getHeight() {
		return height;
	}
	public int getWidth() {
		return width;
	}
	public Point getTopCorner() {
		return topCorner;
	}
	
	public String toString() {
		return("Rectangle: "+height+", "+width+", "+topCorner.toString());
	}
	
	
	public int compareTo(Rectangle rt){
		if(height!=rt.height)
			return(height-rt.height);
		else if(width!=rt.width)
			return(width-rt.width);
		else {
			if(this.topCorner.getX()!=topCorner.getX()) {
				return(this.topCorner.getX()-topCorner.getX());
			} else {
				return(this.topCorner.getY()-topCorner.getY());
			}
			
		}
		
	}
}
