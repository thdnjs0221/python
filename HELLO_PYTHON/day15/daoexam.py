import pymysql
class DaoExam :
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = "select e_id, m_id, kor, eng, math from exam"
        self.curs.execute(sql)
        mylist = self.curs.fetchall()
        return mylist
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
    
    def selectOne(self,e_id):
        sql = f"""
            select e_id, m_id, kor, eng, math from exam where e_id='{e_id}'
            """
        self.curs.execute(sql)
        mylist = self.curs.fetchall()
        return mylist[0]
    
    def insert(self,e_id,m_id,kor,eng,math):
        sql = f"""
            insert into exam(e_id, m_id, kor, eng, math)
            values ('{e_id}','{m_id}','{kor}','{eng}','{math}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self,e_id,m_id,kor,eng,math):
        sql = f"""
            update exam set m_id='{m_id}',kor='{kor}',eng='{eng}',math='{math}'
            where e_id='{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f"""
            delete from exam where e_id='{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
 
    

if __name__=='__main__':
    de = DaoExam()
    exam = de.delete('2')
    print("exam",exam)
