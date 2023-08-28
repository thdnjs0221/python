using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Mywin04

{
    public partial class Form1 : Form

    {
        String number = "";

       
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }


        private void btn1_Click_1(object sender, EventArgs e)
        {
            number += ((Button)sender).Text;
            tb.Text = number;

        }

        private void btncall_Click(object sender, EventArgs e)
        {
            MessageBox.Show(number + "\ncalling");
        }

    }
}
