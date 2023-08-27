package day03;

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;

public class MySwing01 extends JFrame implements ActionListener {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing01 frame = new MySwing01();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
		new MySwing01();
	}

	/**
	 * Create the frame.
	 */
	public MySwing01() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 296);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("New label");
		lblNewLabel.setBounds(56, 64, 57, -19);
		contentPane.add(lblNewLabel);
		
		JLabel lbl = new JLabel("Good Morning");
		lbl.setBounds(56, 42, 85, 15);
		contentPane.add(lbl);
		
		JLabel lbl2 = new JLabel("Good Nigth");
		lbl2.setBounds(56, 42, 85, 15);
		contentPane.add(lbl2);
		
		JButton btn = new JButton("CLICK");
		btn.setBounds(165, 38, 97, 23);
		contentPane.add(btn);
		
		btn.addActionListener(this);
		
		contentPane.add(btn);
		add(contentPane);
		setVisible(true);
		
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==lbl2) {
			contentPane.set
			
		}
		

	}
}
