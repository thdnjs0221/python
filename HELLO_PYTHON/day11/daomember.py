import pymysql
class DaoMem :
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = "select * from member"
        self.curs.execute(sql)
        mylist = self.curs.fetchall()
        return mylist
    
    def selectOne(self,m_id):
        sql = f"""
            select m_id, m_name, tel, email from member where m_id='{m_id}' 
            """
        self.curs.execute(sql)
        mylist = self.curs.fetchall()
        return mylist[0]
    
    def insert(self,m_name,tel,email):
        sql = f"""
            insert into member ( m_name, tel, email)
            values ('{m_name}','{tel}','{email}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
 
    def update(self,m_id,m_name,tel,email):
        sql = f"""
            update member set m_name='{m_name}',tel='{tel}',email='{email}'
            where m_id='{m_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt

    def delete(self,m_id):
        sql = f"""
            delete from member where m_id='{m_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
    
if __name__=='__main__':
    de = DaoMem()
    cnt = de.delete('1')
    # cnt = dm.insert('2','2','2')
    print("cnt",cnt)
