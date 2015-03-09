
from unittest import TestLoader, TextTestRunner

import time
import HTMLTestRunner
# Import smtplib for the actual sending function
import smtplib
# Import the email modules
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from datetime import date
from email import encoders
import trail_test
import gmail

#from worklist import Worklistpage

if __name__ == '__main__':
    loader = TestLoader()

    '''
    #prerequisite test to setup server if unavailable
    suite = loader.loadTestsFromName('AutomationTest.test_title',module = trail_test)
    suite.addTest(loader.loadTestsFromName('AutomationTest.test_article_1', module = trail_test))
    '''
    suite = loader.loadTestsFromName('AutomationTest.test_title',module = gmail)
    suite.addTest(loader.loadTestsFromName('AutomationTest.login', module = gmail))
    suite.addTest(loader.loadTestsFromName('AutomationTest.login_no_username', module = gmail))





    #running the tests added to suite
    report_filename = 'test_report_' + str(date.today()) + '.html'
    fp = open(report_filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=3, title='Automation Test Results')
    result = runner.run(suite)
    print('runtests rc = %s' % result.wasSuccessful())

    print ('Tests run ', result.testsRun)
    print ('Errors ', result.errors)
    print ('Errors ', result.error_count)
    print('failures', result.failures)
    print('failures', result.failure_count)
    fp.close()

    # Define email addresses to use
    addr_to   = 'autotest.raavi@gmail.com'
    addr_from = 'autotest.raavi@gmail.com'



    gmail_user = 'autotest.raavi@gmail.com'
    gmail_pwd = 'autotest'
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.login(gmail_user, gmail_pwd)

    # Construct email
    msg = MIMEMultipart('alternative')
    msg['To'] = addr_to
    msg['From'] = addr_from
    msg['Subject'] = 'Test Email From automation'

    # Create the body of the message (a plain-text and an HTML version).
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(report_filename, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename = automation_report_'+ str(date.today()) + '.html')
    msg.attach(part)
    f = open(report_filename, 'r')
    body = ''.join(f)
    f.close()
    smtpserver.sendmail(gmail_user, addr_to, str(msg))


