package csc1302;
import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class PushCounterPanelSorter extends JPanel implements ActionListener{
	private JLabel label;
	private JButton button;
	private JTextField num1, num2, num3, num4, num5;
	public PushCounterPanelSorter() {
		//setSize(800, 300);
		button = new JButton("SORT");
		num1 = new JTextField(12);
		num2 = new JTextField(12);
		num3 = new JTextField(12);
		num4 = new JTextField(12);
		num5 = new JTextField(12);
		label = new JLabel("");
		add(num1);
		add(num2);
		add(num3);
		add(num4);
		add(num5);
		add(button);
		add(label);
		setBackground(Color.cyan);
		setPreferredSize(new Dimension(400, 300));
		button.addActionListener(this);
		//setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
		public void actionPerformed(ActionEvent event)
 		{
			int aa = Integer.parseInt(num1.getText());
			int bb = Integer.parseInt(num2.getText());
			int c = Integer.parseInt(num3.getText());
			int d = Integer.parseInt(num4.getText());
			int e = Integer.parseInt(num5.getText());
			int[] arr = {aa,bb,c,d,e};
			int temp;
			for(int a = 0; a < arr.length-1; a++) {
				for(int b = 0; b < arr.length-1; b++) {
					if(arr[b] > arr[b+1]) {
						temp = arr[b];
						arr[b] = arr[b+1];
						arr[b+1] = temp;
					}
				}
			label.setText("A sorted array: " + Arrays.toString(arr));
			
	}
}
}
