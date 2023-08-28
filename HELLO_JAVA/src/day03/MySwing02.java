package day03;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;

public class MySwing02 extends JFrame {

   private JPanel contentPane;
   private JTextField tf;

   /**
    * Launch the application.
    */
   public static void main(String[] args) {
      EventQueue.invokeLater(new Runnable() {
         public void run() {
            try {
               MySwing02 frame = new MySwing02();
               frame.setVisible(true);
            } catch (Exception e) {
               e.printStackTrace();
            }
         }
      });
   }

   /**
    * Create the frame.
    */
   public MySwing02() {
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      setBounds(100, 100, 450, 300);
      contentPane = new JPanel();
      contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

      setContentPane(contentPane);
      contentPane.setLayout(null);
      
      tf = new JTextField();
      tf.setText("100");
      tf.setBounds(12, 10, 116, 21);
      contentPane.add(tf);
      tf.setColumns(10);
      
      
      
      
      
      JButton btn = new JButton("INCREASE");
      btn.setBounds(140, 9, 97, 23);
      contentPane.add(btn);
      
      btn.addMouseListener(new MouseAdapter() {
         public void mouseClicked(MouseEvent e) {
            myClick();
         }
      });
      
   }
   
   public void myClick() {
      int count = Integer.parseInt(tf.getText());
      count++;
      tf.setText(String.valueOf(count));
   }
}