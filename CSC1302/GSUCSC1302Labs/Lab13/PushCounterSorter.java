package csc1302;
/**
 * @author sthelluri1
 *
 */
import javax.swing.*;
import java.awt.*;
public class PushCounterSorter {

	/**
	 * @parm args
	 */
	public static void main(String[] args) {
		JFrame frame = new JFrame("Sorter");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		PushCounterPanelSorter panel = new PushCounterPanelSorter();
		frame.getContentPane().add(panel);
		
		frame.pack();
		frame.setVisible(true);
	}

}

