package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * 2. MySwing09.java -> 야구게임 String com = "415" ->
	 * 
	 * 123
	 * 
	 * 123_0s1b 지워주기
	 * 
	 * 415_3s0b ->alert 415 맞췄습니다 (자바 스윙 alert)
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("맞출수:");
		lbl.setBounds(35, 40, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(85, 37, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
		
			}
		});
		btn.setBounds(65, 78, 97, 23);
		contentPane.add(btn);
		
		JTextArea ta = new JTextArea();
		ta.setBounds(35, 118, 176, 133);
		contentPane.add(ta);
	}
	public void myClick() {
		
		
		
	}
	public int randCom() {
		int [] arr= {1,2,3,4,5,6,7,8,9};
		for(int i=0; i<=100; i++) {
			int rnd = (int)(Math.random()*9);
			
			int a = arr[0];
			arr[0]=arr[rnd];
			arr[rnd]=a;
			
			int[]randCom={arr[0],arr[1],arr[2]};
		
		}
		return randCom();
		
	}
	public int getS() {
		int cnt=0;
		
		
	}
	
	
	
	
}
