namespace MyWin01
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btn_Click(object sender, EventArgs e)
        {
            myClick();
            Console.WriteLine("Myclick");
        }
        public void myClick() {

            lbl.Text = "Good Evening";

        }
    }
}