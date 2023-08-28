using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace myWin04
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void btncall_Click(object sender, EventArgs e)
        {
            myClick();
        }
        public void myClick()
        {

            int count1 = Int32.Parse(btn1.Text);
             tb.Text = count1.ToString();
            
        }
    }
}
