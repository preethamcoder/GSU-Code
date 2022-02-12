package csc1302;
import javax.swing.JFrame;
public class PushCounter
{
//-----------------------------------------------------------------
//  Creates and displays the main program frame.
//-----------------------------------------------------------------
public static void main(String[] args)
{
      JFrame frame = new JFrame("Push Counter");
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

      PushCounterPanel panel = new PushCounterPanel();
      frame.getContentPane().add(panel);

      frame.pack();
      frame.setVisible(true);
}
}
