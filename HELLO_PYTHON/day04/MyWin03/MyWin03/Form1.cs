using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ProgressBar;

namespace MyWin03
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
        }
        public void myClick()
        {
            string result = "";
            int dan = Int32.Parse(tb.Text);
            for (int i = 1; i <= 9; i++){
                result += dan+"*"+i+"="+dan * i+"\r\n";
                tbml.Text = result.ToString();
            }

        }

        private void tb1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
