/**
 * 
 */
package csc1302;
import java.util.*;
/**
 * @author Preetham Thelluri
 *
 */
public class Point implements Comparable<Point> {
    private int x;
    private int y;
    public Point() {
        this(0, 0);
    }

    public Point(int x, int y) {
        this.x=x;
        this.y=y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    public int compareTo(Point pt){
	if(x==pt.x)
		return y-pt.y;
	else
		return x-pt.x;
    }
}

