package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;
	private JLabel lbl2;
	private JTextField tf4;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 529, 226);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(54, 47, 116, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lbl1 = new JLabel("에서");
		lbl1.setBounds(189, 50, 57, 15);
		contentPane.add(lbl1);
		
		tf2 = new JTextField();
		tf2.setColumns(10);
		tf2.setBounds(218, 47, 116, 21);
		contentPane.add(tf2);
		
		lbl2 = new JLabel("까지");
		lbl2.setBounds(335, 50, 57, 15);
		contentPane.add(lbl2);
		
		tf3 = new JTextField();
		tf3.setColumns(10);
		tf3.setBounds(373, 47, 116, 21);
		contentPane.add(tf3);
		
		JButton btn = new JButton("배수의합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				Myclick();
			}
		});
		btn.setBounds(381, 92, 97, 23);
		contentPane.add(btn);
		
		tf4 = new JTextField();
		tf4.setColumns(10);
		tf4.setBounds(373, 139, 116, 21);
		contentPane.add(tf4);
	}
	
	public void Myclick() {
		int sum=0;
		int a = Integer.parseInt(tf1.getText());
		int b = Integer.parseInt(tf2.getText());
		int c = Integer.parseInt(tf3.getText());
		
		for (int i=a; i<=b; i++) {
			if(i%c==0 ) {
				sum+=i;
				tf4.setText(String.valueOf(sum));
			}
		}
		
		
				
		
		
		
		
	}
}
