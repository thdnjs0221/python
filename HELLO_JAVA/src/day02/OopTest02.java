package day02;

public class OopTest02 {
	public static void main(String[] args) {
		Animal ani = new Animal();
		System.out.println("flagLife:"+ani.flagLife);
		ani.die();
		System.out.println("flagLife:"+ani.flagLife);
	}

}
