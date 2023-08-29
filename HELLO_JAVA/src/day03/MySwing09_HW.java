package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Arrays;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JLabel lbl;
	private JTextField tf;
	private JTextArea ta;
	private int[] com;
	private String comNum;
	static int[] randCom;

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
		setBounds(100, 100, 531, 433);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl = new JLabel("맞출수:");
		lbl.setBounds(71, 86, 101, 49);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(137, 100, 106, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
				//randCom();
				
			}
		});
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn.setBounds(103, 131, 95, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(71, 164, 217, 203);
		contentPane.add(ta);
	}
	public void myClick() {
		 String mine = tf.getText();

	        if (com == null) {
	            com = randCom();
	            comNum = Arrays.toString(com);
	           // ta.setText("컴퓨터: " + comNum + "\n");
	            System.out.println(comNum);
	        }

	        int s = getS(mine, comNum);
	        int b = getB(mine, comNum);

	        if (s == 3) {
	            JOptionPane.showMessageDialog(null, mine + "  " + s + "S" + b + "B  정답입니다");
	            ta.setText(""); // 정답을 맞추면 입력 필드를 초기화
	            ta.append(mine + "\t" + s + "S" + b + "B  정답입니다\n"); // 결과 출력 영역에 정답을 추가
	            com = null; // 컴퓨터 숫자 초기화
	        } else {
	        	ta.setText("");
	            ta.append(mine + "\t" + s + "S" + b + "B\n"); // 결과 출력 영역에 현재 결과를 추가
	        }
	    }
      
    
		

	public int[] randCom() {
	    int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};
	    
	    for (int i = 0; i <= 100; i++) {
	        int rnd = (int) (Math.random() * 9);

	        int a = arr[0];
	        arr[0] = arr[rnd];
	        arr[rnd] = a;
	    }
	    
	    int[] randCom = {arr[0], arr[1], arr[2]};
	    
	    
	   
	    return randCom;
	}
	
	 public static int getS(String mine, String com) {
		 
		 
		 
	        int cnt = 0;
	        String m1 = mine.substring(0, 1);
	        String m2 = mine.substring(1, 2);
	        String m3 = mine.substring(2, 3);

	        String c1 = com.substring(1, 2); // 첫 번째 숫자인 7 추출
	        String c2 = com.substring(4, 5); // 두 번째 숫자인 2 추출
	        String c3 = com.substring(7, 8); // 세 번째 숫자인 4 추출

	        if (m1.equals(c1)) cnt++;
	        if (m2.equals(c2)) cnt++;
	        if (m3.equals(c3)) cnt++;

	        return cnt;
	    }
	 public static int getB(String mine, String com) {
	        int cnt = 0;
	        String m1 = mine.substring(0, 1);
	        String m2 = mine.substring(1, 2);
	        String m3 = mine.substring(2, 3);

	        String c1 = com.substring(1, 2); // 첫 번째 숫자인 7 추출
	        String c2 = com.substring(4, 5); // 두 번째 숫자인 2 추출
	        String c3 = com.substring(7, 8); // 세 번째 숫자인 4 추출

	        if (m1.equals(c2) || m1.equals(c3)) cnt++;
	        if (m2.equals(c1) || m2.equals(c3)) cnt++;
	        if (m3.equals(c1) || m3.equals(c2)) cnt++;

	        return cnt;
	    }
	 

}
