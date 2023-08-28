package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing05 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JButton btn;
	private JTextField tfResult;
	

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing05 frame = new MySwing05();
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
	public MySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("나:");
		lblMine.setBounds(79, 32, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("컴:");
		lblCom.setBounds(79, 68, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel(" 결과:");
		lblResult.setBounds(79, 107, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.setBounds(128, 29, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(128, 65, 116, 21);
		contentPane.add(tfCom);
		
		btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(100, 138, 97, 23);
		contentPane.add(btn);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(128, 104, 116, 21);
		contentPane.add(tfResult);
	}
	
	public void myClick() {
		String me=tfMine.getText();
		String com="";
		String result="";
		
		double rnd = Math.random();
		
	 System.out.println(com);
	 if(rnd>0.5) {
		com="홀";
	 }else{
		 com="짝"; 
	 }
	 if(me.equals(com)) {
		 result="이김";
	 }else {
		 result="짐";
	 }
	 tfCom.setText(com);
	 tfResult.setText(result);
	 
	 
	 
	 
	
	 
		
	}
}
