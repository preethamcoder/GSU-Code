package csc1302;
import java.awt.Component;

import javax.swing.JFrame;
public class PushCounterMath {
	public static void main(String[] args) {
		JFrame frame = new JFrame("Increment/Decrement");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		PushCounterPanelMath panel = new PushCounterPanelMath();
		frame.getContentPane().add(panel);
		
		frame.pack();
		frame.setVisible(true);
	}
}
