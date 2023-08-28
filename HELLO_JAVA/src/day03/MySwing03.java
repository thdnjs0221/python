package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JButton btn;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단수");
		lbl.setBounds(137, 14, 57, 15);
		contentPane.add(lbl);
		
		btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(137, 43, 97, 23);
		contentPane.add(btn);
		
		tf = new JTextField();
		tf.setBounds(206, 11, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		ta = new JTextArea();
		ta.setBounds(137, 76, 204, 156);
		contentPane.add(ta);
		
	}

	public void myClick() {
		int count=Integer.parseInt(tf.getText());
		for(int i =1; i<=9; i++) {
			ta.append(count+"*"+i+"="+count*i+"\n");
			//ta.setText("")
			
		}
		
	}
}
