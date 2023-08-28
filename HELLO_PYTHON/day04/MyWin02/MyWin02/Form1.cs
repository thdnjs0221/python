using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MyWin02
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
            int count = Int32.Parse(tb.Text);
            count = count - 1;
           // count--;
            tb.Text = count.ToString();
            

        }
    }
}
