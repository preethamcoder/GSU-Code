package csc1302;

public class ColoringPoint extends Point implements Coloring {

	private int x;
	private int y;
	private String color;
	
	public ColoringPoint(int xa, int ya, String colores) {
		super(xa, ya);
		color = colores;
	}
	public void setColor(String coloro) {
		color = coloro;
	}
	public String getColor() {
		return color;
	}
	public boolean equals(Object o) {
		if (o instanceof ColoringPoint) {
            ColoringPoint other = (ColoringPoint) o;
            return (x == other.getX() && y == other.getY() && color.equals(other.getColor())); //TRUE if they are the same
        } else {  
            return false;
        }
	}
	public String toString() {
		return("x = " + super.getX() + ", y = " + super.getY() + ", color " + getColor());
	}
}
