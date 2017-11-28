from flask_script import Manager
from myresume import app, db, Professor, Course

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    thomas_Trinter = Professor(name='Thomas Trinter', department='Finance')
    clinton_White = Professor(name='Clinton White', department='Management Information Systems')
    mark_Serva = Professor(name='Mark Serva', department='Management Information Systems')
    edward_Hortono = Professor(name='Edward Hortono', department='Management Information Systems')
    course1 = Course(name='Database Design and Implementation: MISY', course_number=330, description="Covers the design and implementation of enterprise databases in the business environment. A networked setting and its effect on database management will be emphasized. PREREQ: MISY160 or CISC181. RESTRICTIONS: MIS majors and MIS and/or GET minors only. Not open to computer science majors in the MIS minor. Not open to students who double major in both accounting and management information systems.", professor=mark_Serva)
    course2 = Course(name='Corporate Finance FINC', course_number=413, description="This capstone seminar course studies three different intersections of topics in global corporate finance: the intersections of a) currency and interest rate risk management, b) capital raising and securities market trading, and c) strategy and international financial management. The course emphasizes reports, exercises, cases, discussions, presentations, and analysis of financial news. PREREQ: FINC311, FINC312, FINC314. RESTRICTIONS: Open to Junior and Senior Finance Majors & MISY Majors with Finance concentrations only.", professor=thomas_Trinter)
    course3 = Course(name='Introduction to Programming Business Applications MISY', course_number=225, description="Use of higher level contemporary computing languages to structure Prototyping applications of systems. PREREQ: MISY160 or CISC101. RESTRICTIONS: Not open to CIS majors in the MIS minor.", professor=edward_Hortono)
    course4 = Course(name='Systems Analysis and Implementation MISY', course_number=430, description="Covers the challenges of developing and managing systems analysis and design projects. Students learn to determine systems requirements, analyze systems problems, model potential solutions and design and implement these solutions. Other current topics will be included to reflect the changing information systems environment. PREREQ: MISY330 or CISC437. RESTRICTIONS: Open to MIS majors and minors and INSY majors only.", professor=clinton_White)
    db.session.add(clinton_White)
    db.session.add(thomas_Trinter)
    db.session.add(mark_Serva)
    db.session.add(edward_Hortono)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
