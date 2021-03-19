package csc1302;
import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class PushCounterPanelMath extends JPanel{
	private int value;
	   private JButton inc, dec;
	   private JLabel label;

	   //-----------------------------------------------------------------
	   //  Constructor: Sets up the GUI.
	   //-----------------------------------------------------------------
	   public PushCounterPanelMath()
	   {
	      value = 50;

	      inc = new JButton("Increment");
	      dec = new JButton("Decrement");
	      label = new JLabel("Value: " + value);
	      inc.addActionListener(new ButtonListener());
	      dec.addActionListener(new ButtonListener());
	      
	      add(inc);
	      add(dec);
	      add(label);

	      setBackground(Color.cyan);
	      setPreferredSize(new Dimension(300, 40));
	      
	      
	}
	   private class ButtonListener implements ActionListener
		{
			public void actionPerformed(ActionEvent event)
	 		{
					String s = event.getActionCommand();
					if(s.equals("Increment")) {
						value += 1;
						label.setText("Number: "+ value);
					}else {
						value -= 1;
						label.setText("Number: "+ value);
					}
	 		}
		}
}
