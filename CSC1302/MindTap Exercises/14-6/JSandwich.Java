import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class JSandwich extends JFrame implements ItemListener {
    FlowLayout flow = new FlowLayout();
    JLabel companyName = new JLabel("Sublime Sandwich");
    JComboBox<String> mainBox = new JComboBox<String>();
    JLabel mainList = new JLabel("Main ingredient");
    JComboBox<String> breadBox = new JComboBox<String>();
    JLabel breadList = new JLabel("Breads");
    JTextField totPrice = new JTextField(10);
    int mainNum, breadNum;
    double[] mainPrices = {6.99, 7.99, 8.99};
    double sumPrice = mainPrices[0];
    double breadPrice = 0;
    double mainPrice = mainPrices[0];
    double[] breadPrices = {0, 0, 0};
    String output;
    public JSandwich() {
        super("Sublime Sandwich Shop");
        add(mainList);
        add(mainBox);
        //mainBox.addItem("");
        mainBox.setSize(150, mainBox.getPreferredSize().height);
        mainBox.addItemListener(this);
        mainBox.addItem("Chicken");
        mainBox.addItem("Beef");
        mainBox.addItem("Tuna");
        add(breadBox);
        breadBox.setSize(150, breadBox.getPreferredSize().height);
        breadBox.addItem("");
        breadBox.addItem("White");
        breadBox.addItem("Rye");
        breadBox.addItem("Whole Wheat");
        add(totPrice);
    }
    public static void main(String[] arguments) {
        JSandwich sandframe = new JSandwich();
        sandframe.setSize(240, 200);
        sandframe.setVisible(true);
    }

    @Override
    public void itemStateChanged(ItemEvent list) {
        int i = mainBox.getSelectedIndex();
        if(i == 0){
            totPrice.setText("$6.99");
        }else if(i == 1){
            totPrice.setText("$7.99");
        }else{
            totPrice.setText("$8.99");
        }
    }
}
